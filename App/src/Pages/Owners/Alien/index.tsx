import React, { FC, useEffect, useRef, useState } from 'react'

// style
import './style/alien.scss'

// ICONS
import { IconType } from '@react-icons/all-files'
import { FaInstagram } from '@react-icons/all-files/fa/FaInstagram'
import { FaTelegram } from '@react-icons/all-files/fa/FaTelegram'
import { FaTwitter } from '@react-icons/all-files/fa/FaTwitter'
import { FaEthereum } from '@react-icons/all-files/fa/FaEthereum'

// comps
import NFTCard from '../../../components/NFTCard'

const Alien = () => {
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
    return (
        <section className='owner-container'>
            <section className='thumbnail-container'>
                <div
                    className='owner-thumbnail'
                    style={{
                        backgroundImage:
                            'url(https://cdn.discordapp.com/attachments/860048420253204491/947056906852237322/g224.webp)',
                    }}
                ></div>
                <div className='owner-profile'>
                    <div className='profile-image'></div>
                </div>
            </section>
            <section className='owner-content'>
                <div className='content-container'>
                    <div className='owner-name title'>Alien</div>
                    <div className='owner-wallet'>
                        <div className='icon'>
                            <FaEthereum size={20} />
                        </div>
                        <div className='holder'>0x7ae0...ae9a</div>
                    </div>
                    <div className='owner-descriotion title_small'>
                        Lorem ipsum dolor sit amet consectetur adipisicing elit.
                        Vero corporis labore nulla molestiae est, illum id porro
                        Vero corporis labore nulla molestiae est, illum id
                        incidunt aspernatur, vel
                    </div>
                </div>
                <div className='owner-social'>
                    <div className='open-sea'>
                        <OpenSeaBtn color='blue' name='My Open Sea' />
                    </div>
                    <div className='owner-social-wrapper'>
                        <SocialBtn
                            link='https://web.whatsapp.com/'
                            name='telegram'
                            color='#00ccff'
                            ICON={FaTelegram}
                        />
                        <SocialBtn
                            link='https://web.whatsapp.com/'
                            name='Whatsapp'
                            color='#1DA1F2'
                            ICON={FaTwitter}
                        />
                        <SocialBtn
                            link='https://web.whatsapp.com/'
                            name='instagram'
                            color='#DD2A7B'
                            ICON={FaInstagram}
                        />
                    </div>
                </div>
            </section>
            <section className='owner-collection'>
                <div
                    className={`collection-title title ${
                        isIntersecting ? 'shown' : ''
                    }`}
                    ref={LazyRef}
                >
                    <span>My Collections</span>
                </div>
                <div className='collections-wrapper'>
                    <NFTCard />
                    <NFTCard />
                    <NFTCard />
                    <NFTCard />
                    <NFTCard />
                </div>
            </section>
        </section>
    )
}

export default Alien

interface OpenSeaBtnProps {
    name: string
    color: string
}

const OpenSeaBtn: FC<OpenSeaBtnProps> = ({ name, color }) => {
    return (
        <div className={`open-sea-btn title_small ${color}`}>
            <div className='hover'>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
            {name}
        </div>
    )
}

interface SocialBtnProps {
    ICON: IconType
    name: string
    color: string
    link: string
}

const SocialBtn: FC<SocialBtnProps> = ({ ICON, name, color, link }) => {
    color
    return (
        <a className={`social-btn ${name}`} href={link}>
            <div className='icon'>
                <ICON size={20} fill={color} />
            </div>
            <div className='hover'>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
        </a>
    )
}
