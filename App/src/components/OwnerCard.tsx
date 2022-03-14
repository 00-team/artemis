import React, { FC } from 'react'

// style
import './style/ownercard.scss'

// router
import { Link } from 'react-router-dom'

interface OwnerCardProps {
    link: string
    image: string
}

const OwnerCard: FC<OwnerCardProps> = ({ link, image }) => {
    return (
        <Link className='owner-card-container' to={link}>
            <img src={image} alt='' draggable={false} />
        </Link>
    )
}

export default OwnerCard
