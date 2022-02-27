import { WinScrollTYPE } from '../models/WinScrollTop'

export interface SET_SCROLL_TOP {
    type: WinScrollTYPE.SET_SCROLL_TOP
    payload: number
}

export type Action = SET_SCROLL_TOP
