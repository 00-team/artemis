import React, { FC } from 'react'

// style
import './style/index.scss'

// sections
import HeroSection from './HeroSection'
import Owners from './Owners'
import Faq from './Faq'

const Home: FC = () => {
    return (
        <main>
            <HeroSection />
            <Owners />
            <Faq />
        </main>
    )
}

export default Home
