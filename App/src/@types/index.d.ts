// alert
import { AlertManager } from 'react-alert'

declare global {
    var ReactAlert: AlertManager
}

declare module 'react' {
    interface HTMLAttributes<T> extends AriaAttributes, DOMAttributes<T> {
        // extends React's HTMLAttributes
        custom?: string
    }
}
