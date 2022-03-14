import axios from 'axios'

// redux
import { Dispatch } from 'redux'
import { CollectionTypes } from 'state/models/Collection'
import { Action } from '../action-types/collection'

const BASE_URL = '/api/collection/'

type D = (d: Dispatch<Action>) => Promise<void>

type GX = () => D
const GetXwners: GX = () => async dispatch => {
    try {
        const { data } = await axios.get(BASE_URL + 'owners/')
        if (data.owners) {
            dispatch({ type: CollectionTypes.SET_XWNERS, payload: data.owners })
        }
    } catch (error) {}
}

type GO = (username: string) => D
const GetOwner: GO = u => async dispatch => {
    try {
        const { data } = await axios.get(BASE_URL + `owner/?username=${u}`)

        if (data.username === u) {
            dispatch({ type: CollectionTypes.SET_OWNER, payload: data })
        }
    } catch (error) {
        location.replace('/')
    }
}

type GF = () => D
const GetFAQs: GF = () => async dispatch => {
    try {
        const { data } = await axios.get(BASE_URL + 'faqs/')

        if (data.owners) {
            dispatch({ type: CollectionTypes.SET_FAQS, payload: data.owners })
        }
    } catch (error) {}
}

export { GetXwners, GetOwner, GetFAQs }
