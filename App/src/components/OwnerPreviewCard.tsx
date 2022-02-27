import React, { FC } from 'react'

// style
import './style/OwnerPreviewCard.scss'

interface OwnerPreviewCardProps {
    top_img: string
    image: string
    name: string
    detail: string
    link?: string
}

const OwnerPreviewCard: FC<OwnerPreviewCardProps> = ({
    top_img,
    image,
    detail,
    name,
}) => {
    return (
        <div className='owner-prev-card'>
            <div className='owner-prev-top-img'>
                <img src={top_img} alt='' />
            </div>
            <div className='owner-prev-image'>
                <img src={image} alt='' />
            </div>
            <div className='owner-prev-details'>
                <div className='owner-name title_small'>
                    <span>{name}</span>
                </div>
                <div className='owner-detail title_smaller'>{detail}</div>
            </div>
        </div>
    )
}

export default OwnerPreviewCard
