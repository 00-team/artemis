import React, { FC } from 'react'

// style
import './style/footer.scss'

const Footer: FC = () => {
    return (
        <div className='footer-container'>
            <div className='footer-wrapper'>
                <div className='footer-columns'>
                    <div className='footer-column'>
                        <div className='start'>NightCurly</div>
                        <a
                            data-text='&nbsp;home'
                            href='/'
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
                        <div className='start'>community</div>
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
                            src='/s/img/00-Team.png'
                            alt='siteLogo site-logo site_logo'
                            draggable={false}
                        />
                    </a>
                    <div className='footer-description description'>
                        © {new Date().getFullYear()} NightCurly
                    </div>
                </div>
            </div>
            <div className='creator'>
                Created With ❤ By:
                <a href='https://web-00-team.web.app/'>00 Team</a>
            </div>
        </div>
    )
}

export default Footer
