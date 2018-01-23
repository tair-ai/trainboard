var path = require('path')

module.exports = {
    build: {
        env: {NODE_ENV: '"production"'},
        index: path.resolve(__dirname, '../../backends/templates/index.html'),
        assetsRoot: path.resolve(__dirname, '../../backends/static'),
        assetsSubDirectory: '',
        assetsPublicPath: '/static/',
        productionSourceMap: true,
        productionGzip: false,
        productionGzipExtensions: ['js', 'css']
    },
    dev: {
        env: {NODE_ENV: '"development"'},
        port: 6166,
        assetsSubDirectory: 'static',
        assetsPublicPath: '/',
        context: [ //代理路径

        ],
        proxypath: 'http://127.0.0.1:6666',
        cssSourceMap: false
    }
}
