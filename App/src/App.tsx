import React, { FC } from 'react'

// router
import { Routes, Route } from 'react-router-dom'

// redux
import { useDispatch } from 'react-redux'
import { WinScrollTYPE } from 'state/models/WinScrollTop'

// alert
import { useAlert } from 'react-alert'

// pages
import Home from './Pages/Home'
import Account from './Pages/Account'
// owners page
import Alien from './Pages/Owners/Alien'

// style
import './style/base.scss'
import './style/fonts/imports.scss'

const App: FC = () => {
    const alert = useAlert()

    global.ReactAlert = alert

    const dispatch = useDispatch()

    window.onscroll = () => {
        dispatch({
            type: WinScrollTYPE.SET_SCROLL_TOP,
            payload: window.scrollY,
        })
    }

    return (
        <>
            {/* <Navbar /> */}
            <main>
                <Routes>
                    <Route path='/' element={<Home />} />
                    <Route path='/owners/alien' element={<Alien />} />
                    <Route path='account' element={<Account />} />
                </Routes>
            </main>
        </>
    )
}

export default App
