import { Dispatch } from 'redux'
import { Action } from '../action-types/account'
import { AccountTypes } from '../models/Account'

// axios
import axios from 'axios'

// cookies
import { get as GetCookies } from 'js-cookie'

const BASE_URL = '/api/account/'

const HandleError = (error: unknown) => {
    if (
        axios.isAxiosError(error) &&
        error.response &&
        error.response.data.error
    ) {
        ReactAlert.error(error.response.data.error)
    }
}
type D = (d: Dispatch<Action>) => Promise<void>
type GA = () => D
const GetAccount: GA = () => async dispatch => {
    try {
        const { data } = await axios.get(BASE_URL + 'get/')

        dispatch({ type: AccountTypes.SET_ACCOUNT, payload: data })
    } catch (error) {
        HandleError(error)
    }
}

type UA = (wallet: string) => D
const UpdateAccount: UA = wallet => async dispatch => {
    try {
        const csrftoken = GetCookies('csrftoken')
        if (!csrftoken) {
            location.reload()
            return
        }

        const config = {
            headers: { 'X-CSRFToken': csrftoken },
        }

        const UpdateData = {
            wallet: wallet,
        }

        const { data } = await axios.post(
            BASE_URL + 'update/',
            UpdateData,
            config
        )

        if (data.ok) ReactAlert.success(data.ok)

        dispatch({ type: AccountTypes.SET_WALLET, payload: data.wallet })
    } catch (error) {
        HandleError(error)
    }
}
export { GetAccount, UpdateAccount }

type DT = () => (d: Dispatch<any>) => Promise<void>
const DisconnectTwitter: DT = () => async dispatch => {
    try {
        const { data } = await axios.get(BASE_URL + 'disconnect_twitter/')

        dispatch(GetAccount())

        if (data.ok) ReactAlert.success(data.ok)
    } catch (error) {
        HandleError(error)
    }
}
export { DisconnectTwitter }

type UGT = () => (d: Dispatch<Action>) => Promise<void>
const UpdateGeneralInfo: UGT = () => async dispatch => {
    try {
        const { data } = await axios.get(BASE_URL + 'general_info/')

        dispatch({ type: AccountTypes.SET_GENERAL_INFO, payload: data })
    } catch (error) {
        HandleError(error)
    }
}
export { UpdateGeneralInfo }
