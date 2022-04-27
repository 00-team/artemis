import React, { useEffect, FC } from 'react'

// sections
import HeroSection from './HeroSection'
import TrustUs from './TrustUs'
import Owners from './Owners'
import Faq from './Faq'

// state
import { useDispatch } from 'react-redux'
import { GetXwners } from 'state/actions/collection'

const Home: FC = () => {
    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(GetXwners())
    }, [dispatch])

    return (
        <main>
            <HeroSection />
            <TrustUs />
            <Owners />
            <Faq />
        </main>
    )
}

export default Home
