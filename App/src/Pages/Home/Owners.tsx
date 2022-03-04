import React, { FC, useRef } from 'react'

// redux
import { useSelector } from 'react-redux'
import { RootState } from 'App/src/redux'

// style
import './style/owners.scss'

// comps
import OwnerPreviewCard from '../../components/OwnerPreviewCard'
import UnderlineText from '../../components/utils/UnderlineText'

const Owners: FC = () => {
    const winScrollY = useSelector((s: RootState) => s.winScrollTop)

    // owners scroll top ref
    let ostr = useRef<HTMLDivElement>(null)

    if (ostr.current) {
        // owners scroll top
        const ost = ostr.current!.offsetTop - winScrollY

        const element = document.querySelectorAll(
            '.owner-prev-card'
        ) as NodeListOf<HTMLDivElement>

        if (ost < 900) {
            element.forEach((div: HTMLDivElement) => {
                div.style.transform = `translateY(${75}%)`
            })
        }
        if (ost < 600) {
            element.forEach((div: HTMLDivElement) => {
                div.style.transform = `translateY(${50}%)`
            })
        }
        if (ost < 500) {
            element.forEach((div: HTMLDivElement) => {
                div.style.transform = `translateY(${25}%)`
            })
        }
        if (ost < 400) {
            element.forEach((div: HTMLDivElement) => {
                div.style.transform = `translateY(${12.5}%)`
            })
        }
        if (ost < 300) {
            element.forEach((div: HTMLDivElement) => {
                div.style.transform = `translateY(${0}%)`
            })
        }
        if (ost < 0) {
            element.forEach((div: HTMLDivElement) => {
                div.style.transform = `translateY(${0}%)`
            })
        }
    }

    return (
        <section className='owners'>
            <UnderlineText threshold={1}>See Our Owners</UnderlineText>
            <div className='owners-wrapper' ref={ostr}>
                <OwnerPreviewCard
                    name='Arina'
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
