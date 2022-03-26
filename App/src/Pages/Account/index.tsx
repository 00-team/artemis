import React, { FC, useEffect } from 'react'

// style
import './style/account.scss'

// icons
import { FaWallet } from '@react-icons/all-files/fa/FaWallet'
import { CgSignal } from '@react-icons/all-files/cg/CgSignal'
import { FaIdBadge } from '@react-icons/all-files/fa/FaIdBadge'
import { FaTwitter } from '@react-icons/all-files/fa/FaTwitter'

import { RiLogoutBoxLine } from '@react-icons/all-files/ri/RiLogoutBoxLine'

// redux
import { useSelector, useDispatch } from 'react-redux'
import { GetAccount, RootState } from 'state'
import { AccountModel, TwitterModel } from 'state/models/Account'
import { Avatar } from '@00-team/utils'

const Account: FC = () => {
    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(GetAccount())
    }, [dispatch])

    const AccountState = useSelector((s: RootState) => s.Account)

    if (!AccountState) return <></>

    return (
        <div className='account-container'>
            <div className='account-wrapper'>
                <AccountSideBar {...AccountState} />
                <AccountContent {...AccountState} />
            </div>
        </div>
    )
}

export default Account

const AccountSideBar: FC<AccountModel> = props => {
    const { picture, first_name } = props

    return (
        <div className='sidebar-container'>
            <div className='sidebar-wrapper'>
                <div className='sidebar-top'>
                    <span className='animation'>
                        <div
                            className='account-profile transform'
                            style={{ animationDelay: '0.5s' }}
                        >
                            <Avatar picture={picture} username={first_name} />
                        </div>
                    </span>
                    <span className='animation'>
                        <div
                            className='account-name title_small transform'
                            style={{ animationDelay: '1s' }}
                        >
                            username test
                        </div>
                    </span>
                </div>
            </div>
            <div className='sidebar-logout'></div>
        </div>
    )
}

const AccountContent: FC<AccountModel> = props => {
    // debug
    let walletstring = Math.random().toString(36).slice(2)
    walletstring += walletstring

    const { twitter } = props
    // debug end

    return (
        <div className='content-container '>
            <span
                className='column-container animation boxShadow'
                style={{ animationDelay: '2s' }}
            >
                <div
                    className='column wallet-container transform '
                    style={{ animationDelay: '1.5s' }}
                >
                    <div className='column-title title_small'>
                        <div className='icon wallet'>
                            <FaWallet size={24} />
                        </div>
                        <div className='holder'>
                            <div>Wallet</div>
                        </div>
                    </div>
                    <div className='wallet-wrapper '>
                        <div className='wrapper-column'>
                            <div className='column-holder title_small'>
                                <div className='icon'>
                                    <CgSignal size={24} />
                                </div>
                                <div className='holder'>wallet status:</div>
                            </div>
                            <div className='column-data linked description'>
                                linked
                            </div>
                        </div>
                        <div className='wrapper-column'>
                            <div className='column-holder title_small'>
                                <div className='icon'>
                                    <FaIdBadge size={24} />
                                </div>
                                <div className='holder'>wallet id:</div>
                            </div>
                            <div
                                className='column-data wallet_id description'
                                tabIndex={1}
                            >
                                {walletstring}
                            </div>
                        </div>
                    </div>
                    <div className='disconnect-column title_small'>
                        <div className='icon'>
                            <RiLogoutBoxLine size={24} />
                        </div>
                        <div className='holder'>disconenct wallet</div>
                    </div>
                </div>
            </span>
            {twitter && <TwitterCard {...twitter} />}
        </div>
    )
}

const TwitterCard: FC<TwitterModel> = props => {
    const { followers, followings, tweets, picture } = props
    const { nickname, username, description } = props

    return (
        <span
            className='column-container twitter animation boxShadow'
            style={{ animationDelay: '2.5s' }}
        >
            <div
                className='column twitter-container transform '
                style={{ animationDelay: '2s' }}
            >
                <div className='column-title title_small'>
                    <div className='icon twitter'>
                        <FaTwitter size={24} />
                    </div>
                    <div className='holder'>
                        <div>Twitter</div>
                    </div>
                </div>
                <div className='twitter-wrapper'>
                    <div className='twitter-profile'>
                        <div className='profile-img'>
                            <Avatar picture={picture} username={username} />
                        </div>
                        <div className='profile-name title_smaller'>
                            <div className='profile-name-wrapper'>
                                <div className='profile-name-nickname'>
                                    {nickname}
                                </div>
                                <div className='profile-name-username'>
                                    @{username}
                                </div>
                            </div>
                        </div>
                        <div className='profile-description description'>
                            {description}
                        </div>
                    </div>
                    <div className='twitter-status'>
                        <div className='status'>
                            <div className='holder'>Following</div>
                            <div className='data'>{170 || followings}</div>
                        </div>
                        <div className='status'>
                            <div className='holder'>Followers</div>
                            <div className='data'>{154 || followers}</div>
                        </div>
                        <div className='status'>
                            <div className='holder'>Tweets</div>
                            <div className='data'>{10 || tweets}</div>
                        </div>
                    </div>
                </div>
                <div className='disconnect-column title_small'>
                    <div className='icon'>
                        <RiLogoutBoxLine size={24} />
                    </div>
                    <div className='holder'>disconenct twitter</div>
                </div>
            </div>
        </span>
    )
}
