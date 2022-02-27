import React, { useEffect, useRef, useState } from 'react'

// style
import './style/owners.scss'

// comps
import OwnerPreviewCard from '../../components/OwnerPreviewCard'

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
        <section className='owners'>
            <div
                className={`section-title title ${
                    isIntersecting ? 'shown' : ''
                }`}
                ref={LazyRef}
            >
                <span>See Our Owners</span>
            </div>
            <div className='owners-wrapper'>
                <OwnerPreviewCard
                    name='Alien'
                    detail='Tell Me Whats The Secret Of Love I Dont Get It'
                    image='https://i.guim.co.uk/img/media/ef8492feb3715ed4de705727d9f513c168a8b196/37_0_1125_675/master/1125.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=cb647d991d8897cc8a81d2c33c4406d5'
                    top_img='https://cdn.discordapp.com/avatars/663056543666667532/363040ba873c85a501ac9b1579958dcb.webp?size=128'
                />
                <OwnerPreviewCard
                    name='Alien'
                    detail='Tell Me Whats The Secret Of Love I Dont Get It'
                    image='https://i.guim.co.uk/img/media/ef8492feb3715ed4de705727d9f513c168a8b196/37_0_1125_675/master/1125.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=cb647d991d8897cc8a81d2c33c4406d5'
                    top_img='https://cdn.discordapp.com/avatars/663056543666667532/363040ba873c85a501ac9b1579958dcb.webp?size=128'
                />
                <OwnerPreviewCard
                    name='Alien'
                    detail='Tell Me Whats The Secret Of Love I Dont Get It'
                    image='https://i.guim.co.uk/img/media/ef8492feb3715ed4de705727d9f513c168a8b196/37_0_1125_675/master/1125.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=cb647d991d8897cc8a81d2c33c4406d5'
                    top_img='https://cdn.discordapp.com/avatars/663056543666667532/363040ba873c85a501ac9b1579958dcb.webp?size=128'
                />
            </div>
        </section>
    )
}

export default Owners
