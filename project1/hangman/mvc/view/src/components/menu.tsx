import { 
    MenuItem 
} from '../utils/enums';

import {
    StatePageProps
} from '../utils/interfaces';


/**
 * Function will create a menu that asks the user to choose out 
 * of the following options:
 *  - Start a new game
 *  - Quit the game
 *  - Choose a new username 
 * 
 * These options will each be a button that will send the corresponding
 *  string back through the menuSelection api
 *  for a new game state.
 * 
 * There will also be a box that will display:
 *  - The current username
 *  - The number of wins for that username
 *  - The number of losses for that username
 */
export function MenuPage(props: StatePageProps) {

    function submitSelection(selection: MenuItem) {
        props.api.menuSelection(selection)
            .then(res => {
                console.log("Menu Selection Results: ", res.menuSelection)
                props.setState(res.menuSelection);
            })
            .catch(console.error);
    }

    return (
        <div>
            <h1>Hangman</h1>
            <p>Guess the word</p>
            <button onClick={() => submitSelection(MenuItem.PLAY_GAME)}>
                Play Game
            </button>
            <button onClick={() => submitSelection(MenuItem.NEW_PLAYER)}>
                New Player
            </button>
            <button onClick={() => submitSelection(MenuItem.QUIT_GAME)}>
                Quit Game
            </button>

            <p>Username: {props.state.name}</p>
            <p>Wins: {props.state.wins}</p>
            <p>Losses: {props.state.losses}</p>
        </div>

    );
}
