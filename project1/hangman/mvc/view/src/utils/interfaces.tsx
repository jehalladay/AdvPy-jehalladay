import { 
    ReactNode 
} from 'react';

import {
    Client, 
    StateResult
} from '../generated';

import {
    MenuItem
} from './enums';

export interface IApi {
    client: Client;
    getState(): Promise<{getState: StateResult}>;
    startGame(): Promise<{startGame: StateResult}>;
    performDefaultAction(): Promise<{performDefaultAction: StateResult}>;
    submitUsername(name: string): Promise<{submitUsername: StateResult}>;
    menuSelection(selection: MenuItem): Promise<{menuSelection: StateResult}>;
    submitDifficulty(difficulty: number): Promise<{submitDifficulty: StateResult}>;
    terminateGame(): Promise<{terminate: StateResult}>;
    submitGuess(guess: string): Promise<{submitGuess: StateResult}>;
}

export interface PlayerStats {
    name: string;
    wins: number;
    losses: number;
    word: string;
    guessedWord: string;
};

export interface ControllerProps {
    api: IApi;
    state: StateResult;
    setState: (state: StateResult) => void;
    children: ReactNode;
};

export interface State extends PlayerStats {
    state: string;
};

export interface IStatePage {

};

export interface StatePageProps {
    setState: (state: StateResult) => void;
    state: StateResult;
    api: IApi;
    chiildren?: ReactNode
}