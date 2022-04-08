import React from 'react'

// utils

// style
import './style/footer.scss'

const Footer = () => {
    return (
        <div className='footer-container'>
            <div className='footer-wrapper'>
                <div className='footer-column'>
                    <div className='start title_small'>NightCurly</div>
                    <a
                        data-text='&nbsp;home'
                        href=''
                        className='link title_smaller'
                    >
                        &nbsp;home
                    </a>
                    <a
                        data-text='&nbsp;FAQ'
                        href=''
                        className='link title_smaller'
                    >
                        &nbsp;FAQ
                    </a>
                    <a
                        data-text='&nbsp;Owners'
                        href=''
                        className='link title_smaller'
                    >
                        &nbsp;Owners
                    </a>
                </div>
                <div className='footer-column'>
                    <div className='start title_small'>community</div>
                    <a
                        data-text='&nbsp;disocrd'
                        href=''
                        className='link title_smaller'
                    >
                        &nbsp;discord
                    </a>
                </div>
            </div>
            <div className='footer-logo'></div>
        </div>
    )
}

export default Footer
