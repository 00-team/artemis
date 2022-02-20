import React from 'react'

// style
import './style/card.scss'

// icons
import { FaEthereum } from '@react-icons/all-files/fa/FaEthereum'
import { BsClockFill } from '@react-icons/all-files/bs/BsClockFill'

const NFTCard = () => {
    return (
        <div className='card-container'>
            <div className='card-wrapper'>
                <img
                    className='thumbnail'
                    src='https://www.larazon.es/resizer/eUdlAaViar6ldNv_0ZzrHDdj1z0=/600x400/smart/filters:format(webp):quality(65)/cloudfront-eu-central-1.images.arcpublishing.com/larazon/C3QPAGIE3RBULNY6TPH7GGWBTQ.jpg'
                />
                <div className='content'>
                    <div className='card-title title_small'>
                        <span>title test</span>
                    </div>
                    <div className='card-description description'>
                        {' '}
                        dolor sit amet consectetur adipisicing elit. Quia
                        consequatur consequuntur amet est doloribus a quas sunt,
                        cumque, aperiam voluptatem rerum fuga laborum, ab quidem
                        veniam enim. Alias, repellendus minima!
                    </div>
                </div>
                <div className='others-wrapper'>
                    <div className='others title_smaller'>
                        <div className='price'>
                            <div className='icon'>
                                <FaEthereum size={20} />
                            </div>
                            <div className='text'>0.041 ETH</div>
                        </div>
                        <div className='time-published'>
                            <div className='icon'>
                                <BsClockFill size={20} />
                            </div>
                            <div className='text'>3 Days Ago</div>
                        </div>
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
