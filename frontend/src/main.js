// solve all the dependencies for the app
import { createApp } from 'vue' 
import App from './App.vue' // mount with the app
import router from './router' // setup the router
import ElementPlus from 'element-plus' // import the element-plus
import 'mdb-vue-ui-kit/css/mdb.min.css';
import 'element-plus/theme-chalk/el-loading.css';
import 'element-plus/theme-chalk/el-message.css';
import {createPinia }from 'pinia'
import './assets/main.css'


const app = createApp(App)

app.use(ElementPlus)
app.use(router)
app.use(createPinia())

import useStore from './stores/store.js'
const store = useStore()

router.beforeEach((to, from, next) => {
    if(to.path === "/login" || to.path === "/register"){
        next()
    }else{
        if (sessionStorage.getItem('accessToken')){
            next()
        } else {
            next("/login")
            store.loggedError= true
            console.log(store.loggedError)
        }
    }
})


app.mount('#app')
