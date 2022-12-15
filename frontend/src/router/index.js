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
      name: 'post',
      component: () => import('../views/WritingAndPush.vue')
    },
    {
      path: '/tags',
      name: 'tags',
      component: () => import('../views/Tags.vue')
    },
    {
      path: '/user/userpage',
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
    },
    {
      path: '/article/:id',
      name: 'article',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Article.vue')
    },
    {
      path: '/tags/:id',
      name: 'taggedpage',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/TaggedPage.vue')
    }
  ]
})

// vue3 路由有时候不跳转，解决方案
const originalPush = router.push
router.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}





export default router