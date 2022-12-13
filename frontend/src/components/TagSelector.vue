<template>
  <el-select v-model="value" multiple placeholder="Select" style="width: 240px">
    <el-option v-for="item in options" :value="item.tag_name" :label="item.tag_name" :key="item.tag_name"/>
  </el-select>
</template>
  
<script setup>


import { ref, onMounted, reactive } from 'vue'
import { getTags } from '../http/api';

const value = ref('')

let options = reactive([{"tag_name": "test", "tag_description": "test"}])

onMounted(() => {  
  getTags().then((res) => {
    options = res.data.tags
  }).catch((err) => {
    console.log(err)
  })
})






console.log(value)

</script>