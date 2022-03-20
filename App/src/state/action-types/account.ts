import { AccountTypes, State } from '../models/Account'

interface SET_ACCOUNT {
    type: AccountTypes.SET_ACCOUNT
    payload: State
}
interface SET_WALLET {
    type: AccountTypes.SET_WALLET
    payload: string | null
}

export type Action = SET_ACCOUNT | SET_WALLET
