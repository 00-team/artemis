import { RuleSetRule, RuleSetUseItem } from 'webpack'

export const CssLoaders: RuleSetUseItem[] = ['style-loader', 'css-loader']

export const SassLoaders: RuleSetUseItem[] = [
    {
        loader: 'sass-loader',
        options: {
            sassOptions: {
                includePaths: ['./App/src/style'],
            },
        },
    },
]

export const DevStyle: RuleSetRule = {
    test: /\.(s|)[ac]ss$/i,
    use: [...CssLoaders, ...SassLoaders],
}
export const BuildStyle: RuleSetRule = {
    test: /\.(s|)[ac]ss$/i,
    use: [...CssLoaders, 'postcss-loader', ...SassLoaders],
}
