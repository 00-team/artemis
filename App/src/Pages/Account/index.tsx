import React, { FC, useEffect } from 'react'

// redux
import { useSelector, useDispatch } from 'react-redux'
import { GetAccount, RootState, UpdateAccount } from '../../redux'

// debug only
// getting a string with 42 char length
const getW = () =>
    Array.from(Array(42).keys())
        .map(() => Math.floor(Math.random() * 10))
        .join('')

const Account: FC = () => {
    const dispatch = useDispatch()
    const AccountState = useSelector((s: RootState) => s.Account)

    useEffect(() => {
        dispatch(GetAccount())
    }, [dispatch])

    console.log(AccountState)

    return (
        <div>
            <button onClick={() => dispatch(UpdateAccount(getW()))}>
                UpdateAccount Wallet
            </button>
            <div>{JSON.stringify(AccountState)}</div>
        </div>
    )
}

export default Account
