import React, { FC, useEffect } from 'react'

// style
import './style/account.scss'

// redux
import { useSelector, useDispatch } from 'react-redux'
import {
    GetAccount,
    RootState,
    // UpdateAccount
} from 'state'

// debug only
// getting a string with 42 char length
// const getW = () =>
//     Array.from(Array(42).keys())
//         .map(() => Math.floor(Math.random() * 10))
//         .join('')

const Account: FC = () => {
    const dispatch = useDispatch()
    const AccountState = useSelector((s: RootState) => s.Account)
    console.log(AccountState)

    useEffect(() => {
        dispatch(GetAccount())
    }, [dispatch])

    return (
        <div className='account-container'>
            <div className='account-wrapper'>
                <AccountContent />
                <AccountSideBar />
            </div>
            {/* <button onClick={() => dispatch(UpdateAccount(getW()))}>
                UpdateAccount Wallet
            </button>
            <div>{JSON.stringify(AccountState)}</div> */}
        </div>
    )
}

export default Account

const AccountSideBar: FC = () => {
    return (
        <div className='sidebar-container'>
            <div className='sidebar-wrapper'>
                <div className='sidebar-top'>
                    <div className='account-profile'></div>
                    <div className='account-name'>username test</div>
                </div>
            </div>
            <div className='sidebar-logout'></div>
        </div>
    )
}

const AccountContent: FC = () => {
    return <div className='contant-container'></div>
}
