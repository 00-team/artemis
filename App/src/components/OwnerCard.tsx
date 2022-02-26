import React, { FC } from 'react'

// style
import './style/ownercard.scss'

interface OwnerCardProps {
    link: string
    image: string
}

const OwnerCard: FC<OwnerCardProps> = ({ link, image }) => {
    return (
        <a className='owner-card-container' href={link}>
            <img src={image} alt='' draggable={false} />
        </a>
    )
}

export default OwnerCard
