// types
import { Configuration } from 'webpack'

// styles
import { BuildStyle, CssExtract } from './config/style'

// plugins
import HtmlPG from './config/django-html'
import Compression from 'compression-webpack-plugin'
import CssMinimizer from 'css-minimizer-webpack-plugin'

// Main configs
import Main from './main'

const BuildConfig: Configuration = {
    ...Main,
    mode: 'production',
    module: {
        rules: [...Main.module!.rules!, BuildStyle],
    },
    plugins: [
        ...Main.plugins!,
        new CssExtract({ filename: '[name].[contenthash].css' }),
        new Compression({ exclude: /\.(html)$/ }),
        HtmlPG,
    ],
    optimization: {
        emitOnErrors: false,
        chunkIds: 'deterministic',
        minimize: true,
        minimizer: [new CssMinimizer()],
    },
}

export default BuildConfig
