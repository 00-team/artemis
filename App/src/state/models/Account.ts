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

type State = AccountModel | null
const DefaultState: State = null

enum AccountTypes {
    SET_ACCOUNT = 'SET_ACCOUNT',
    SET_WALLET = 'SET_WALLET',
}

export { AccountModel, TwitterModel, State, DefaultState, AccountTypes }
