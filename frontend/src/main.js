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
import VueMarkdownEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import vuepressTheme from '@kangc/v-md-editor/lib/theme/vuepress.js';
import '@kangc/v-md-editor/lib/theme/style/vuepress.css';

import Prism from 'prismjs';

VueMarkdownEditor.use(vuepressTheme, {
    Prism,
  });


const app = createApp(App)

app.use(ElementPlus)
app.use(router)
app.use(createPinia())
app.use(VueMarkdownEditor);

import useStore from './stores/store.js'
const store = useStore()

router.beforeEach((to, from, next) => {
    if(to.path == "/login" || to.path == "/register"){
        next()
        
    }else{
        if (sessionStorage.getItem('user_name')!=null){
            next()
        } else {
            next("/login")
            store.loggedError= true
        }
    }
})

//  解决vue3点击路由不跳转的问题
const originalPush = router.push
router.push = function push(location) {
    return originalPush.call(this, location).catch(err => err)
}

app.mount('#app')
