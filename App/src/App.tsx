import React, { FC } from 'react'

// alert
import { useAlert } from 'react-alert'

// style
import './style/base.scss'
import './style/fonts/imports.scss'

const App: FC = () => {
    const alert = useAlert()

    global.ReactAlert = alert

    return <div>App</div>
}

export default App
