import React, { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'

// style
import './style/navbar.scss'

// icons
import { AiFillHome } from '@react-icons/all-files/ai/AiFillHome'
import { FaWallet } from '@react-icons/all-files/fa/FaWallet'

const Navbar = () => {
    let location = useLocation()

    const [MenuActive, setMenuActive] = useState(false)

    useEffect(() => {
        console.log(location)
    }, [location])

    return (
        <div className='navbar-container'>
            <div
                onClick={() => setMenuActive(!MenuActive)}
                className={`menu ${MenuActive ? 'active' : ''}`}
            >
                <div className='toggle'></div>

                <li>
                    <div className='first'>
                        <a href='/account'>
                            <FaWallet size={25} />
                        </a>
                    </div>
                </li>
                <li>
                    <div className='sec'>
                        <a href='/'>
                            <AiFillHome size={25} />
                        </a>
                    </div>
                </li>
            </div>
        </div>
    )
}

export default Navbar
