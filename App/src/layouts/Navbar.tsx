import React, { useEffect } from 'react'
import { useLocation } from 'react-router-dom'

// style
import './style/navbar.scss'

const Navbar = () => {
    let location = useLocation()

    useEffect(() => {
        console.log(location)
    }, [location])

    return <div>Navbar</div>
}

export default Navbar
