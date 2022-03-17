import { Action } from '../action-types/winScrollTop'
import { WinScrollTYPE } from '../models/WinScrollTop'

export default (state = scrollY, action: Action): number => {
    switch (action.type) {
        case WinScrollTYPE.SET_SCROLL_TOP:
            return action.payload

        default:
            return state
    }
}
