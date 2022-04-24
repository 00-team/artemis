import React, { FC, useEffect } from 'react'

// redux
import { useDispatch, useSelector } from 'react-redux'
import { RootState, UpdateGeneralInfo } from 'state'

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
            <span>bot users: {GeneralInfo.bot_users}</span>
            <span>accounts: {GeneralInfo.accounts}</span>
            <span>twitters: {GeneralInfo.twitters}</span>
        </div>
    )
}

export default Stats
