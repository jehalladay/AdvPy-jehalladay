import {FieldsSelection,Observable} from '@genql/runtime'

export type Scalars = {
    Boolean: boolean,
    String: string,
    Int: number,
}

export interface StateResult {
    success: Scalars['Boolean']
    state: Scalars['String']
    name?: Scalars['String']
    word?: Scalars['String']
    guessedWord?: Scalars['String']
    wins?: Scalars['Int']
    losses?: Scalars['Int']
    missed: Scalars['Int']
    time?: Scalars['String']
    method?: Scalars['String']
    input?: Scalars['String']
    message?: (Scalars['String'] | undefined)[]
    errors?: (Scalars['String'] | undefined)[]
    __typename: 'StateResult'
}

export interface Query {
    getState: StateResult
    __typename: 'Query'
}

export interface Mutation {
    performAction: StateResult
    performDefaultAction: StateResult
    startGame: StateResult
    submitUsername: StateResult
    menuSelection: StateResult
    submitDifficulty: StateResult
    terminate: StateResult
    submitGuess: StateResult
    __typename: 'Mutation'
}

export interface StateResultRequest{
    success?: boolean | number
    state?: boolean | number
    name?: boolean | number
    word?: boolean | number
    guessedWord?: boolean | number
    wins?: boolean | number
    losses?: boolean | number
    missed?: boolean | number
    time?: boolean | number
    method?: boolean | number
    input?: boolean | number
    message?: boolean | number
    errors?: boolean | number
    __typename?: boolean | number
    __scalar?: boolean | number
}

export interface QueryRequest{
    getState?: StateResultRequest
    __typename?: boolean | number
    __scalar?: boolean | number
}

export interface MutationRequest{
    performAction?: [{action: Scalars['String']},StateResultRequest]
    performDefaultAction?: StateResultRequest
    startGame?: StateResultRequest
    submitUsername?: [{username: Scalars['String']},StateResultRequest]
    menuSelection?: [{selection: Scalars['String']},StateResultRequest]
    submitDifficulty?: [{difficulty: Scalars['Int']},StateResultRequest]
    terminate?: StateResultRequest
    submitGuess?: [{guess: Scalars['String']},StateResultRequest]
    __typename?: boolean | number
    __scalar?: boolean | number
}


const StateResult_possibleTypes: string[] = ['StateResult']
export const isStateResult = (obj?: { __typename?: any } | null): obj is StateResult => {
  if (!obj?.__typename) throw new Error('__typename is missing in "isStateResult"')
  return StateResult_possibleTypes.includes(obj.__typename)
}



const Query_possibleTypes: string[] = ['Query']
export const isQuery = (obj?: { __typename?: any } | null): obj is Query => {
  if (!obj?.__typename) throw new Error('__typename is missing in "isQuery"')
  return Query_possibleTypes.includes(obj.__typename)
}



const Mutation_possibleTypes: string[] = ['Mutation']
export const isMutation = (obj?: { __typename?: any } | null): obj is Mutation => {
  if (!obj?.__typename) throw new Error('__typename is missing in "isMutation"')
  return Mutation_possibleTypes.includes(obj.__typename)
}


