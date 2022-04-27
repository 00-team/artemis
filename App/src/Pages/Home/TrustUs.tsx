import React, { useEffect, useRef, useState } from 'react'

// redux
import { useDispatch, useSelector } from 'react-redux'
import { RootState, UpdateGeneralInfo } from 'state'

// utils
import { DisplayNumbers } from '@00-team/utils'
import UnderlineText from 'components/utils/UnderlineText'
import CountUpAnim from 'components/utils/CountUpAnim'

// style
import './style/trustus.scss'

const _ = (n: number) => DisplayNumbers(n, 1e3, 1e9)
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
                <div className={`trust-item ${isIntersecting ? 'active' : ''}`}>
                    <div className='holder'>Users</div>
                    <CountUpAnim
                        end={Number(_(GeneralInfo.bot_users))}
                        speed={50}
                    />
                </div>
                <div className={`trust-item ${isIntersecting ? 'active' : ''}`}>
                    <div className='holder'>Customers</div>
                    <CountUpAnim
                        end={Number(_(GeneralInfo.accounts))}
                        speed={50}
                    />
                </div>
                <div className={`trust-item ${isIntersecting ? 'active' : ''}`}>
                    <div className='holder'>Twitters</div>
                    <CountUpAnim
                        end={Number(_(GeneralInfo.twitters))}
                        speed={50}
                    />
                </div>
            </div>
        </section>
    )
}

export default TrustUs
