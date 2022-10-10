import {
    StatePageProps
} from '../utils/interfaces';


/**
 * Function will ask the user to enter their name.
 *  It will then send the name to the server.
 * 
 *  When pressed, the start button will query the server 
 *  for a new game state.
 * 
 * @returns 
 */
export function InputNamePage(props: StatePageProps) {
    return (
        <div>
            <h1>Hangman</h1>
            <p>Guess the word</p>
            <label>
                Enter your username:  
                <input 
                    type="text" 
                    defaultValue='player'
                    onKeyDown={(e) => {
                        if (e.key === 'Enter') {
                            props.api.submitUsername(e.currentTarget.value).then(
                                res => {
                                    console.log("Submitted username: ", res.submitUsername)
                                    props.setState(res.submitUsername);
                                }
                            );
                        }
                    }}
                />
            </label>
            
        </div>

    );
}
