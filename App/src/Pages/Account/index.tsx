import React, { FC, useEffect } from 'react'

// style
import './style/account.scss'

// icons
import { FaWallet } from '@react-icons/all-files/fa/FaWallet'

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
                    <div className='account-profile '></div>
                    <div className='account-name title_smaller'>
                        username test
                    </div>
                </div>
            </div>
            <div className='sidebar-logout'></div>
        </div>
    )
}

const AccountContent: FC = () => {
    return (
        <div className='content-container'>
            <div className='column wallet-container '>
                <div className='wallet-title title_small'>
                    <div className='icon'>
                        <FaWallet />
                    </div>
                    <div className='holder'>My Wallet</div>
                    <div className='icon'>
                        <FaWallet />
                    </div>
                </div>
            </div>
            <div className='column twitter-container '></div>
        </div>
    )
}
