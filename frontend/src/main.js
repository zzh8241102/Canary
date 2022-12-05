// solve all the dependencies for the app
import { createApp } from 'vue' 
import App from './App.vue' // mount with the app
import router from './router' // setup the router
import ElementPlus from 'element-plus' // import the element-plus
import 'mdb-vue-ui-kit/css/mdb.min.css';
import {createPinia }from 'pinia'

import './assets/main.css'

const app = createApp(App)

app.use(ElementPlus)
app.use(router)
app.use(createPinia())

app.mount('#app')
