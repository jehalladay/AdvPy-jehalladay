
import {
    StatePageProps
} from '../utils/interfaces';

import {
    HANGMAN_PICS
} from '../utils/constants';

/**
 * Function will create a page 
 * 
 */
export function WinPage(props: StatePageProps) {


    function backToMenu() {
        props.api.performDefaultAction()
            .then(res => {
                console.log('Win page: ', res.performDefaultAction);
                props.setState(res.performDefaultAction);
            }
        ).catch(console.error);
    }

    // we will center the picture
    return (
        <div>
            <h1>Hangman</h1>
            <p>Guess the word</p>

            <p>Congratulations for Winning!</p>
            <p>Username: {props.state.name}</p>

            <p>{"Word:\t"} {props.state.word}</p>
            <p>{"Guessed Word:\t"} {props.state.guessedWord}</p>

            <img src={HANGMAN_PICS[props.state.missed]} alt={`hangman_${props.state.missed}`}/>
            
            <button onClick={() => backToMenu()} style={{display: 'block', margin: 'auto'}}>
                Back to Menu
            </button>

            <p>Wins: {props.state.wins}</p>
            <p>Losses: {props.state.losses}</p>
        </div>

    );
}
