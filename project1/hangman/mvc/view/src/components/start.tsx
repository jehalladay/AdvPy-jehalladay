import React from 'react';

import {
    StatePageProps
} from '../utils/interfaces';

/**
 * Function will show the title of the game: Hangman
 *  Then, it will show a start button.
 * 
 *  When pressed, the start button will query the server 
 *  for a new game state.
 * 
 * @returns 
 */
export function StartPage(props: StatePageProps) {

    function startGame() {
        props.api.performDefaultAction()
            .then(res => {
                console.log('StartPage: ', res);
                props.setState(res.performDefaultAction);
            }
        ).catch(console.error);
    }

    return (
        <div>
            <h1>Hangman</h1>
            <p>Guess the word</p>
            <button onClick={() => startGame()}>
                Start Game
            </button>
        </div>
  );
}