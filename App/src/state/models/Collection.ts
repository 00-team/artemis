interface OwnerX {
    username: string
    picture: string
    description: string
    image: string
}

interface Owner {
    username: string
    picture: string
    banner: string
    wallet: string
    description: string
    floor_price: string
    ceil_price: string
    opensea: string
    twitter: string
    instagram: string
    assets: Asset[]
}

interface Asset {
    image: string
    title: string
    description: string
}

interface OwnerFAQ {
    owner: string
    faqs: FAQ[]
}

interface FAQ {
    question: string
    answer: string
}

export { OwnerX, Owner, Asset, OwnerFAQ, FAQ }

type OwnerState = Owner | null
type XwnerState = OwnerX[]
type FaqState = OwnerFAQ[]

export { OwnerState, XwnerState, FaqState }

enum CollectionTypes {
    SET_OWNER = 'SET_OWNER',
    SET_XWNERS = 'SET_XWNERS',
    SET_FAQS = 'SET_FAQS',
}

export { CollectionTypes }
