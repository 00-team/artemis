import React, { useEffect, useRef, useState } from 'react'

// redux
import { useDispatch, useSelector } from 'react-redux'
import { RootState, UpdateGeneralInfo } from 'state'

// utils
import { C, CountAnim } from '@00-team/utils'
import UnderlineText from 'components/utils/UnderlineText'

// style
import './style/trustus.scss'

var UpdaterID: NodeJS.Timer | null = null

const TrustUs = () => {
    const dispatch = useDispatch()
    const GeneralInfo = useSelector((s: RootState) => s.GeneralInfo)

    const LazyRef = useRef<HTMLDivElement>(null)
    const [isIntersecting, setisIntersecting] = useState(false)

    useEffect(() => {
        if (LazyRef.current && !isIntersecting) {
            var observer = new IntersectionObserver(
                ([entry]) => {
                    if (entry && entry.isIntersecting) {
                        setisIntersecting(true)
                        observer.disconnect()
                    }
                },
                {
                    rootMargin: window.innerWidth < 768 ? '-35px' : '-70px',
                }
            )

            observer.observe(LazyRef.current)
        }
        return () => {
            if (observer) observer.disconnect()
        }
    }, [LazyRef])

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
            <div className='trust-wrapper' ref={LazyRef}>
                <div className={'trust-item' + C(isIntersecting, 'active')}>
                    <div className='holder'>Users</div>
                    <CountAnim end={GeneralInfo.bot_users} />
                </div>
                <div className={'trust-item' + C(isIntersecting, 'active')}>
                    <div className='holder'>Customers</div>
                    <CountAnim end={GeneralInfo.accounts} />
                </div>
                <div className={'trust-item' + C(isIntersecting, 'active')}>
                    <div className='holder'>Twitters</div>
                    <CountAnim end={GeneralInfo.twitters} />
                </div>
                <div className={'trust-item' + C(isIntersecting, 'active')}>
                    <div className='holder'>Hits</div>
                    <CountAnim end={GeneralInfo.hits} />
                </div>
            </div>
        </section>
    )
}

export default TrustUs
