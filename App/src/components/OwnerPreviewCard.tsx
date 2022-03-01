import React, { FC } from 'react'

// style
import './style/ownerpreviewcard.scss'

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
        <span className='owner-prev-container'>
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
                    <button className='see-more title_smaller'>see more</button>
                </div>
            </div>
        </span>
    )
}

export default OwnerPreviewCard
