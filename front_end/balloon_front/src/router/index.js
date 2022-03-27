import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import PostList from '@/components/PostList.vue'
import PostPage from '@/components/PostPage.vue'

import Auth from '@/components/pages/Auth.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'index',
      component: Home,
    },
    {
      path: '/postlist',
      name: 'postlist',
      component: PostList,
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth,
    },
    {
      path: '/postpage',
      name: 'PostPage',
      component: PostPage,
    },

    

  ],
})
