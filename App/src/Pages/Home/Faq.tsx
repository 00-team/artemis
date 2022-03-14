import React, { useRef } from 'react'

// utils
import UnderlineText from '../../components/utils/UnderlineText'

// comp
import FaqOwner from '../../components/FaqOwner'

// redux
import { useSelector } from 'react-redux'
import { RootState } from 'App/src/redux'

// style
import './style/faq.scss'

const Faq = () => {
    const winScrollY = useSelector((s: RootState) => s.winScrollTop)

    // faqs scroll top ref
    let fstr = useRef<HTMLDivElement>(null)

    if (fstr.current) {
        // owners scroll top
        const ost = fstr.current!.offsetTop - winScrollY

        const element = document.querySelectorAll(
            '.faqOwner-container'
        ) as NodeListOf<HTMLDivElement>

        console.log(element, ost)

        // 1 == manfi

        if (element[0] && element[1]) {
            if (ost < 1100) {
                element[1].style.transform = `translate(600px,600px)`
                element[0].style.transform = `translate(-600px,600px)`
            }
            if (ost < 900) {
                element[1].style.transform = `translate(500px,500px)`
                element[0].style.transform = `translate(-500px,500px)`
            }
            if (ost < 700) {
                element[1].style.transform = `translate(300px,300px)`
                element[0].style.transform = `translate(-300px,300px)`
            }
            if (ost < 600) {
                element[1].style.transform = `translate(150px,150px)`
                element[0].style.transform = `translate(-150px,150px)`
            }
            if (ost < 500) {
                element[1].style.transform = `translate(50px,50px)`
                element[0].style.transform = `translate(-50px,50px)`
            }
            if (ost < 400) {
                element[1].style.transform = `translate(0,0)`
                element[0].style.transform = `translate(0,0)`
            }
        }
    }

    return (
        <div className='faq-container'>
            <UnderlineText>Frequently Asked Questions</UnderlineText>
            <div className='faq-wrapper' ref={fstr}>
                <FaqOwner title='Alien' />
                <FaqOwner title='Arina' />
            </div>
        </div>
    )
}

export default Faq
