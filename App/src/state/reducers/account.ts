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

import { DefaultGeneralState as DGS } from '../models/Account'
import { GeneralInfoModel } from '../models/Account'

const GeneralInfo = (state = DGS, action: Action): GeneralInfoModel => {
    switch (action.type) {
        case AccountTypes.SET_GENERAL_INFO:
            return action.payload

        default:
            return state
    }
}

export { Account, GeneralInfo }
