import { Action } from '../action-types/account'
import { AccountTypes, DefaultState, State } from '../models/Account'

const Account = (state = DefaultState, action: Action): State => {
    switch (action.type) {
        case AccountTypes.SET_ACCOUNT:
            return action.payload

        case AccountTypes.SET_WALLET:
            if (state)
                return {
                    ...state,
                    wallet: action.payload,
                }

            return state

        default:
            return state
    }
}

export { Account }
