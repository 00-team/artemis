import React, { CSSProperties, FC, useState } from 'react'

// style
import './style/faqowner.scss'

// utils
import { C } from '@00-team/utils'

// icons
import { IoIosArrowUp } from '@react-icons/all-files/io/IoIosArrowUp'

interface FaqOwnerProps {
    title: string
    style?: CSSProperties
    // faqs: Array<[{ question: string; answer: string }]>
}

const SAMPLE_FAQS = [
    {
        question: 'What is the purpose of this website?',
        answer: 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Mollitia distinctio voluptates itaque quaerat in inventore ipsa architecto perferendis. Ad, exercitationem officia sint incidunt iusto quod recusandae tempora voluptatibus. Facere, dolores.',
    },
    {
        question: 'What is the purpose of this website?',
        answer: 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Mollitia distinctio voluptates itaque quaerat in inventore ipsa architecto perferendis. Ad, exercitationem officia sint incidunt iusto quod recusandae tempora voluptatibus. Facere, dolores.',
    },
    {
        question: 'What is the purpose of this website?',
        answer: 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Mollitia distinctio voluptates itaque quaerat in inventore ipsa architecto perferendis. Ad, exercitationem officia sint incidunt iusto quod recusandae tempora voluptatibus. Facere, dolores.',
    },
]

const FaqOwner: FC<FaqOwnerProps> = ({ title, style }) => {
    const [FaqActive, setFaqActive] = useState(-1)

    return (
        <div className='faqOwner-container' style={style}>
            <div className='faqOwner-title title_small'>
                <span>{title}</span>
            </div>
            <div className='faqOwner-faqs'>
                {SAMPLE_FAQS.map((faq, index) => {
                    return (
                        <div className='faqOwner-wrapper' key={index}>
                            <div
                                className='faq-question-container title_smaller'
                                onClick={() => {
                                    if (FaqActive === index) setFaqActive(-1)
                                    else setFaqActive(index)
                                }}
                            >
                                <div className='faq-question'>
                                    {faq.question}
                                </div>
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
                                {faq.answer}
                            </div>
                        </div>
                    )
                })}
            </div>
        </div>
    )
}

export default FaqOwner
