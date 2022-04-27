import React, { useEffect } from 'react'

// redux
import { useDispatch, useSelector } from 'react-redux'
import { RootState, UpdateGeneralInfo } from 'state'

// utils
import { DisplayNumbers } from '@00-team/utils'
import UnderlineText from 'components/utils/UnderlineText'

// style
import './style/trustus.scss'

const _ = (n: number) => DisplayNumbers(n, 1e3, 1e9)
var UpdaterID: NodeJS.Timer | null = null

const TrustUs = () => {
    const dispatch = useDispatch()
    const GeneralInfo = useSelector((s: RootState) => s.GeneralInfo)

    useEffect(() => {
        const MakeUpdater = () => {
            if (UpdaterID) clearInterval(UpdaterID)
            dispatch(UpdateGeneralInfo())
            UpdaterID = setInterval(() => dispatch(UpdateGeneralInfo()), 7_000)
        }

        MakeUpdater()

        function ChangeTab() {
            if (document.visibilityState === 'hidden' && UpdaterID) {
                clearInterval(UpdaterID)
                UpdaterID = null
            } else if (document.visibilityState === 'visible' && !UpdaterID) {
                MakeUpdater()
            }
        }

        document.addEventListener('visibilitychange', ChangeTab)

        return () => {
            if (UpdaterID) clearInterval(UpdaterID)
            document.removeEventListener('visibilitychange', ChangeTab)
        }
    }, [dispatch])

    return (
        <section className='trustus-container' id='trust'>
            <UnderlineText threshold={1}>Why Trust Us?</UnderlineText>
            <span>bot users: {_(GeneralInfo.bot_users)}</span>
            <span>accounts: {_(GeneralInfo.accounts)}</span>
            <span>twitters: {_(GeneralInfo.twitters)}</span>
            <span>hits: {GeneralInfo.hits}</span>
        </section>
    )
}

export default TrustUs
