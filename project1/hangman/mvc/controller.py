'''
    Assignment - Project 1: Hangman
    File: controller.py
    Description: This program will control the game and manages passing the game state
        to the view in display.py.
    James Halladay
    Advanced Programming with Python
    Date: 8/29/2022


    *******************************************************************************
        Here we are building a hangman game.  The game will use a MVC design pattern 
            where the model is in ./game.py, the view is in ./display.py, and this file
            is the controller.
    *******************************************************************************
'''
import os

from datetime import (
    datetime
)

from flask import (
    Flask, 
    send_from_directory, 
    render_template,
    request,
    jsonify
)

from ariadne import (
    ObjectType,
    graphql_sync,
    load_schema_from_path,
    make_executable_schema,
)

from ariadne.constants import (
    PLAYGROUND_HTML
)

from hangman.mvc.model import (
    Model
)

from hangman.utils.functions import (
    pretty
)

from hangman.utils.constants import (
    MenuItems,
    GameStates,
    Response,
    ResponseField,
)

from hangman.utils.finite_state_machine import (
    STATE_TRANSITION_TABLE,
    State,
    Action,
)


class Controller:
    '''
        This class will control the game state and the server that 
            will be used to send the view to the browser.
        
        The game state is controlled by the finite state machine in
            ./utils/finite_state_machine.py
    '''
    
    game: Model
    app: Flask
    state: State
    

    def __init__(self, name: str, game: Model):

        # First we set up the basic constants
        self.game = game
        self.name = name
        self.state = State.START_STATE.value

        # We set up the flask app
        self.app = Flask(
            name, 
            template_folder = os.path.abspath('mvc/view/build'),
            static_folder = os.path.abspath('mvc/view/build')
        )
        
        # Queries though GraphQL
        self.query = ObjectType("Query")
        self.query.set_field("getState", self.get_state)

        # Mutations though GraphQL
        self.mutation = ObjectType("Mutation")
        self.mutation.set_field("performAction", self.perform_action)
        self.mutation.set_field("performDefaultAction", self.perform_default_action)
        self.mutation.set_field("startGame", self.start_game)
        self.mutation.set_field("submitUsername", self.check_username)
        self.mutation.set_field("menuSelection", self.menu_selection)
        self.mutation.set_field("submitDifficulty", self.submit_difficulty)
        self.mutation.set_field("terminate", self.terminate)
        self.mutation.set_field("submitGuess", self.submit_guess)

        self.type_defs = load_schema_from_path('schema.graphql')
        self.schema = make_executable_schema(
            self.type_defs,
            [
                self.query, 
                self.mutation
            ],
        )

        # Finally, we set up the routes
        self.routes()

    
    def run(self):
        self.app.run(port = '4999', debug = True)
        self.state = State.START_STATE.value


    def create_response(self, calling_method: callable, success: bool = False) -> Response:
        return {
            ResponseField.guessedWord.name: ' '.join(self.game.guessed_word),
            ResponseField.success.name    : success,
            ResponseField.time.name       : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            ResponseField.method.name     : calling_method.__name__,
            ResponseField.state.name      : self.state,
            ResponseField.name.name       : self.game.name,
            ResponseField.wins.name       : self.game.wins,
            ResponseField.losses.name     : self.game.losses,
            ResponseField.missed.name     : self.game.missed,
            ResponseField.message.name    : [],
            ResponseField.errors.name     : [],
        }


    def start_game(self, obj, info) -> Response:
        
        response = self.create_response(self.start_game, success = True)
        self.state = State.START_STATE.value
        self.game.initialize_db()

        return response


    def get_state(self, obj, info) -> Response:

        return self.create_response(self.get_state, success = True)


    def get_new_state(self, action: Action) -> State:
        return STATE_TRANSITION_TABLE[action][self.state]


    def perform_action(self, obj, info, action: Action) -> Response:
        payload: Response = self.create_response(self.perform_action, success = True)
        old_state = self.state

        try:
            self.state = self.get_new_state(action)
            payload[ResponseField.state.name] = self.state

        except Exception as error:
            payload[ResponseField.errors.name].append(str(error))            

        if self.state == State.ERROR.value:
            payload[ResponseField.success.name] = False
            payload[ResponseField.errors.name].append(
                f"Invalid Action for State. Action: {action}, State: {old_state}",
            )

        return payload
        

    def perform_default_action(self, obj, info) -> Response:
        return self.perform_action(None, None, Action.DEFAULT.value)


    def check_username(self, obj, info, username: str) -> Response:
        payload: Response = self.create_response(self.check_username, success = False)
        old_state = self.state
        
        if self.game.new_player(username)[0]:
            self.state = self.get_new_state(Action.NO_NAME.value)
            payload[ResponseField.message.name].append("Created new player: " + username)

        elif self.game.load_game(username)[0]:
            self.state = self.get_new_state(Action.NAME_EXISTS.value)
            payload[ResponseField.message.name].append("Loaded player: " + username)

        if self.state == State.CREATE_PLAYER_STATE.value or self.state == State.LOAD_PLAYER_STATE.value:
            payload[ResponseField.success.name] = True
            payload[ResponseField.name.name] = self.game.name
            self.state = self.get_new_state(Action.DEFAULT.value)

        else:
            payload[ResponseField.errors.name].append("Error in username check")
            payload[ResponseField.errors.name].append(
                f"Invalid Action for State. Action: {Action.NO_NAME.value} or {Action.NAME_EXISTS.value}, State: {old_state}",
            )

        payload[ResponseField.state.name]  = self.state
        payload[ResponseField.wins.name]   = self.game.wins
        payload[ResponseField.losses.name] = self.game.losses
        payload[ResponseField.missed.name] = self.game.missed

        return payload


    def menu_selection(self, obj, info, selection: str) -> Response:

        payload: Response = self.create_response(self.menu_selection, success = True)
        old_state = self.state

        if selection == MenuItems.PLAY_GAME.value: 
            self.state = self.get_new_state(Action.PLAY.value)
            payload[ResponseField.message.name].append("Starting Game")

        elif selection == MenuItems.QUIT_GAME.value:
            self.state = self.get_new_state(Action.QUIT.value)
            payload[ResponseField.message.name].append("Quitting Game")

        elif selection == MenuItems.NEW_PLAYER.value:
            self.state = self.get_new_state(Action.NEW_PLAYER.value)
            payload[ResponseField.message.name].append("Creating New Player")

        else:
            self.state = self.get_new_state(Action.NO_ACTION.value)
            payload[ResponseField.success.name] = False
            payload[ResponseField.errors.name].append("Invalid Menu Selection")

        if self.state == State.ERROR.value:
            payload[ResponseField.success.name] = False
            payload[ResponseField.errors.name].append(
                f"Invalid Action for State. Actions: {Action.PLAY.value} | {Action.QUIT.value} | {Action.NEW_PLAYER.value}",
            )

            payload[ResponseField.errors.name].append(
                f"Invalid Action for State. State: {old_state}",
            )

        payload[ResponseField.state.name] = self.state

        return payload


    def submit_difficulty(self, obj, info, difficulty: int) -> Response:
        payload: Response = self.create_response(self.submit_difficulty, success = True)
        old_state: dict   = self.state
        difficulty: int   = int(difficulty)

        self.game.difficulty = difficulty
        self.game.new_word(difficulty)
        self.game.current_guessed_word()

        self.state = self.get_new_state(Action.DEFAULT.value)

        if difficulty >= 1 and difficulty <= 3:
            payload[ResponseField.message.name].append("Starting Easy Game")

        elif difficulty > 3 and difficulty < 6:
            payload[ResponseField.message.name].append("Starting Medium Game")

        elif difficulty >= 6 and difficulty <= 10:
            payload[ResponseField.message.name].append("Starting Hard Game")

        else:
            self.state = self.get_new_state(Action.NO_ACTION.value)
            payload[ResponseField.success.name] = False
            payload[ResponseField.errors.name].append("Invalid Difficulty Selection")

        if self.state == State.ERROR.value:
            payload[ResponseField.success.name] = False
            payload[ResponseField.errors.name].append(
                f"Invalid Action for State. Actions: {Action.DEFAULT.value}, State: {old_state}",
            )

        payload[ResponseField.state.name] = self.state
        payload[ResponseField.word.name] = self.game.word
        payload[ResponseField.guessedWord.name] = ' '.join(self.game.guessed_word)

        return payload
 

    def submit_guess(self, obj, info, guess: str) -> Response:
        payload: Response = self.create_response(self.submit_guess, success = True)

        if self.game.guess(guess):
            if self.game.game_state() == GameStates.WIN:
                self.state = self.get_new_state(Action.WIN.value)
                payload[ResponseField.message.name] = ["You Win!", ]

            elif self.game.game_state() == GameStates.LOSE:
                self.state = self.get_new_state(Action.LOSE.value)
                payload[ResponseField.message.name] = ["You Lose!", ]

        else:
            payload[ResponseField.message.name] = ["Guess Again", ]

        self.game.current_guessed_word()

        payload[ResponseField.state.name]       = self.state
        payload[ResponseField.word.name]        = self.game.word
        payload[ResponseField.guessedWord.name] = ' '.join(self.game.guessed_word)
        payload[ResponseField.missed.name]      = self.game.missed

        if self.state != State.GUESS_STATE.value:
            self.game.new_game()
            self.game.save_game()

        payload[ResponseField.wins.name]        = self.game.wins
        payload[ResponseField.losses.name]      = self.game.losses

        return payload


    def terminate(self, obj, info) -> None:
        os._exit(0)


    def routes(self):
        @self.app.route('/')
        def index():
            return render_template('index.html')

        @self.app.route("/graphql", methods=["GET"])
        def graphql_playground():
            return PLAYGROUND_HTML, 200

        @self.app.route("/graphql", methods=["POST"])
        def graphql_server():
            data = request.get_json()

            success, result = graphql_sync(
                self.schema,
                data,
                context_value=request,
                debug = self.app.debug
            )
 
            status_code = 200 if success else 400
            return jsonify(result), status_code

        @self.app.route('/static/<path:path>') 
        def serve_file(path): 

            file_name = path.split('/')[-1]
            dir_end = '/'.join(['static', *path.split('/')[:-1]])
            dir_name = os.path.join(self.app.static_folder, dir_end)

            return send_from_directory(dir_name, file_name)

        @self.app.route('/<path:path>')
        def serve_public_file(path):

            file_name = path.split('/')[-1]
            dir_end = '/'.join(path.split('/')[:-1])
            dir_name = os.path.join(self.app.static_folder, dir_end)

            return send_from_directory(dir_name, file_name)

        @self.query.field('hello')
        def _(_, info):
            return 'world'



if __name__ == "__main__":
    print('This file is not meant to be run directly.')
