import React, { useEffect, useRef, useState } from 'react'

// style
import './style/herosection.scss'

// icons
import { ImCross } from '@react-icons/all-files/im/ImCross'

const HeroSection = () => {
    const [ScrollWin, setScrollWin] = useState(0)

    const LazyRef = useRef<HTMLDivElement>(null)
    const [isIntersecting, setisIntersecting] = useState(false)

    useEffect(() => {
        if (LazyRef.current && !isIntersecting) {
            var observer = new IntersectionObserver(([entry]) => {
                if (entry && entry.isIntersecting) {
                    setisIntersecting(true)
                    observer.disconnect()
                }
            })

            observer.observe(LazyRef.current)
        }
        return () => {
            if (observer) observer.disconnect()
        }
    }, [LazyRef])

    window.onscroll = () => {
        tranfromHandler()
    }

    const tranfromHandler = () => {
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
                <div className='hero-text-wrapper' ref={LazyRef}>
                    <div
                        className={`title_hero ${isIntersecting ? 'show' : ''}`}
                        ref={LazyRef}
                    >
                        Welcome To My NFT COLLECTION
                    </div>
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
            <div
                className='cross right'
                style={{
                    transform: `rotate(${ScrollWin}deg)`,
                }}
            >
                <ImCross size={50} />
            </div>
            <div
                className='cross left'
                style={{
                    transform: `rotate(-${ScrollWin}deg)`,
                }}
            >
                <ImCross size={50} />
            </div>
            {/* <div className='cursor'></div> */}
        </section>
    )
}

export default HeroSection
