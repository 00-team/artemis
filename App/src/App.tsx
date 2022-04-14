import React, { FC, useEffect } from 'react'

// loadable
import loadable from '@loadable/component'

// router
import { Routes, Route } from 'react-router-dom'

// redux state
import { useDispatch } from 'react-redux'
import { WinScrollTYPE } from 'state/models/WinScrollTop'
import { GetFAQs } from 'state/actions/collection'

// alert
import { useAlert } from 'react-alert'

// layouts
import Navbar from './layouts/Navbar'
import Footer from './layouts/Footer'

// pages
const Home = loadable(() => import('./Pages/Home'))
const Account = loadable(() => import('./Pages/Account'))
const Owner = loadable(() => import('./Pages/Owner'))

// Error
import Error from './Pages/Error'

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

    if (typeof errorCode !== 'undefined')
        return (
            <Error
                code={errorCode}
                title={errorTitle}
                description={errorDescription}
            />
        )

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
            <Footer />
        </>
    )
}

export default App
