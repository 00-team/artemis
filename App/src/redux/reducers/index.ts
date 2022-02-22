import { combineReducers } from 'redux'

// Account
import { Account } from './account'

const reducers = combineReducers({
    Account,
})

export type RootState = ReturnType<typeof reducers>

export default reducers