export interface StateResultPromiseChain{
    success: ({get: (request?: boolean|number, defaultValue?: Scalars['Boolean']) => Promise<Scalars['Boolean']>}),
    state: ({get: (request?: boolean|number, defaultValue?: Scalars['String']) => Promise<Scalars['String']>}),
    name: ({get: (request?: boolean|number, defaultValue?: (Scalars['String'] | undefined)) => Promise<(Scalars['String'] | undefined)>}),
    word: ({get: (request?: boolean|number, defaultValue?: (Scalars['String'] | undefined)) => Promise<(Scalars['String'] | undefined)>}),
    guessedWord: ({get: (request?: boolean|number, defaultValue?: (Scalars['String'] | undefined)) => Promise<(Scalars['String'] | undefined)>}),
    wins: ({get: (request?: boolean|number, defaultValue?: (Scalars['Int'] | undefined)) => Promise<(Scalars['Int'] | undefined)>}),
    losses: ({get: (request?: boolean|number, defaultValue?: (Scalars['Int'] | undefined)) => Promise<(Scalars['Int'] | undefined)>}),
    missed: ({get: (request?: boolean|number, defaultValue?: Scalars['Int']) => Promise<Scalars['Int']>}),
    time: ({get: (request?: boolean|number, defaultValue?: (Scalars['String'] | undefined)) => Promise<(Scalars['String'] | undefined)>}),
    method: ({get: (request?: boolean|number, defaultValue?: (Scalars['String'] | undefined)) => Promise<(Scalars['String'] | undefined)>}),
    input: ({get: (request?: boolean|number, defaultValue?: (Scalars['String'] | undefined)) => Promise<(Scalars['String'] | undefined)>}),
    message: ({get: (request?: boolean|number, defaultValue?: ((Scalars['String'] | undefined)[] | undefined)) => Promise<((Scalars['String'] | undefined)[] | undefined)>}),
    errors: ({get: (request?: boolean|number, defaultValue?: ((Scalars['String'] | undefined)[] | undefined)) => Promise<((Scalars['String'] | undefined)[] | undefined)>})
}

export interface StateResultObservableChain{
    success: ({get: (request?: boolean|number, defaultValue?: Scalars['Boolean']) => Observable<Scalars['Boolean']>}),
    state: ({get: (request?: boolean|number, defaultValue?: Scalars['String']) => Observable<Scalars['String']>}),
    name: ({get: (request?: boolean|number, defaultValue?: (Scalars['String'] | undefined)) => Observable<(Scalars['String'] | undefined)>}),
    word: ({get: (request?: boolean|number, defaultValue?: (Scalars['String'] | undefined)) => Observable<(Scalars['String'] | undefined)>}),
    guessedWord: ({get: (request?: boolean|number, defaultValue?: (Scalars['String'] | undefined)) => Observable<(Scalars['String'] | undefined)>}),
    wins: ({get: (request?: boolean|number, defaultValue?: (Scalars['Int'] | undefined)) => Observable<(Scalars['Int'] | undefined)>}),
    losses: ({get: (request?: boolean|number, defaultValue?: (Scalars['Int'] | undefined)) => Observable<(Scalars['Int'] | undefined)>}),
    missed: ({get: (request?: boolean|number, defaultValue?: Scalars['Int']) => Observable<Scalars['Int']>}),
    time: ({get: (request?: boolean|number, defaultValue?: (Scalars['String'] | undefined)) => Observable<(Scalars['String'] | undefined)>}),
    method: ({get: (request?: boolean|number, defaultValue?: (Scalars['String'] | undefined)) => Observable<(Scalars['String'] | undefined)>}),
    input: ({get: (request?: boolean|number, defaultValue?: (Scalars['String'] | undefined)) => Observable<(Scalars['String'] | undefined)>}),
    message: ({get: (request?: boolean|number, defaultValue?: ((Scalars['String'] | undefined)[] | undefined)) => Observable<((Scalars['String'] | undefined)[] | undefined)>}),
    errors: ({get: (request?: boolean|number, defaultValue?: ((Scalars['String'] | undefined)[] | undefined)) => Observable<((Scalars['String'] | undefined)[] | undefined)>})
}

export interface QueryPromiseChain{
    getState: (StateResultPromiseChain & {get: <R extends StateResultRequest>(request: R, defaultValue?: FieldsSelection<StateResult, R>) => Promise<FieldsSelection<StateResult, R>>})
}

export interface QueryObservableChain{
    getState: (StateResultObservableChain & {get: <R extends StateResultRequest>(request: R, defaultValue?: FieldsSelection<StateResult, R>) => Observable<FieldsSelection<StateResult, R>>})
}

