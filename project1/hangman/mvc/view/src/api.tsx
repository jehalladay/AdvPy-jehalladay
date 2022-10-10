import {
    createClient,
    everything,
    Client,
    StateResult
} from './generated';

import {
    IApi
} from './utils/interfaces';

import { 
    MenuItem 
} from './utils/enums';


export class Api implements IApi {

    public client: Client;

    constructor() {
        this.client = createClient({
            url: 'http://127.0.0.1:4999/graphql',
        })
    }
    
    getState() {
        return this.client.query({
            getState: {
                ...everything
            }
        });
    }

    startGame() {
        return this.client.mutation({
            startGame: {
                ...everything
            }
        });
    }

    performDefaultAction() {
        return this.client.mutation({
            performDefaultAction: {
                ...everything
            }
        });
    }

    submitUsername(name: string) {
        return this.client.mutation({
            submitUsername: [
                {
                    username: name
                }, 
                {
                    ...everything
                }
            ]
        });
    }

    menuSelection(selection: MenuItem) {
        return this.client.mutation({
            menuSelection: [
                {
                    selection: selection
                },
                {
                    ...everything
                }
            ]
        });
    }

    submitDifficulty(difficulty: number) {
        return this.client.mutation({
            submitDifficulty: [
                {
                    difficulty: difficulty
                },
                {
                    ...everything
                }
            ]
        });
    }

    terminateGame() {
        return this.client.mutation({
            terminate: {
                ...everything
            }
        });
    }

    submitGuess(guess: string): Promise<{submitGuess: StateResult}> {
        return this.client.mutation({
            submitGuess: [
                {
                    guess: guess
                },
                {
                    ...everything
                }  
            ]
        });
    }
}
  