import { combineReducers } from 'redux'

import winScrollTop from './winScrollTop'

// Account
import { Account } from './account'

// Collection
import { Xwners, Owner, FAQs } from './collection'

const reducers = combineReducers({
    Account,
    winScrollTop,
    Xwners,
    Owner,
    FAQs,
})

export type RootState = ReturnType<typeof reducers>

export default reducers
