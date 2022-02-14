// types
import { Configuration } from 'webpack'

// styles
import { BuildStyle } from './config/style'

import HtmlFiles from './config/django-html'

// Main configs
import Main from './main'

const BuildConfig: Configuration = {
    ...Main,
    mode: 'production',
    module: {
        rules: [...Main.module!.rules!, BuildStyle],
    },
    plugins: [...Main.plugins!, ...HtmlFiles],
    optimization: {
        emitOnErrors: false,
        chunkIds: 'deterministic',
        minimize: true,
        splitChunks: {
            chunks: 'all',
            maxSize: 200000,
        },
    },
}

export default BuildConfig
