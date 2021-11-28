import Vue from 'vue'
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')


Vue.createApp({
  el: '#app',
  data(){
      return {
          message: 'Hello Axios',
      }
  },
}).mount('#app')