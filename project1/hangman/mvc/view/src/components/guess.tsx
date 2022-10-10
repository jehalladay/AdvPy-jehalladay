
import Keyboard from 'react-simple-keyboard';

import 'react-simple-keyboard/build/css/index.css';

import {
    StatePageProps
} from '../utils/interfaces';

import {
    HANGMAN_PICS
} from '../utils/constants';

/**
 * Function will create a page that will allow users to input
 *  their guess. A QWERTY keyboard will be displayed and each
 *  key will send back the guess to the server.
 * 
 * Will also display the current guessed word and the number of
 *  missed guesses using the state.missed value to choose which 
 *  hangman picture to display.
 * 
 */
export function GuessPage(props: StatePageProps) {


    function onKeyPress(button: string) {
        props.api.submitGuess(button).then(
            res => {
                console.log("Guess Letter Results: ", res.submitGuess)
                props.setState(res.submitGuess);
            }
        ).catch(console.error);
    }

    return (
        <div>
            <h1>Hangman</h1>
            <p>Guess the word</p>

            <p>Username: {props.state.name}</p>

            <p>{"Word:\t"} {props.state.guessedWord}</p>

            <img src={HANGMAN_PICS[props.state.missed]} alt="hangman" />

            <Keyboard layout = {{
                'default': [
                    'q w e r t y u i o p',
                    'a s d f g h j k l',
                    'z x c v b n m',
                    // '{space}'
                ]
            }} onKeyPress={onKeyPress} />
            
            <p>Wins: {props.state.wins}</p>
            <p>Losses: {props.state.losses}</p>
            <p>Missed Guesses: {props.state.missed}</p>
        </div>

    );
}
