import { resolve } from 'path'

const BASE_DIR = resolve(__dirname, '../../')
const APP_DIR = resolve(BASE_DIR, 'App')
const DIST_DIR = resolve(BASE_DIR, 'static/dist')
const SRC_DIR = resolve(APP_DIR, 'src')

export { BASE_DIR, APP_DIR, DIST_DIR, SRC_DIR, resolve }
