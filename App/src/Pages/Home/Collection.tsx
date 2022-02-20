import React from 'react'

// style
import './style/collection.scss'

const Collection = () => {
    return (
        <section className='collection'>
            <div className='section-title title'>Explore Collections</div>
            <input
                className='search-bar title_small'
                type='text'
                placeholder='Explore...'
            />
            <div className='collection-wrapper'></div>
        </section>
    )
}

export default Collection
