<template>
    
    <router-view :key="$route.fullPath"></router-view>
    <el-backtop :right="100" :bottom="100" />
    
</template>

<script setup>
///////////////////////////////////////////////
import { computed, ref, onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { helloWorld } from './http/api';
import useStore from './stores/store.js'
import NavBar from './components/NavBar.vue'
// import { helloWorld } from './http/api.js'

///////////////////////////////////////////////
const user = ref("")
const store = useStore()
///////////////////////////////////////////////
onMounted(() => {
    // set customized element ui style sheets
    document.body.style.setProperty('--el-color-primary', '#735CFF');
    document.body.style.setProperty('--el-color-primary-light-9', '##EDEDFC');
    document.body.style.setProperty('--el-color-primary-light-3', '#9E8ACF');
 })

 
///////////////////////////////////////////////
</script>


<style scoped>


</style>
