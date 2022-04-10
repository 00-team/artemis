import React from 'react'

// style
import './style/error404.scss'

const Error404 = () => {
    return (
        <div className='error-container'>
            <div className='stars'>
                <div id='stars'></div>
                <div id='stars2'></div>
                <div id='stars3'></div>
            </div>
            <div className='lamp__wrap'>
                <div className='lamp'>
                    <div className='cable'></div>
                    <div className='cover'></div>
                    <div className='in-cover'>
                        <div className='bulb'></div>
                    </div>
                    <div className='light'></div>
                </div>
            </div>
            <section className='error'>
                <div className='error__content'>
                    <div className='error__message message'>
                        <h1 className='message__title title'>Page Not Found</h1>
                        <p className='message__text title_small'>
                            We're sorry, the page you were looking for couldn't
                            be found.
                        </p>
                    </div>
                    <div className='error__nav e-nav'>
                        <a href='' target='_blank' className='e-nav__link'></a>
                    </div>
                </div>
            </section>
        </div>
    )
}

export default Error404
