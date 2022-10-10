/**
 * Function will use graphQL to query the server for 
 *  the current game state.
 */
export function queryForState() {
    fetch(
        `/graphql`, 
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
            query: `query testGetState {
                        getState {
                        success
                        errors
                        state
                        method
                        time
                        }
                    }
                `,
            }),
        }
    )
    .then(res => res.json())
    .then(res => console.log(res.data))
    .catch(console.error)
}