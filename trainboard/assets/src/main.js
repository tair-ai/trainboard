import Vue from 'vue'
import VueRouter from 'vue-router'
import routes from './router'
import './style/common'
import API from './api'

Vue.use(VueRouter)
Vue.prototype.$http = API

const router = new VueRouter({
  linkActiveClass: 'active',
  routes: routes
})

new Vue({
	router,
}).$mount('#app')
