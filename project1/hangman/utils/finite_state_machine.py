
from enum import Enum

from typing import (
    Dict,
    Any
)


GameState = str
GameAction = str


class State(Enum):
    START_STATE        : GameState = 'start_state'
    INPUT_NAME_STATE   : GameState = 'input_name_state'
    CREATE_PLAYER_STATE: GameState = 'create_player_state'
    LOAD_PLAYER_STATE  : GameState = 'load_player_state'
    MENU               : GameState = 'menu_state'
    PLAY_GAME_STATE    : GameState = 'play_state'
    GUESS_STATE        : GameState = 'guess_state'
    WIN_STATE          : GameState = 'win_state'
    LOSE_STATE         : GameState = 'lose_state'
    ERROR              : GameState = 'error_state'
    QUIT_STATE         : GameState = 'quit_state'


class Action(Enum):
    DEFAULT    : GameAction = 'default_action'
    QUIT       : GameAction = 'quit_action'
    PLAY       : GameAction = 'play_action'
    NAME_EXISTS: GameAction = 'name_exists_action'
    NO_NAME    : GameAction = 'no_name_action'
    NEW_PLAYER : GameAction = 'new_player_action'
    WIN        : GameAction = 'win_action'
    LOSE       : GameAction = 'lose_action'
    GUESS      : GameAction = 'guess_action'
    NO_ACTION  : GameAction = 'no_action'



