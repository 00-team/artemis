// types
import { Configuration } from 'webpack'

// styles
import { DevStyle } from './config/style'

import HtmlFiles from './config/django-html'

// Main configs
import Main from './main'

const DjangoConfig: Configuration = {
    ...Main,
    watch: true,
    mode: 'development',
    module: {
        rules: [...Main.module!.rules!, DevStyle],
    },
    plugins: [...Main.plugins!, ...HtmlFiles],
    devtool: 'source-map',
}

export default DjangoConfig
