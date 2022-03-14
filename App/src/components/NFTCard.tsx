import React, { FC } from 'react'

// state
import { AssetModel } from 'state/models/Collection'

// style
import './style/nftcard.scss'

const NFTCard: FC<AssetModel> = ({ description, image, title }) => {
    return (
        <div className='card-container'>
            <div className='card-wrapper'>
                <img className='thumbnail' src={image} />
                <div className='content'>
                    <div className='card-title title_small'>
                        <span>{title}</span>
                    </div>
                    <div className='card-description description'>
                        {description}
                    </div>
                </div>

                <div className='created-by-wrapper'>
                    <div className='created-by'>
                        <div className='avatar'></div>
                        <div className='text title_smaller'>
                            Creation Of: <span className='owner'>ALIEN</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default NFTCard
