<template>
<div v-for="(item, index) in allTags" :key="index">
  <el-card class="box-card">
      <template #header>
          <span>
            
            <el-tag size="large" class="font-setter-big tag tag-title-area"  effect="light" @click
            ="jumpTo(item.tag_id)">
            {{ item.tag_name }}</el-tag>
          </span>
      </template>
      <div>
        <p class="card-body">
          {{ item.tag_description }}
        </p>
      </div>
    
  </el-card>
</div>
  </template>
  
  <script setup>
  // set box-card style
  import {ref,reactive} from 'vue'
  import { ElMessage } from 'element-plus'
  import { getTags } from '../http/api';

  import AddTagVue from './icons/AddTag.vue';
  import router from '../router';
  const getUserByLocalOrSession = () => {
  if (sessionStorage.getItem('user_name') != null) {
    return sessionStorage.getItem('user_name')
  } else if (localStorage.getItem('user_name') != null) {
    return localStorage.getItem('user_name')
  } 
}
  const allTags = ref([])

  const data = reactive({
    params: {
      username: getUserByLocalOrSession()
    }
  })

  getTags().then((res) => {
    allTags.value = res.data.tags
  }).catch((err) => {
    console.log(err)
  })

  const jumpTo = (id) => {
    router.push({ name: 'taggedpage', params: { id: id} })
  }
  </script>

<style scoped>

.tag-title-area{
  cursor: pointer;
}
.card-body{
  /* 最多显示四排字 */
  min-height: 102px;
  padding: 0;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 4;
  overflow: hidden;
  
}
.font-setter-big{
  font-size: 17px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.box-card {
  width: 250px;
}
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
  

  
  </style>