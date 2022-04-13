import React, { FC, useEffect, useState } from 'react'

// style
import './style/account.scss'

// utils
import Loading from 'components/utils/Loading'
import Success from 'components/utils/Success'
import Error from 'components/utils/Error'

// icons
import { FaWallet } from '@react-icons/all-files/fa/FaWallet'
import { CgSignal } from '@react-icons/all-files/cg/CgSignal'
import { FaIdBadge } from '@react-icons/all-files/fa/FaIdBadge'
import { FaTwitter } from '@react-icons/all-files/fa/FaTwitter'
import { AiOutlineEdit } from '@react-icons/all-files/ai/AiOutlineEdit'

import { RiLogoutBoxLine } from '@react-icons/all-files/ri/RiLogoutBoxLine'
import { FiLogIn } from '@react-icons/all-files/fi/FiLogIn'

import { IoClose } from '@react-icons/all-files/io5/IoClose'
import { BiLogOut } from '@react-icons/all-files/bi/BiLogOut'

// btn icons
import { HiOutlineArrowNarrowRight } from '@react-icons/all-files/hi/HiOutlineArrowNarrowRight'

// redux
import { useSelector, useDispatch } from 'react-redux'
import { DisconnectTwitter, GetAccount, RootState, UpdateAccount } from 'state'
import { AccountModel, TwitterModel } from 'state/models/Account'

// utils
import { Avatar } from '@00-team/utils'

// components
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
    const { picture, first_name, username } = props

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
                            {username || first_name}
                        </div>
                    </span>
                </div>
            </div>
            <div className='sidebar-logout title_small'>
                <a className='logout-wrapper' href='/api/account/logout/'>
                    <div className='icon'>
                        <BiLogOut size={24} />
                    </div>
                    <div className='holder'>Log Out</div>
                </a>
            </div>
        </div>
    )
}

const TWITTER_DEFAULT: TwitterModel = {
    description: '',
    followers: 0,
    followings: 0,
    tweets: 0,
    nickname: 'unknown',
    picture: '/s/img/no-photo.png',
    user_id: '0000000000',
    username: 'unknown',
}

const AccountContent: FC<AccountModel> = props => {
    const dispatch = useDispatch()
    const { twitter } = props
    const { wallet } = props

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
                                <div
                                    className='column-data wallet-status title_small'
                                    style={{
                                        color: wallet ? '#00dc7d' : '#e20338',
                                    }}
                                >
                                    {wallet ? 'linked' : 'disconnected'}
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
                                    {wallet ? wallet : '-- Empty --'}
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
                            <div
                                className='disconnect-column bottom-column title_small'
                                onClick={() =>
                                    wallet && dispatch(UpdateAccount(''))
                                }
                            >
                                <div className='icon'>
                                    <RiLogoutBoxLine size={24} />
                                </div>
                                <div className='holder'>disconenct wallet</div>
                            </div>
                        </div>
                    </div>
                </span>

                {twitter ? (
                    <TwitterCard twitter={twitter} status={true} />
                ) : (
                    <TwitterCard twitter={TWITTER_DEFAULT} status={false} />
                )}
            </div>
            {ShowChangeWallet && (
                <ChangeWallet setShowChangeWallet={setShowChangeWallet} />
            )}
        </div>
    )
}

interface TwitterCardProps {
    twitter: TwitterModel
    status: boolean
}

const TwitterCard: FC<TwitterCardProps> = ({ twitter, status }) => {
    const dispatch = useDispatch()
    const { followers, followings, tweets, picture } = twitter
    const { nickname, username, description } = twitter

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
                                <CountUpAnim end={followings} speed={50} />
                            </div>
                        </div>
                        <div className='status'>
                            <div className='holder'>Followers</div>
                            <div className='data'>
                                <CountUpAnim end={followers} speed={50} />
                            </div>
                        </div>
                        <div className='status'>
                            <div className='holder'>Tweets</div>
                            <div className='data'>
                                <CountUpAnim end={tweets} speed={50} />
                            </div>
                        </div>
                    </div>
                    {!status && (
                        <div className='connect-twitter title_small'>
                            <div className='connect-wrapper'>
                                <div className='icon'>
                                    <FiLogIn size={24} />
                                </div>
                                <a
                                    className='holder'
                                    href='/api/account/twitter_auth/'
                                >
                                    connect twitter
                                </a>
                            </div>
                        </div>
                    )}
                </div>
                <div className='bottom-columns'>
                    {status && (
                        <div
                            className='disconnect-column bottom-column title_small'
                            onClick={() => dispatch(DisconnectTwitter())}
                        >
                            <div className='icon'>
                                <RiLogoutBoxLine size={24} />
                            </div>
                            <div className='holder'>disconenct twitter</div>
                        </div>
                    )}
                </div>
            </div>
        </span>
    )
}

interface ChangeWalletProps {
    setShowChangeWallet(show: boolean): void
}

const ChangeWallet: FC<ChangeWalletProps> = ({ setShowChangeWallet }) => {
    const dispatch = useDispatch()
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
        if (inp1.value.length < 42 || inp2.value.length < 42) {
            return ReactAlert.error('Please Enter A Valid Wallet ID')
        }

        SendForm(inp1.value)
        return ReactAlert.info('your request has been sent')
    }

    const SendForm = (wallet: string) => {
        setLoadingStatus({
            show: true,
            status: 'loading',
            message: 'Sending Your Request...',
        })
        setTimeout(() => {
            dispatch(UpdateAccount(wallet))
            setLoadingStatus({
                show: true,
                status: 'success',
                message: 'There Was An error changing your wallet',
            })

            // to close change wallet
            setTimeout(() => {
                setShowChangeWallet(false)
            }, 3000)
            //
        }, 3000)
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
                    {LoadingStatus.status === 'loading' && (
                        <Loading message={LoadingStatus.message} />
                    )}
                    {LoadingStatus.status === 'success' && (
                        <Success message={LoadingStatus.message} />
                    )}
                    {LoadingStatus.status === 'error' && (
                        <Error message={LoadingStatus.message} />
                    )}
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
