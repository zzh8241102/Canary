<template>
    <router-view></router-view>
</template>

<script setup>
///////////////////////////////////////////////
import { computed, ref, onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import useStore from './stores/store.js'
// import { helloWorld } from './http/api.js'

///////////////////////////////////////////////
const user = ref("")
const store = useStore()
///////////////////////////////////////////////
onMounted(() => {
    document.body.style.setProperty('--el-color-primary', '#261048');
    document.body.style.setProperty('--el-color-primary-light-9', '#F5FBF0');
    document.body.style.setProperty('--el-color-primary-light-3', '#BEBDEB');

    helloWorld.then((res) => {
        store.hello = res.data
    })
})
///////////////////////////////////////////////
</script>


<style>

</style>
