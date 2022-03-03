import React from 'react'

// utils
import UnderlineText from '../../components/utils/UnderlineText'

// comp
import FaqOwner from '../../components/FaqOwner'

// style
import './style/faq.scss'

const Faq = () => {
    return (
        <div className='faq-container'>
            <UnderlineText>FAQ</UnderlineText>
            <div className='faq-wrapper'>
                <FaqOwner title='Alien' />
                <FaqOwner title='Arina' />
            </div>
        </div>
    )
}

export default Faq
