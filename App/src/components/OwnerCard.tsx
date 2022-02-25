import React, { FC, useState } from 'react'
import { Link } from 'react-router-dom'

// style
import './style/ownercard.scss'

interface OwnerCardProps {
    link: string
}

const OwnerCard: FC<OwnerCardProps> = ({ link }) => {
    const [ShowDetails, setShowDetails] = useState(false)
    setShowDetails

    return (
        <div
            className='owner-card-container'
            tabIndex={0}
            onBlurCapture={() => setShowDetails(false)}
            onFocus={() => setShowDetails(true)}
        >
            <div className='card-preview'>
                <img
                    className='main-image'
                    src='https://i.guim.co.uk/img/media/ef8492feb3715ed4de705727d9f513c168a8b196/37_0_1125_675/master/1125.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=cb647d991d8897cc8a81d2c33c4406d5'
                />
                <div className='owner-image-container'>
                    <div className='owner-image'></div>
                </div>
            </div>
            <div className={`card-details ${ShowDetails ? 'show' : ''}`}>
                <div className='details-wrapper'>
                    <div className='name'>
                        <span>Alien</span>
                    </div>
                    <div className='descriotion'>
                        Lorem ipsum dolor sit amet consectetur adipisicing elit.
                        Nulla voluptatem voluptates ad. Alias, distinctio sit
                        sequi suscipit culpa eius, ut odio asperiores optio
                        corrupti ipsa minima tenetur repellat maiores eum?
                    </div>
                    <Link to={`/owners/${link}`} className='see-more-container'>
                        <div className='see-more'>
                            <button>See More</button>
                        </div>
                    </Link>
                </div>
            </div>
        </div>
    )
}

export default OwnerCard
