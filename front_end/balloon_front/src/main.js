import Vue from 'vue'
// import BootstrapVue3 from 'bootstrap-vue-3'
// import Vue from 'vue'
import App from './App'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// import 'bootstrap-vue/dist/bootstrap-vue.css'
import  BootstrapVue  from 'bootstrap-vue'

import VueSession from 'vue-session'

import router from './router'
import store from './store'

import vuetify from './plugins/vuetify'

// import router from './router'
// import router from './router'

// import axios from 'axios'
Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(VueSession)
new Vue({
    router,
    store,
    vuetify,


    render: h => h(App)
}).$mount('#app')

// const app = createApp(App)
// // app.use(router)
// app.use(router)
// app.use(BootstrapVue3)
// // app.use(VueSession)
// app.mount('#app')


// Vue.prototype.$axios = axios
// const app = createApp({App})

// app.config.globalProperties.$axios = axios

// app.provide('$axios', axios)

// console.log(process.env.VUE_APP_API_BASE_URL)