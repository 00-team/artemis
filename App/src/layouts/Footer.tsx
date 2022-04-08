import React from 'react'

// utils

// style
import './style/footer.scss'

const SiteLogo = require('../../../static/img/00-Team.png')

const Footer = () => {
    return (
        <div className='footer-container'>
            <div className='footer-wrapper'>
                <div className='footer-columns'>
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

                <div className='footer-logo'>
                    <a href='/'>
                        <img
                            src={SiteLogo}
                            alt='siteLogo site-logo site_logo'
                        />
                    </a>
                    <div className='footer-description description'>
                        ©2022 NightCurly
                    </div>
                </div>
            </div>
            <div className='creator'>
                Created With ❤ By:
                <a href='https://web-00-team.web.app/'>
                    00 Team © {new Date().getFullYear()}
                </a>
            </div>
        </div>
    )
}

export default Footer
