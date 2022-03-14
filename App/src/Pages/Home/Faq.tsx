import React, { useRef } from 'react'

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

//     // if (offset < 1100)
//     //     return 600
//     // if (offset < 900)
//     //     return 500
//     // if (offset < 700)
//     //     return 300
//     // if (offset < 600)
//     //     return 200
//     // if (offset < 500)
//     //     return 300
//     // if (offset < 400)
//     //     return 0
// }

const Faq = () => {
    // const winScrollY = useSelector((s: RootState) => s.winScrollTop)
    const FAQs = useSelector((s: RootState) => s.FAQs)
    const FaqRef = useRef<HTMLDivElement>(null)
    // const offset = Offset(FaqRef.current, winScrollY)

    return (
        <div className='faq-container'>
            <UnderlineText>FAQ</UnderlineText>
            <div className='faq-wrapper' ref={FaqRef}>
                {FAQs.map(f => (
                    <FaqOwner title={f.owner} faqs={f.faqs} key={f.owner} />
                ))}
                {/* <FaqOwner
                    title='Alien'
                    style={{
                        transform: `translate(-${offset}px, ${offset}px)`,
                    }}
                />
                <FaqOwner
                    title='Arina'
                    style={{
                        transform: `translate(${offset}px, ${offset}px)`,
                    }}
                /> */}
            </div>
        </div>
    )
}

export default Faq
