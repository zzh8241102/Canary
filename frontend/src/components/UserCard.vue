<template>
    <el-card class="box-card" :style="boxStyleObj">
      <template #header>
        <div class="card-header">
          <span>Card name</span>
          <el-button class="button" text>Operation button</el-button>
        </div>
      </template>
      <div v-for="o in 4" :key="o" class="text item">{{ 'List item ' + o }}</div>
    </el-card>
  </template>
  
<script setup>

import {ref,onMounted} from 'vue'
// import useStore from '../store/store.js'
const boxStyleObj = ref({
    display:'inline-block',
    width: '320px',
    height: '500px'
})
// const store = useStore()

onMounted(() => {
  if(window.innerWidth <= 1100){
      // 将box-card类的宽度设置为100%
      boxStyleObj.value.width = '80%'
  } else if(window.innerWidth>1100){
    boxStyleObj.value.width = '320px'
  }
  window.onresize = () =>{
    if(window.innerWidth <= 1100){
      // 将box-card类的宽度设置为100%
      boxStyleObj.value.width = '80%'
  } else if(window.innerWidth>1100){
    boxStyleObj.value.width = '320px'
  }
  }
})

</script>

  <style scoped>
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .text {
    font-size: 14px;
  }
  
  .item {
    margin-bottom: 18px;
  }
  
  /* .box-card {
    display:inline-block;
    width: 320px;
    height: 500px;
  } */
  </style>