export interface MutationPromiseChain{
    performAction: ((args: {action: Scalars['String']}) => StateResultPromiseChain & {get: <R extends StateResultRequest>(request: R, defaultValue?: FieldsSelection<StateResult, R>) => Promise<FieldsSelection<StateResult, R>>}),
    performDefaultAction: (StateResultPromiseChain & {get: <R extends StateResultRequest>(request: R, defaultValue?: FieldsSelection<StateResult, R>) => Promise<FieldsSelection<StateResult, R>>}),
    startGame: (StateResultPromiseChain & {get: <R extends StateResultRequest>(request: R, defaultValue?: FieldsSelection<StateResult, R>) => Promise<FieldsSelection<StateResult, R>>}),
    submitUsername: ((args: {username: Scalars['String']}) => StateResultPromiseChain & {get: <R extends StateResultRequest>(request: R, defaultValue?: FieldsSelection<StateResult, R>) => Promise<FieldsSelection<StateResult, R>>}),
    menuSelection: ((args: {selection: Scalars['String']}) => StateResultPromiseChain & {get: <R extends StateResultRequest>(request: R, defaultValue?: FieldsSelection<StateResult, R>) => Promise<FieldsSelection<StateResult, R>>}),
    submitDifficulty: ((args: {difficulty: Scalars['Int']}) => StateResultPromiseChain & {get: <R extends StateResultRequest>(request: R, defaultValue?: FieldsSelection<StateResult, R>) => Promise<FieldsSelection<StateResult, R>>}),
    terminate: (StateResultPromiseChain & {get: <R extends StateResultRequest>(request: R, defaultValue?: FieldsSelection<StateResult, R>) => Promise<FieldsSelection<StateResult, R>>}),
    submitGuess: ((args: {guess: Scalars['String']}) => StateResultPromiseChain & {get: <R extends StateResultRequest>(request: R, defaultValue?: FieldsSelection<StateResult, R>) => Promise<FieldsSelection<StateResult, R>>})
}

export interface MutationObservableChain{
    performAction: ((args: {action: Scalars['String']}) => StateResultObservableChain & {get: <R extends StateResultRequest>(request: R, defaultValue?: FieldsSelection<StateResult, R>) => Observable<FieldsSelection<StateResult, R>>}),
    performDefaultAction: (StateResultObservableChain & {get: <R extends StateResultRequest>(request: R, defaultValue?: FieldsSelection<StateResult, R>) => Observable<FieldsSelection<StateResult, R>>}),
    startGame: (StateResultObservableChain & {get: <R extends StateResultRequest>(request: R, defaultValue?: FieldsSelection<StateResult, R>) => Observable<FieldsSelection<StateResult, R>>}),
    submitUsername: ((args: {username: Scalars['String']}) => StateResultObservableChain & {get: <R extends StateResultRequest>(request: R, defaultValue?: FieldsSelection<StateResult, R>) => Observable<FieldsSelection<StateResult, R>>}),
    menuSelection: ((args: {selection: Scalars['String']}) => StateResultObservableChain & {get: <R extends StateResultRequest>(request: R, defaultValue?: FieldsSelection<StateResult, R>) => Observable<FieldsSelection<StateResult, R>>}),
    submitDifficulty: ((args: {difficulty: Scalars['Int']}) => StateResultObservableChain & {get: <R extends StateResultRequest>(request: R, defaultValue?: FieldsSelection<StateResult, R>) => Observable<FieldsSelection<StateResult, R>>}),
    terminate: (StateResultObservableChain & {get: <R extends StateResultRequest>(request: R, defaultValue?: FieldsSelection<StateResult, R>) => Observable<FieldsSelection<StateResult, R>>}),
    submitGuess: ((args: {guess: Scalars['String']}) => StateResultObservableChain & {get: <R extends StateResultRequest>(request: R, defaultValue?: FieldsSelection<StateResult, R>) => Observable<FieldsSelection<StateResult, R>>})
}