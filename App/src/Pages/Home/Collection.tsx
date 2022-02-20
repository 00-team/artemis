import React, { useEffect, useRef, useState } from 'react'

// style
import './style/collection.scss'

import NFTCard from '../../components/NFTCard'

const Collection = () => {
    const LazyRef = useRef<HTMLDivElement>(null)
    const [isIntersecting, setisIntersecting] = useState(false)

    useEffect(() => {
        if (LazyRef.current && !isIntersecting) {
            var observer = new IntersectionObserver(
                ([entry]) => {
                    if (entry && entry.isIntersecting) {
                        setisIntersecting(true)
                        observer.disconnect()
                    }
                },
                {
                    threshold: 1,
                    rootMargin: '-13px',
                }
            )

            observer.observe(LazyRef.current)
        }
        return () => {
            if (observer) observer.disconnect()
        }
    }, [LazyRef])

    useEffect(() => {
        console.log(isIntersecting)
    }, [isIntersecting])

    return (
        <section className='collection'>
            <div
                className={`section-title title ${
                    isIntersecting ? 'shown' : ''
                }`}
                ref={LazyRef}
            >
                <span>Explore Collections</span>
            </div>
            <input
                className='search-bar title_small'
                type='text'
                placeholder='Explore...'
            />
            <div className='collection-wrapper'>
                <NFTCard />
                <NFTCard />
                <NFTCard />
            </div>
        </section>
    )
}

export default Collection
