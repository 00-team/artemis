import { CollectionTypes } from '../models/Collection'
import { Action } from '../action-types/collection'

import { XwnerState, OwnerState, FaqState } from '../models/Collection'

const Xwners = (state: XwnerState, action: Action): XwnerState => {
    switch (action.type) {
        case CollectionTypes.SET_XWNERS:
            return action.payload

        default:
            return state
    }
}

const Owner = (state: OwnerState, action: Action): OwnerState => {
    switch (action.type) {
        case CollectionTypes.SET_OWNER:
            return action.payload

        default:
            return state
    }
}

const Faqs = (state: FaqState, action: Action): FaqState => {
    switch (action.type) {
        case CollectionTypes.SET_FAQS:
            return action.payload

        default:
            return state
    }
}

export { Xwners, Owner, Faqs }
