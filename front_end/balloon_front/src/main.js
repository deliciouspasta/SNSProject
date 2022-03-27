import Vue from 'vue'
import App from './App'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import  BootstrapVue  from 'bootstrap-vue'
import VueSession from 'vue-session'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'


Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(VueSession)
new Vue({
    router,
    store,
    vuetify,

    render: h => h(App)
}).$mount('#app')