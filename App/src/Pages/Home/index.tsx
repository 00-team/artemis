import React, { FC } from 'react'

// style
import './style/index.scss'

// sections
import HeroSection from './HeroSection'
import Collection from './Collection'

const Home: FC = () => {
    return (
        <main>
            <HeroSection />
            <Collection />
        </main>
    )
}

export default Home
