import {
    StatePageProps
} from '../utils/interfaces';


/**
 * Function will ask the user to select a difficulty
 *  The difficulties will range from 1-10 and will
 *      correspond to the length of the word they
 *      will be guessing.
 * 
 * The difficulty will be represented by a slider
 * with a button to submit the difficulty.
 * 
 * @returns 
 */
export function PreGamePage(props: StatePageProps) {

    function submitDifficulty() {
        const slider = document.getElementById("myRange") as HTMLInputElement;
        const range: number = parseInt(slider.value);

        console.log('Selected difficulty: ', slider);
        console.log('Selected difficulty: ', range);

        props.api.submitDifficulty(range)
            .then(res => {
                console.log("Submitted difficulty: ", res.submitDifficulty)
                props.setState(res.submitDifficulty);
            }
        ).catch(console.error);
    }

    return (
        <div>
            <h1>Hangman</h1>
            <p>Guess the word</p>

            <label>
                Select Difficulty:
                <input
                    type="range"
                    min="1"
                    max="10"
                    defaultValue="5"
                    className="slider"
                    id="myRange"
                />
            </label>
            <button onClick={submitDifficulty} >
                Submit Difficulty
            </button>
        </div>

    );
}
