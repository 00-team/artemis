import { Configuration } from 'webpack'

// path
import { DIST_DIR, SRC_DIR } from './config/path'
import { resolve } from 'path'

const Main: Configuration = {
    entry: resolve(SRC_DIR, 'index.tsx'),
    output: {
        path: DIST_DIR,
        filename: '[name].bundle.js',
        chunkFilename: '[name].[id].chunk.js',
        clean: true,
        sourceMapFilename: 'source_maps/[file].map',
    },
    module: {
        rules: [
            {
                test: /\.(ts|tsx)$/,
                exclude: /node_modules/,
                use: 'ts-loader',
            },
            {
                test: /\.(png|svg|jpg|jpeg|gif)$/i,
                type: 'asset/resource',
            },
        ],
    },
    plugins: [],
    resolve: {
        extensions: ['.mjs', '.tsx', '.ts', '.js'],
    },
}

export default Main
