import React, { FC, ReactNode, useEffect, useRef, useState } from 'react'

import './style/underlinetext.scss'

interface UnderlineTextProps {
    rootMargin?: number | -13
    threshold?: number | 1

    children: ReactNode
}

const UnderlineText: FC<UnderlineTextProps> = ({
    children,
    rootMargin,
    threshold,
}) => {
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
                    threshold: threshold,
                    rootMargin: `${rootMargin}px`,
                }
            )

            observer.observe(LazyRef.current)
        }
        return () => {
            if (observer) observer.disconnect()
        }
    }, [LazyRef])
    return (
        <div
            className={`section-title title ${isIntersecting ? 'shown' : ''}`}
            ref={LazyRef}
        >
            <span>{children}</span>
        </div>
    )
}

export default UnderlineText
