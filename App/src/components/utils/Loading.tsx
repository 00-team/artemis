import React, { FC } from 'react'

// style
import './style/loading.scss'

interface LoadingProps {
    message: string
}

const Loading: FC<LoadingProps> = ({ message }) => {
    return (
        <div className='loading-container'>
            <div className='loading'>
                <div className='loading__square'></div>
                <div className='loading__square'></div>
                <div className='loading__square'></div>
                <div className='loading__square'></div>
                <div className='loading__square'></div>
                <div className='loading__square'></div>
                <div className='loading__square'></div>
            </div>
            <div className='title_small loading_message'>{message}</div>
        </div>
    )
}

export default Loading
