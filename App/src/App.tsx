import React, { FC, useEffect } from 'react'

// router
import { Routes, Route } from 'react-router-dom'

// redux state
import { useDispatch } from 'react-redux'
import { WinScrollTYPE } from 'state/models/WinScrollTop'
import { GetFAQs } from 'state/actions/collection'

// alert
import { useAlert } from 'react-alert'

// layouts
import Navbar from 'layouts/Navbar'

// pages
import Home from './Pages/Home'
import Account from './Pages/Account'

// owners page
import Owner from './Pages/Owner'

// style
import './style/base.scss'
import './style/fonts/imports.scss'

const App: FC = () => {
    const alert = useAlert()

    global.ReactAlert = alert

    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(GetFAQs())

        window.onscroll = () =>
            dispatch({
                type: WinScrollTYPE.SET_SCROLL_TOP,
                payload: scrollY,
            })
    }, [dispatch])

    return (
        <>
            <Navbar />
            <main>
                <Routes>
                    <Route path='/' element={<Home />} />
                    <Route path='/owners/:username' element={<Owner />} />
                    <Route path='account' element={<Account />} />
                </Routes>
            </main>
        </>
    )
}

export default App
