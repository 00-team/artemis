import { WebpackPluginInstance } from 'webpack'

// path
import { BASE_DIR, APP_DIR } from './path'
import { resolve } from 'path'

// plugins
import HtmlWP from 'html-webpack-plugin'

const BaseFile = new HtmlWP({
    filename: resolve(BASE_DIR, `evolution/templates/base.html`),
    template: resolve(APP_DIR, 'templates/django.html'),
    inject: true,
    publicPath: '/s/',
    minify: false,
})

const plugins: WebpackPluginInstance[] = [BaseFile]

export default plugins
