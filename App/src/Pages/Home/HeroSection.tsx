import React, { useState } from 'react'

// style
import './style/herosection.scss'

const HeroSection = () => {
    const [ScrollWin, setScrollWin] = useState(0)

    window.onscroll = () => {
        tranfromHandler()
    }

    const tranfromHandler = () => {
        console.log(window.scrollY)
        setScrollWin(window.scrollY)
    }

    return (
        <section className='hero-container'>
            <div className='stars'>
                <div id='stars'></div>
                <div id='stars2'></div>
                <div id='stars3'></div>
            </div>
            <div className='hero-wrapper'>
                <div className='hero-img-wrapper'></div>
                <div className='hero-text-wrapper'>
                    <div className='title'>Welcome To My NFT COLLECTION</div>
                    {/* <div className='description'>Enjoy</div> */}
                </div>
            </div>
            <div
                className='circle right'
                style={{
                    transform: `scale(${
                        ScrollWin > 300 ? ScrollWin / 100 : '2.8'
                    })  translateX(${-ScrollWin / 2}px)`,
                }}
            ></div>
            <div
                className='circle left'
                style={{
                    transform: `scale(${
                        ScrollWin > 300 ? ScrollWin / 100 : '2.8'
                    })  translateX(${ScrollWin / 2}px)`,
                }}
            ></div>
            <div className='cursor'></div>
        </section>
    )
}

export default HeroSection
