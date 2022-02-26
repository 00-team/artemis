import React, { FC } from 'react'

// style
import './style/index.scss'

// sections
import HeroSection from './HeroSection'
import Owners from './Owners'

const Home: FC = () => {
    return (
        <main>
            <HeroSection />
            <Owners />
        </main>
    )
}

export default Home
