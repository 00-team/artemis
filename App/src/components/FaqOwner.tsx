import React, { CSSProperties, FC, useState } from 'react'

// style
import './style/faqowner.scss'

// utils
import { C } from '@00-team/utils'

// icons
import { IoIosArrowUp } from '@react-icons/all-files/io/IoIosArrowUp'
import { FAQModel } from 'state/models/Collection'

interface FaqOwnerProps {
    title: string
    style?: CSSProperties
    faqs: FAQModel[]
}

const FaqOwner: FC<FaqOwnerProps> = ({ title, style, faqs }) => {
    const [FaqActive, setFaqActive] = useState(-1)

    return (
        <div className='faqOwner-container' style={style}>
            <div className='faqOwner-title title_small'>
                <span>{title}</span>
            </div>
            <div className='faqOwner-faqs'>
                {faqs.map(({ question, answer }, index) => {
                    return (
                        <div className='faqOwner-wrapper' key={index}>
                            <div
                                className='faq-question-container title_smaller'
                                onClick={() => {
                                    if (FaqActive === index) setFaqActive(-1)
                                    else setFaqActive(index)
                                }}
                            >
                                <div className='faq-question'>{question}</div>
                                <div
                                    className={`icon ${C(
                                        FaqActive === index,
                                        'active'
                                    )}`}
                                >
                                    <IoIosArrowUp size={25} />
                                </div>
                            </div>
                            <div
                                className={`faq-answer description ${C(
                                    FaqActive === index,
                                    'show'
                                )}`}
                            >
                                {answer}
                            </div>
                        </div>
                    )
                })}
            </div>
        </div>
    )
}

export default FaqOwner
