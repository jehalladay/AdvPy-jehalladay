
export enum States {
    START_STATE         = 'start_state',
    INPUT_NAME_STATE    = 'input_name_state',
    CREATE_PLAYER_STATE = 'create_player_state',
    LOAD_PLAYER_STATE   = 'load_player_state',
    MENU                = 'menu_state',
    PLAY_GAME_STATE     = 'play_state',
    GUESS_STATE         = 'guess_state',
    WIN_STATE           = 'win_state',
    LOSE_STATE          = 'lose_state',
    ERROR               = 'error_state',
    QUIT_STATE          = 'quit_state',
};

export enum MenuItem {
    PLAY_GAME = 'play',
    QUIT_GAME = 'quit',
    NEW_PLAYER = 'new',
};
