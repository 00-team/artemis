interface XwnerModel {
    username: string
    picture: string
    description: string
    image: string
}

interface OwnerModel {
    username: string
    picture: string
    banner: string
    wallet: string | null
    description: string
    floor_price: string
    ceil_price: string
    opensea: string
    twitter: string | null
    instagram: string | null
    assets: AssetModel[]
}

interface AssetModel {
    image: string
    title: string
    description: string
}

interface OwnerFAQModel {
    owner: string
    faqs: FAQModel[]
}

interface FAQModel {
    question: string
    answer: string
}

export { XwnerModel, OwnerModel, AssetModel, OwnerFAQModel, FAQModel }

type OwnerState = OwnerModel | null
type XwnerState = XwnerModel[]
type FaqState = OwnerFAQModel[]

export { OwnerState, XwnerState, FaqState }

enum CollectionTypes {
    SET_OWNER = 'SET_OWNER',
    SET_XWNERS = 'SET_XWNERS',
    SET_FAQS = 'SET_FAQS',
}

export { CollectionTypes }
