import { combineReducers } from 'redux'

// Account
import { Account } from './account'
import winScrollTop from './winScrollTop'

const reducers = combineReducers({
    Account,
    winScrollTop,
})

export type RootState = ReturnType<typeof reducers>

export default reducers
