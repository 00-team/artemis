import React, { FC, useEffect, useState } from 'react'

// style
import './style/account.scss'

// utils
import Loading from 'components/utils/Loading'

// icons
import { FaWallet } from '@react-icons/all-files/fa/FaWallet'
import { CgSignal } from '@react-icons/all-files/cg/CgSignal'
import { FaIdBadge } from '@react-icons/all-files/fa/FaIdBadge'
import { FaTwitter } from '@react-icons/all-files/fa/FaTwitter'
import { AiOutlineEdit } from '@react-icons/all-files/ai/AiOutlineEdit'

import { RiLogoutBoxLine } from '@react-icons/all-files/ri/RiLogoutBoxLine'

import { IoClose } from '@react-icons/all-files/io5/IoClose'

// btn icons
import { HiOutlineArrowNarrowRight } from '@react-icons/all-files/hi/HiOutlineArrowNarrowRight'

// redux
import { useSelector, useDispatch } from 'react-redux'
import { GetAccount, RootState } from 'state'
import { AccountModel, TwitterModel } from 'state/models/Account'
import { Avatar } from '@00-team/utils'
import CountUpAnim from 'components/utils/CountUpAnim'

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

    const [ShowChangeWallet, setShowChangeWallet] = useState(false)

    return (
        <div className='content-container '>
            <div className='columns-wrapper'>
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
                                <div className='column-data linked title_small'>
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
                        <div className='bottom-columns'>
                            <div className='edit-column bottom-column title_small'>
                                <div className='icon'>
                                    <AiOutlineEdit size={24} />
                                </div>
                                <div
                                    className='holder'
                                    onClick={() => setShowChangeWallet(true)}
                                >
                                    Edit Wallet
                                </div>
                            </div>
                            <div className='disconnect-column bottom-column title_small'>
                                <div className='icon'>
                                    <RiLogoutBoxLine size={24} />
                                </div>
                                <div className='holder'>disconenct wallet</div>
                            </div>
                        </div>
                    </div>
                </span>
                {twitter && <TwitterCard {...twitter} />}
            </div>
            {ShowChangeWallet && (
                <ChangeWallet setShowChangeWallet={setShowChangeWallet} />
            )}
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
                            <div className='data'>
                                <CountUpAnim
                                    end={170 || followings}
                                    speed={50}
                                />
                            </div>
                        </div>
                        <div className='status'>
                            <div className='holder'>Followers</div>
                            <div className='data'>
                                <CountUpAnim
                                    end={11054 || followers}
                                    speed={50}
                                />
                            </div>
                        </div>
                        <div className='status'>
                            <div className='holder'>Tweets</div>
                            <div className='data'>
                                <CountUpAnim end={11020 || tweets} speed={50} />
                            </div>
                        </div>
                    </div>
                </div>
                <div className='bottom-columns'>
                    <div className='disconnect-column bottom-column title_small'>
                        <div className='icon'>
                            <RiLogoutBoxLine size={24} />
                        </div>
                        <div className='holder'>disconenct twitter</div>
                    </div>
                </div>
            </div>
        </span>
    )
}

interface ChangeWalletProps {
    setShowChangeWallet(show: boolean): void
}

const ChangeWallet: FC<ChangeWalletProps> = ({ setShowChangeWallet }) => {
    const [LoadingStatus, setLoadingStatus] = useState({
        show: false,
        message: '',
        status: '',
    })

    const CheckForm = () => {
        let inp1 = document.getElementById('inp') as HTMLInputElement
        let inp2 = document.getElementById('inp-repeat') as HTMLInputElement

        if (!inp1.value || !inp2.value) {
            return ReactAlert.error('Please Fill All The Fields')
        }
        if (inp1.value !== inp2.value) {
            return ReactAlert.error("Wallet IDs Don't Match")
        }
        if (inp1.value.indexOf(' ') >= 0 || inp2.value.indexOf(' ') >= 0) {
            return ReactAlert.error('Please Enter A Valid Wallet ID')
        }
        if (inp1.value.length < 24 || inp2.value.length < 24) {
            return ReactAlert.error('Please Enter A Valid Wallet ID')
        }

        SendForm()
        return ReactAlert.info('your request has been sent')
    }

    const SendForm = () => {
        setLoadingStatus({
            show: true,
            message: 'Sending Your Request...',
            status: 'loading',
        })
        setTimeout(() => {
            setLoadingStatus({
                show: true,
                message: '',
                status: '',
            })
        }, 10000)
    }

    return (
        <div className='change-wallet-container'>
            <div className='change-wallet-wrapper'>
                <div
                    className='close-btn'
                    onClick={() => setShowChangeWallet(false)}
                >
                    <IoClose />
                </div>
                <div className='change-wallet-title title'>
                    change wallet ID
                </div>
                <div className='change-wallet-inps'>
                    <div className='change-wallet-inp title_smaller'>
                        <label htmlFor='inp'>
                            <div className='icon'>
                                <FaIdBadge size={24} />
                            </div>
                            <div className='holder'>New Wallet ID</div>
                        </label>
                        <input id='inp' type='text' />
                    </div>
                    <div className='change-wallet-inp repeat title_smaller'>
                        <label htmlFor='inp-repeat'>
                            <div className='icon'>
                                <FaIdBadge size={24} />
                            </div>
                            <div className='holder'>Repeat Wallet ID</div>
                        </label>
                        <input id='inp-repeat' type='text' />
                    </div>
                </div>
                <div className='change-btn'>
                    <ButtonWithArrow
                        border
                        classname='title_smaller'
                        onClick={() => CheckForm()}
                    >
                        Change My Wallet
                    </ButtonWithArrow>
                </div>
            </div>
            {LoadingStatus.show && (
                <div className='loading-wrapper'>
                    <div className='loading-container'>
                        {LoadingStatus.status === 'loading' && (
                            <Loading message={LoadingStatus.message} />
                        )}
                    </div>
                </div>
            )}
        </div>
    )
}

interface ButtonProps {
    onClick?: (e: React.MouseEvent) => void
    classname?: string
    backgroundColor?: string
    color?: string
    borderRadius?: number
    border?: boolean
    borderColor?: string
}

const ButtonWithArrow: FC<ButtonProps> = ({
    children,
    onClick,
    classname,
    borderColor,
}) => {
    return (
        <button
            className={`arrow-button basic-button ${
                classname ? classname : ''
            }`}
            onClick={e => (onClick ? onClick(e) : {})}
            style={borderColor ? { borderColor: borderColor } : {}}
        >
            <div className='icon-arrow before'>
                <HiOutlineArrowNarrowRight size={24} />
            </div>
            <div className='label'>{children}</div>
            <div className='icon-arrow after'>
                <HiOutlineArrowNarrowRight size={24} />
            </div>
        </button>
    )
}
