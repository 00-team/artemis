import React, { useEffect, useRef, useState } from 'react'

// style
import './style/collection.scss'

const Owners = () => {
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

    return (
        <section className='collection'>
            <div
                className={`section-title title ${
                    isIntersecting ? 'shown' : ''
                }`}
                ref={LazyRef}
            >
                <span>See Our Owners</span>
            </div>
        </section>
    )
}

export default Owners
