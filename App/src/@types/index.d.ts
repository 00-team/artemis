// alert
import { AlertManager } from 'react-alert'

declare global {
    var ReactAlert: AlertManager
    var errorCode: string | undefined
    var errorTitle: string | undefined
    var errorDescription: string | undefined
}

declare module 'react' {
    interface HTMLAttributes<T> extends AriaAttributes, DOMAttributes<T> {
        // extends React's HTMLAttributes
        custom?: string
    }
}