STATE_TRANSITION_TABLE: Dict[GameAction, Dict[GameState, GameState]] = {
    Action.DEFAULT.value: { 
        State.START_STATE.value        : State.INPUT_NAME_STATE.value, 
        State.INPUT_NAME_STATE.value   : State.ERROR.value           , 
        State.CREATE_PLAYER_STATE.value: State.MENU.value            , 
        State.LOAD_PLAYER_STATE.value  : State.MENU.value            , 
        State.MENU.value               : State.ERROR.value           , 
        State.PLAY_GAME_STATE.value    : State.GUESS_STATE.value     , 
        State.GUESS_STATE.value        : State.ERROR.value           , 
        State.WIN_STATE.value          : State.MENU.value            , 
        State.LOSE_STATE.value         : State.MENU.value            , 
        State.ERROR.value              : State.QUIT_STATE.value      , 
        State.QUIT_STATE.value         : State.QUIT_STATE.value      ,
    },

    Action.QUIT.value: { 
        State.START_STATE.value        : State.ERROR.value     , 
        State.INPUT_NAME_STATE.value   : State.ERROR.value     , 
        State.CREATE_PLAYER_STATE.value: State.ERROR.value     , 
        State.LOAD_PLAYER_STATE.value  : State.ERROR.value     , 
        State.MENU.value               : State.QUIT_STATE.value, 
        State.PLAY_GAME_STATE.value    : State.ERROR.value     , 
        State.GUESS_STATE.value        : State.ERROR.value     , 
        State.WIN_STATE.value          : State.ERROR.value     , 
        State.LOSE_STATE.value         : State.ERROR.value     , 
        State.ERROR.value              : State.ERROR.value     , 
        State.QUIT_STATE.value         : State.QUIT_STATE.value,
    },

    Action.PLAY.value: { 
        State.START_STATE.value        : State.ERROR.value          , 
        State.INPUT_NAME_STATE.value   : State.ERROR.value          , 
        State.CREATE_PLAYER_STATE.value: State.ERROR.value          , 
        State.LOAD_PLAYER_STATE.value  : State.ERROR.value          , 
        State.MENU.value               : State.PLAY_GAME_STATE.value, 
        State.PLAY_GAME_STATE.value    : State.ERROR.value          , 
        State.GUESS_STATE.value        : State.ERROR.value          , 
        State.WIN_STATE.value          : State.ERROR.value          , 
        State.LOSE_STATE.value         : State.ERROR.value          , 
        State.ERROR.value              : State.ERROR.value          , 
        State.QUIT_STATE.value         : State.QUIT_STATE.value     ,
    },

    Action.NAME_EXISTS.value: { 
        State.START_STATE.value        : State.ERROR.value            , 
        State.INPUT_NAME_STATE.value   : State.LOAD_PLAYER_STATE.value, 
        State.CREATE_PLAYER_STATE.value: State.ERROR.value            , 
        State.LOAD_PLAYER_STATE.value  : State.ERROR.value            , 
        State.MENU.value               : State.ERROR.value            , 
        State.PLAY_GAME_STATE.value    : State.ERROR.value            , 
        State.GUESS_STATE.value        : State.ERROR.value            , 
        State.WIN_STATE.value          : State.ERROR.value            , 
        State.LOSE_STATE.value         : State.ERROR.value            , 
        State.ERROR.value              : State.ERROR.value            , 
        State.QUIT_STATE.value         : State.QUIT_STATE.value       
    },

    Action.NO_NAME.value: { 
        State.START_STATE.value        : State.ERROR.value              , 
        State.INPUT_NAME_STATE.value   : State.CREATE_PLAYER_STATE.value, 
        State.CREATE_PLAYER_STATE.value: State.ERROR.value              , 
        State.LOAD_PLAYER_STATE.value  : State.ERROR.value              , 
        State.MENU.value               : State.ERROR.value              , 
        State.PLAY_GAME_STATE.value    : State.ERROR.value              , 
        State.GUESS_STATE.value        : State.ERROR.value              , 
        State.WIN_STATE.value          : State.ERROR.value              , 
        State.LOSE_STATE.value         : State.ERROR.value              , 
        State.ERROR.value              : State.ERROR.value              , 
        State.QUIT_STATE.value         : State.QUIT_STATE.value         ,
    },
    
    Action.NEW_PLAYER.value: { 
        State.START_STATE.value        : State.ERROR.value           , 
        State.INPUT_NAME_STATE.value   : State.ERROR.value           , 
        State.CREATE_PLAYER_STATE.value: State.ERROR.value           , 
        State.LOAD_PLAYER_STATE.value  : State.ERROR.value           , 
        State.MENU.value               : State.INPUT_NAME_STATE.value, 
        State.PLAY_GAME_STATE.value    : State.ERROR.value           , 
        State.GUESS_STATE.value        : State.ERROR.value           , 
        State.WIN_STATE.value          : State.ERROR.value           , 
        State.LOSE_STATE.value         : State.ERROR.value           , 
        State.ERROR.value              : State.ERROR.value           , 
        State.QUIT_STATE.value         : State.QUIT_STATE.value      ,
    },

    Action.WIN.value: { 
        State.START_STATE.value        : State.ERROR.value     , 
        State.INPUT_NAME_STATE.value   : State.ERROR.value     , 
        State.CREATE_PLAYER_STATE.value: State.ERROR.value     , 
        State.LOAD_PLAYER_STATE.value  : State.ERROR.value     , 
        State.MENU.value               : State.ERROR.value     , 
        State.PLAY_GAME_STATE.value    : State.ERROR.value     , 
        State.GUESS_STATE.value        : State.WIN_STATE.value , 
        State.WIN_STATE.value          : State.ERROR.value     , 
        State.LOSE_STATE.value         : State.ERROR.value     , 
        State.ERROR.value              : State.ERROR.value     , 
        State.QUIT_STATE.value         : State.QUIT_STATE.value,
    },
        
    Action.LOSE.value: { 
        State.START_STATE.value        : State.ERROR.value     , 
        State.INPUT_NAME_STATE.value   : State.ERROR.value     , 
        State.CREATE_PLAYER_STATE.value: State.ERROR.value     , 
        State.LOAD_PLAYER_STATE.value  : State.ERROR.value     , 
        State.MENU.value               : State.ERROR.value     , 
        State.PLAY_GAME_STATE.value    : State.ERROR.value     , 
        State.GUESS_STATE.value        : State.LOSE_STATE.value, 
        State.WIN_STATE.value          : State.ERROR.value     , 
        State.LOSE_STATE.value         : State.ERROR.value     , 
        State.ERROR.value              : State.ERROR.value     , 
        State.QUIT_STATE.value         : State.QUIT_STATE.value,
    },
        
    Action.GUESS.value: { 
        State.START_STATE.value        : State.ERROR.value      , 
        State.INPUT_NAME_STATE.value   : State.ERROR.value      , 
        State.CREATE_PLAYER_STATE.value: State.ERROR.value      , 
        State.LOAD_PLAYER_STATE.value  : State.ERROR.value      , 
        State.MENU.value               : State.ERROR.value      , 
        State.PLAY_GAME_STATE.value    : State.ERROR.value      , 
        State.GUESS_STATE.value        : State.GUESS_STATE.value, 
        State.WIN_STATE.value          : State.ERROR.value      , 
        State.LOSE_STATE.value         : State.ERROR.value      , 
        State.ERROR.value              : State.ERROR.value      , 
        State.QUIT_STATE.value         : State.QUIT_STATE.value ,
    },

    Action.NO_ACTION.value: { 
        State.START_STATE.value        : State.ERROR.value, 
        State.INPUT_NAME_STATE.value   : State.ERROR.value, 
        State.CREATE_PLAYER_STATE.value: State.ERROR.value, 
        State.LOAD_PLAYER_STATE.value  : State.ERROR.value, 
        State.MENU.value               : State.ERROR.value, 
        State.PLAY_GAME_STATE.value    : State.ERROR.value, 
        State.GUESS_STATE.value        : State.ERROR.value, 
        State.WIN_STATE.value          : State.ERROR.value, 
        State.LOSE_STATE.value         : State.ERROR.value, 
        State.ERROR.value              : State.ERROR.value, 
        State.QUIT_STATE.value         : State.ERROR.value,
    },
}
