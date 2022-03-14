import React, { useEffect, useRef, useState } from 'react'

// state
import { useSelector } from 'react-redux'
import { RootState } from 'state'

// style
import './style/herosection.scss'

// icons
import { ImCross } from '@react-icons/all-files/im/ImCross'

// comps
import OwnerCard from '../../components/OwnerCard'

const HeroSection = () => {
    const LazyRef = useRef<HTMLDivElement>(null)
    const [isIntersecting, setisIntersecting] = useState(false)

    const winScrollY = useSelector((s: RootState) => s.winScrollTop)
    const Xwners = useSelector((s: RootState) => s.Xwners)

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

    return (
        <section className='hero-container'>
            <div className='stars'>
                <div id='stars'></div>
                <div id='stars2'></div>
                <div id='stars3'></div>
            </div>
            <div className='hero-wrapper'>
                {/* <div className='hero-img-wrapper'></div> */}
                <div className='hero-text-wrapper' ref={LazyRef}>
                    <div
                        className={`title_hero ${isIntersecting ? 'show' : ''}`}
                        ref={LazyRef}
                    >
                        Welcome To Our NFT COLLECTION
                    </div>
                    {/* <div className='description'>Enjoy</div> */}
                </div>
            </div>
            <section className='owners-container'>
                {Xwners.map(x => (
                    <OwnerCard
                        link={'/owners/' + x.username}
                        image={x.image}
                        key={x.username}
                    />
                ))}
            </section>
            <div
                className='circle right'
                style={{
                    transform: `scale(${
                        winScrollY > 300 ? winScrollY / 150 : '1.5'
                    })  translateX(${-winScrollY / 2}px)`,
                }}
            ></div>
            <div
                className='circle left'
                style={{
                    transform: `scale(${
                        winScrollY > 300 ? winScrollY / 150 : '1.5'
                    })  translateX(${winScrollY / 2}px)`,
                }}
            ></div>
            <div
                className='cross right'
                style={{
                    transform: `rotate(${winScrollY}deg)`,
                }}
            >
                <ImCross size={50} />
            </div>
            <div
                className='cross left'
                style={{
                    transform: `rotate(-${winScrollY}deg)`,
                }}
            >
                <ImCross size={50} />
            </div>
            <div className='scroll-down-container'>
                <div className='scroll-down'></div>
            </div>
        </section>
    )
}

export default HeroSection
