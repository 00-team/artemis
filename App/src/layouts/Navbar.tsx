import React, { useState } from 'react'

// style
import './style/navbar.scss'

// icons
import { AiFillHome } from '@react-icons/all-files/ai/AiFillHome'
import { FaWallet } from '@react-icons/all-files/fa/FaWallet'
import { Link } from 'react-router-dom'

const Navbar = () => {
    const [MenuActive, setMenuActive] = useState(false)

    return (
        <div className='navbar-container'>
            <div
                onClick={() => setMenuActive(!MenuActive)}
                className={`menu ${MenuActive ? 'active' : ''}`}
            >
                <div
                    className='toggle'
                    style={{ backgroundImage: 'url(/s/img/navbar-icon.png)' }}
                />

                <li>
                    <div className='first'>
                        <Link to='/account'>
                            <FaWallet size={25} />
                        </Link>
                    </div>
                </li>
                <li>
                    <div className='sec'>
                        <Link to='/'>
                            <AiFillHome size={25} />
                        </Link>
                    </div>
                </li>
            </div>
        </div>
    )
}

export default Navbar
