import App from './App'

export default [{
    path: '/',
    component: App,
    children: [
        {
            path: '',
            redirect: 'home'
        },
        {
            path: '/home',
            component: r => require.ensure([], () => r(require('./page/home')), 'home'),
        },
    ]
}]
