type strnull = string | null

interface Account {
    first_name: strnull
    last_name: strnull
    wallet: strnull
    username: strnull
    picture: strnull
    twitter: Twitter | null
}

interface Twitter {
    username: string
}

type State = Account | null
const DefaultState: State = null

enum AccountTypes {
    SET_ACCOUNT = 'SET_ACCOUNT',
    SET_WALLET = 'SET_WALLET',
}

export { strnull, Account, Twitter, State, DefaultState, AccountTypes }
