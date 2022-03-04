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
            if (ost < 1000) {
                element[1].style.transform = `translate(700px,700px)`
                element[0].style.transform = `translate(-700px,700px)`
            }
            if (ost < 800) {
                element[1].style.transform = `translate(400px,400px)`
                element[0].style.transform = `translate(-400px,400px)`
            }
            if (ost < 600) {
                element[1].style.transform = `translate(250px,250px)`
                element[0].style.transform = `translate(-250px,250px)`
            }
            if (ost < 500) {
                element[1].style.transform = `translate(100px,100px)`
                element[0].style.transform = `translate(-100px,100px)`
            }
            if (ost < 350) {
                element[1].style.transform = `translate(50px,50px)`
                element[0].style.transform = `translate(-50px,50px)`
            }
            if (ost < 200) {
                element[1].style.transform = `translate(0,0)`
                element[0].style.transform = `translate(0,0)`
            }
        }
    }

    return (
        <div className='faq-container'>
            <UnderlineText>FAQ</UnderlineText>
            <div className='faq-wrapper' ref={fstr}>
                <FaqOwner title='Alien' />
                <FaqOwner title='Arina' />
            </div>
        </div>
    )
}

export default Faq
