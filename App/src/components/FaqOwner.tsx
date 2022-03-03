import React, { FC } from 'react'

// style
import './style/faqowner.scss'

interface FaqOwnerProps {
    title: string
    // faqs: Array<[{ question: string; answer: string }]>
}

const FaqOwner: FC<FaqOwnerProps> = ({ title }) => {
    return (
        <div className='faqOwner-container'>
            <div className='faqOwner-title title_small'>
                <span>{title}</span>
            </div>
        </div>
    )
}

export default FaqOwner
