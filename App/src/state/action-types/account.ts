import { AccountTypes, State } from '../models/Account'
import { GeneralInfoModel } from '../models/Account'

interface SET_ACCOUNT {
    type: AccountTypes.SET_ACCOUNT
    payload: State
}

interface SET_WALLET {
    type: AccountTypes.SET_WALLET
    payload: string | null
}

interface SET_GENERAL_INFO {
    type: AccountTypes.SET_GENERAL_INFO
    payload: GeneralInfoModel
}

export type Action = SET_ACCOUNT | SET_WALLET | SET_GENERAL_INFO
