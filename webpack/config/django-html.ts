// path
import { BASE_DIR, APP_DIR, resolve } from './path'

// plugins
import HtmlWP from 'html-webpack-plugin'

const BaseFile = new HtmlWP({
    filename: resolve(BASE_DIR, 'nightcurly/templates/base.html'),
    template: resolve(APP_DIR, 'templates/django.html'),
    inject: true,
    publicPath: '/s/dist/',
    minify: false,
})

export default BaseFile
