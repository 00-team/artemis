import React, { FC } from 'react'

// style
import './style/ownerpreviewcard.scss'

// router
import { Link } from 'react-router-dom'

// state
import { XwnerModel } from 'state/models/Collection'

interface OPCProps extends XwnerModel {
    translate?: number
}

const OwnerPreviewCard: FC<OPCProps> = props => {
    const { username, picture, image, description, translate } = props

    return (
        <span className='owner-prev-container'>
            <div
                className='owner-prev-card'
                style={{ transform: `translateY(${translate || 0}%)` }}
            >
                <div className='owner-prev-top-img'>
                    <img src={picture} alt='' />
                </div>
                <div className='owner-prev-image'>
                    <img src={image} alt='' />
                </div>
                <div className='owner-prev-details'>
                    <div className='owner-name title_small'>
                        <span>{username}</span>
                    </div>
                    <div className='owner-detail title_smaller'>
                        {description}
                    </div>
                    <Link
                        to={'/owners/' + username}
                        className='see-more title_smaller'
                    >
                        see more
                    </Link>
                </div>
            </div>
        </span>
    )
}

export default OwnerPreviewCard
