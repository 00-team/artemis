import React, { FC, useRef } from 'react'

// redux
import { useSelector } from 'react-redux'
import { RootState } from 'state'

// style
import './style/owners.scss'

// comps
import OwnerPreviewCard from '../../components/OwnerPreviewCard'
import UnderlineText from '../../components/utils/UnderlineText'

const Owners: FC = () => {
    const winScrollY = useSelector((s: RootState) => s.winScrollTop)
    const Xwners = useSelector((s: RootState) => s.Xwners)

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
        <section className='owners' id='owners'>
            <UnderlineText threshold={1}>See Our Owners</UnderlineText>
            <div className='owners-wrapper' ref={ostr}>
                {Xwners.map(x => (
                    <OwnerPreviewCard key={x.username} {...x} />
                ))}
            </div>
        </section>
    )
}

export default Owners
