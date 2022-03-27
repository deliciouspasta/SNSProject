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






// import { createRouter, createWebHistory } from 'vue-router'
// import Home from '../views/Home.vue'
// import About from '../views/About.vue'

// const routes = [
//   {
//     path: '/',
//     name: 'Home',
//     component: Home
//   },
//   {
//     path: '/about',
//     name: 'About',
//     // route level code-splitting
//     // this generates a separate chunk (about.[hash].js) for this route
//     // which is lazy-loaded when the route is visited.
//     component: About
//   }
// ]

// const router = createRouter({
//   history: createWebHistory(process.env.BASE_URL),
//   routes
// })

// export default router
