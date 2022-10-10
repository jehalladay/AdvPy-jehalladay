import {
    StatePageProps
} from '../utils/interfaces';


/**
 * Function will send the shutdown signal to the server once
 *      the user clicks the quit button.
 * 
 * @returns 
 */
export function QuitPage(props: StatePageProps) {

    return (
        <div>
            <h1>Hangman</h1>
            <p>Guess the word</p>

            <button onClick={() => props.api.terminateGame()}>
                Quit Game
            </button>
        </div>

    );
}
