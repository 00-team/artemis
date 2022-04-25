import React, { FC, StrictMode } from 'react'
import { hydrate, render } from 'react-dom'

// App
import App from './App'

// router
import { BrowserRouter as Router } from 'react-router-dom'

// redux
import { Provider as ReduxProvider } from 'react-redux'
import { store } from 'state'

// alerts
import { Provider as AlertProvider, AlertProviderProps } from 'react-alert'
import AlertTemplate from './layouts/Alert'

const AlertProps: AlertProviderProps = {
    template: AlertTemplate,
    position: 'top right',
    timeout: 10_000,
    transition: 'fade',
    containerStyle: {
        top: innerWidth <= 768 ? '10px' : '70px',
        zIndex: '1000',

        width: '100%',
        // height: '100%',

        flexDirection: 'column-reverse',
        alignItems: innerWidth <= 768 ? 'center' : 'flex-end',
        justifyContent: 'flex-start',
        gap: '4vh',

        padding: '2rem',
    },
}

const Root: FC = () => {
    return (
        <ReduxProvider store={store}>
            <Router>
                <AlertProvider {...AlertProps}>
                    <App />
                </AlertProvider>
            </Router>
        </ReduxProvider>
    )
}

const RootElement = document.getElementById('root')!
const StrictRoot = (
    <StrictMode>
        <Root />
    </StrictMode>
)

if (RootElement.hasChildNodes()) hydrate(StrictRoot, RootElement)
else render(StrictRoot, RootElement)
