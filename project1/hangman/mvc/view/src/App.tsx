import React, { Component } from 'react';

import './App.css';

import {
    Api
} from './api';

import { 
    Controller 
} from './components/controller';

import {
     StateResult 
} from './generated';


export default class App extends Component {

    private api: Api;
    public state: StateResult = {
        success: true,
        state: "",
        word: "",
        guessedWord: "",
        name: "",
        wins: 0,
        losses: 0,
        missed: 0,
        __typename: "StateResult"
    }
    
    constructor(props: any) {
        super(props);
        this.api = new Api();
        this.api.startGame().then(
            (res) => {
                console.log('state', res);
                this.setState(res.startGame);
            }
        );

        this.setState = this.setState.bind(this);
    }

    render() {
        return (
            <div className="App">
                <Controller api={this.api} state={this.state} setState={this.setState}>
                </Controller>
                {/* <header className="App-header">
                </header> */}
            </div>
        );
    }
}
