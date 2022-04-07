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
                        <FaWallet size={25} />
                    </div>
                </li>
                <li>
                    <div className='sec'>
                        <AiFillHome size={25} />
                    </div>
                </li>
            </div>
        </div>
    )
}

export default Navbar
