import React, { useEffect, useRef, useState } from 'react'

// utils
import UnderlineText from '../../components/utils/UnderlineText'

// comp
import FaqOwner from '../../components/FaqOwner'

// redux
import { useSelector } from 'react-redux'
import { RootState } from 'state'

// style
import './style/faq.scss'

// const Offset = (element: HTMLElement | null, SY: number): number => {
//     if (!element) return 0

//     const offset = Math.round((element.offsetTop - SY - 500) / 100)
//     if (offset > 0) return offset * 100

//     return 0
// }

const Faq = () => {
    // const winScrollY = useSelector((s: RootState) => s.winScrollTop)
    const FAQs = useSelector((s: RootState) => s.FAQs)
    const FaqRef = useRef<HTMLDivElement>(null)
    const [shown, setShown] = useState(false)
    // const offset = Offset(FaqRef.current, winScrollY)

    useEffect(() => {
        setShown(FAQs.some(o => o.faqs.length > 0))
    }, [FAQs])

    if (!shown) return <></>

    return (
        <div className='faq-container'>
            <UnderlineText>Frequently Asked Questions</UnderlineText>
            <div className='faq-wrapper' ref={FaqRef}>
                {FAQs.filter(o => o.faqs.length > 0).map(f => (
                    <FaqOwner title={f.owner} faqs={f.faqs} key={f.owner} />
                ))}
            </div>
        </div>
    )
}

export default Faq
