import React, { FC, useEffect, useRef, useState } from 'react'

// redux
import { useSelector } from 'react-redux'
import { RootState } from 'state'

// style
import './style/owners.scss'

// comps
import OwnerPreviewCard from '../../components/OwnerPreviewCard'
import UnderlineText from '../../components/utils/UnderlineText'

const Owners: FC = () => {
    const winScrollY = useSelector((s: RootState) => s.winScrollTop)
    const Xwners = useSelector((s: RootState) => s.Xwners)
    const [translate, setTranslate] = useState(0)

    // owners scroll top ref
    const ostr = useRef<HTMLDivElement>(null)

    useEffect(() => {
        if (!ostr.current) return

        const offset =
            Math.round((ostr.current.offsetTop - winScrollY) / 300) * 25 - 25

        setTranslate(offset <= 0 ? 0 : offset)
    }, [winScrollY, ostr])

    return (
        <section className='owners' id='owners'>
            <UnderlineText threshold={1}>See Our Owners</UnderlineText>
            <div className='owners-wrapper' ref={ostr}>
                {Xwners.map(x => (
                    <OwnerPreviewCard
                        key={x.username}
                        {...x}
                        translate={translate}
                    />
                ))}
            </div>
        </section>
    )
}

export default Owners
