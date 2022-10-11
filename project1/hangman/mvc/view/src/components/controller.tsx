import {
    ControllerProps
} from '../utils/interfaces';

import {
    GuessPage
} from './guess';

import {
    InputNamePage
} from './input_name';

import {
    LosePage
} from './lose';

import {
    MenuPage
} from './menu';

import {
    PreGamePage
} from './pre_game';

import {
    QuitPage
} from './quit';

import {
    StartPage
} from './start'

import {
    States
} from '../utils/enums';

import {
    WinPage
} from './win';


export function Controller(props: ControllerProps) {

    let child = null;

    const state = props.state;
    // const setState = props.setState;
    const api = props.api;

    console.log(state);


    switch (state.state) {
        case States.START_STATE:
            child = <StartPage api={api} state={state} setState={props.setState} />;
            break;
        case States.INPUT_NAME_STATE:
            child = <InputNamePage api={api} state={state} setState={props.setState} />;
            break;
        case States.CREATE_PLAYER_STATE:
            child = <div>State {States.CREATE_PLAYER_STATE} has no corresponding view</div>;
            break;
            case States.LOAD_PLAYER_STATE:
            child = <div>State {States.LOAD_PLAYER_STATE} has no corresponding view</div>;
            break;
        case States.MENU:
            child = <MenuPage api={api} state={state} setState={props.setState} />;
            break;
        case States.PLAY_GAME_STATE:
            child = <PreGamePage api={api} state={state} setState={props.setState} />;
            break;
        case States.GUESS_STATE:
            child = <GuessPage api={api} state={state} setState={props.setState} />;
            break;
        case States.WIN_STATE:
            child = <WinPage api={api} state={state} setState={props.setState} />;
            break;
        case States.LOSE_STATE:
            child = <LosePage api={api} state={state} setState={props.setState} />;
            break;
        case States.ERROR:
            child = <div>error</div>;
            break;
        case States.QUIT_STATE:
            child = <QuitPage api={api} state={state} setState={props.setState} />;
            break;
        default:
            child = <div>default</div>;
            break;
    }
        
    return (
        <div>
            {child}
        </div>
    );
}