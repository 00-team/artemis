import React, { useEffect } from 'react'

// redux
import { useDispatch, useSelector } from 'react-redux'
import { RootState, UpdateGeneralInfo } from 'state'

// utils
import { DisplayNumbers } from '@00-team/utils'
import UnderlineText from 'components/utils/UnderlineText'

// style
import './style/trustus.scss'

const _ = (n: number) => DisplayNumbers(n, 10e3, 10e9)

const TrustUs = () => {
    const dispatch = useDispatch()
    const GeneralInfo = useSelector((s: RootState) => s.GeneralInfo)

    useEffect(() => {
        dispatch(UpdateGeneralInfo())

        let interval = setInterval(() => dispatch(UpdateGeneralInfo()), 7000)

        document.addEventListener('visibilitychange', () => {
            if (document.visibilityState === 'hidden') {
                clearInterval(interval)
            }
        })

        return () => {
            if (interval) {
                clearInterval(interval)
                document.removeEventListener('visibilitychange', () => {})
            }
        }
    }, [dispatch])

    return (
        <section className='trustus-container' id='trust'>
            <UnderlineText threshold={1}>Why Trust Us?</UnderlineText>
            <span>bot users: {_(GeneralInfo.bot_users)}</span>
            <span>accounts: {_(GeneralInfo.accounts)}</span>
            <span>twitters: {_(GeneralInfo.twitters)}</span>
        </section>
    )
}

export default TrustUs
