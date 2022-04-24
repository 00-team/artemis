import { combineReducers } from 'redux'

import winScrollTop from './winScrollTop'

// Account
import { Account, GeneralInfo } from './account'

// Collection
import { Xwners, Owner, FAQs } from './collection'

const reducers = combineReducers({
    GeneralInfo,
    Account,
    winScrollTop,
    Xwners,
    Owner,
    FAQs,
})

export type RootState = ReturnType<typeof reducers>

export default reducers
