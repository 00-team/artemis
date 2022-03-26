import React, { FC, useEffect, useRef, useState } from 'react'

interface CountUpAnimProps {
    end: number
    speed: number
}

const CountUpAnim: FC<CountUpAnimProps> = ({ end, speed }) => {
    const [Count, setCount] = useState(0)
    const ref = useRef<HTMLDivElement>(null)

    const accumulator = end / 100

    const updateCounterState = () => {
        if (ref && ref.current) {
            const currentCount = parseInt(ref.current.innerText)
            if (currentCount < end) {
                const result = Math.ceil(currentCount + accumulator)
                if (result > end) return setCount(end)

                setCount(result)
            }
        }
        setTimeout(updateCounterState, speed)
    }

    useEffect(() => {
        let isMounted = true
        if (isMounted) {
            updateCounterState()
        }

        return () => {
            isMounted = false
        }
    }, [end])

    return <div ref={ref}>{Count}</div>
}

export default CountUpAnim
