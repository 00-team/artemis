import React, { FC } from 'react'

// style
import './style/alert.scss'

import { AlertComponentPropsWithStyle as AlertProps } from 'react-alert'

const Alert: FC<AlertProps> = ({ message, options }) => {
    return (
        <div className={`alert-container ${options.type || 'info'}`}>
            {message}
        </div>
    )
}

export default Alert
