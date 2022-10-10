module.exports = {
    "scalars": [
        1,
        2,
        3
    ],
    "types": {
        "StateResult": {
            "success": [
                1
            ],
            "state": [
                2
            ],
            "name": [
                2
            ],
            "word": [
                2
            ],
            "guessedWord": [
                2
            ],
            "wins": [
                3
            ],
            "losses": [
                3
            ],
            "missed": [
                3
            ],
            "time": [
                2
            ],
            "method": [
                2
            ],
            "input": [
                2
            ],
            "message": [
                2
            ],
            "errors": [
                2
            ],
            "__typename": [
                2
            ]
        },
        "Boolean": {},
        "String": {},
        "Int": {},
        "Query": {
            "getState": [
                0
            ],
            "__typename": [
                2
            ]
        },
        "Mutation": {
            "performAction": [
                0,
                {
                    "action": [
                        2,
                        "String!"
                    ]
                }
            ],
            "performDefaultAction": [
                0
            ],
            "startGame": [
                0
            ],
            "submitUsername": [
                0,
                {
                    "username": [
                        2,
                        "String!"
                    ]
                }
            ],
            "menuSelection": [
                0,
                {
                    "selection": [
                        2,
                        "String!"
                    ]
                }
            ],
            "submitDifficulty": [
                0,
                {
                    "difficulty": [
                        3,
                        "Int!"
                    ]
                }
            ],
            "terminate": [
                0
            ],
            "submitGuess": [
                0,
                {
                    "guess": [
                        2,
                        "String!"
                    ]
                }
            ],
            "__typename": [
                2
            ]
        }
    }
}