import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Balloon from '@/components/Balloon.vue'

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'index',
      component: Home,
    },
    {
      path: '/balloonpage',
      name: 'balloonpage',
      component: Balloon,
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
