import { Entry } from 'webpack'

import { resolve, SRC_DIR } from './path'

const Entries: Entry = {
    main: {
        import: resolve(SRC_DIR, 'index.tsx'),
        dependOn: ['Home', 'Account', 'Owner', 'shared'],
    },
    Home: {
        import: resolve(SRC_DIR, 'Pages/Home/'),
        dependOn: ['state', 'shared'],
    },
    Account: {
        import: resolve(SRC_DIR, 'Pages/Account'),
        dependOn: ['state', 'shared'],
    },
    Owner: {
        import: resolve(SRC_DIR, 'Pages/Owner'),
        dependOn: ['state', 'shared'],
    },
    state: {
        import: resolve(SRC_DIR, 'state'),
        dependOn: ['shared'],
    },
    shared: ['react', 'react-dom', 'redux', '@00-team/utils'],
}

export default Entries
