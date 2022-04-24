import React, { FC, useEffect } from 'react'

// redux
import { useDispatch, useSelector } from 'react-redux'
import { RootState, UpdateGeneralInfo } from 'state'

// utils
import { DisplayNumbers } from '@00-team/utils'

const _ = (n: number) => DisplayNumbers(n, 10e3, 10e9)

// style
import './style/stats.scss'

const Stats: FC = () => {
    const dispatch = useDispatch()
    const GeneralInfo = useSelector((s: RootState) => s.GeneralInfo)

    useEffect(() => {
        dispatch(UpdateGeneralInfo())
        let interval = setInterval(() => dispatch(UpdateGeneralInfo()), 7000)

        return () => {
            clearInterval(interval)
        }
    }, [dispatch])

    return (
        <div className='stats-container'>
            <span>bot users: {_(GeneralInfo.bot_users)}</span>
            <span>accounts: {_(GeneralInfo.accounts)}</span>
            <span>twitters: {_(GeneralInfo.twitters)}</span>
        </div>
    )
}

export default Stats
