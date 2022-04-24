type strnull = string | null

interface AccountModel {
    first_name: string
    last_name: strnull
    wallet: strnull
    username: strnull
    picture: strnull
    twitter: TwitterModel | null
}

interface TwitterModel {
    user_id: string
    nickname: string
    username: string
    tweets: number
    followers: number
    followings: number
    description: strnull
    picture: strnull
}

interface GeneralInfoModel {
    bot_users: number
    accounts: number
    twitters: number
}

export { AccountModel, TwitterModel, GeneralInfoModel }

type State = AccountModel | null
const DefaultState: State = null
const DefaultGeneralState: GeneralInfoModel = {
    bot_users: 0,
    accounts: 0,
    twitters: 0,
}

export { State, DefaultState, DefaultGeneralState }

enum AccountTypes {
    SET_ACCOUNT = 'SET_ACCOUNT',
    SET_WALLET = 'SET_WALLET',
    SET_GENERAL_INFO = 'SET_GENERAL_INFO',
}

export { AccountTypes }
