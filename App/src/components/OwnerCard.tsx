import React, { useState } from 'react'

// style
import './style/ownercard.scss'

const OwnerCard = () => {
    const [ShowDetails, setShowDetails] = useState(false)

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
            <div className={`card-details ${ShowDetails ? 'show' : ''}`}></div>
        </div>
    )
}

export default OwnerCard
