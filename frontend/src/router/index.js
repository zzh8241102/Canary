import {
  createRouter,
  createWebHistory
} from 'vue-router'


const router = createRouter({
  history: createWebHistory(
    import.meta.env.BASE_URL),
  routes: [{
      path: '/',
      name: 'home',
      component: () => import('../views/HomePageView.vue')
    },
    // children:[
    {
      path: '/post',
      name: 'PostPage',
      component: () => import('../views/WritingAndPush.vue')
    },
    {
      path: '/tags',
      name: 'tags',
      component: () => import('../views/Tags.vue')
    },
    {
      path: '/user/:id',
      name: 'userPage',
      component: () => import('../views/UserPage.vue')
    },
    // ]

    {
      path: '/login',
      name: 'login',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Login.vue')
    },
    {
      path: '/register',
      name: 'register',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Register.vue')
    }
  ]
})



export default router