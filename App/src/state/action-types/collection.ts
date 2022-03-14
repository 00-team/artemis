import { CollectionTypes } from '../models/Collection'
import { XwnerState, OwnerState, FaqState } from '../models/Collection'

interface SET_XWNERS {
    type: CollectionTypes.SET_XWNERS
    payload: XwnerState
}

interface SET_OWNER {
    type: CollectionTypes.SET_OWNER
    payload: OwnerState
}

interface SET_FAQS {
    type: CollectionTypes.SET_FAQS
    payload: FaqState
}

export type Action = SET_XWNERS | SET_OWNER | SET_FAQS
