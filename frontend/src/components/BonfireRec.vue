<template>
    <el-row>
      <el-col>
        <el-card :body-style="{ padding: '0px' }">
          <img
            src="../assets/discord.png"
            class="image"
          />
          <div style="padding: 14px">
            <span class="font-setter"><b>Bonfire,
                A place clustering people obtaining same interest</b></span>
            <hr>
            <div class="bottom">
              
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </template>
  
  <script lang="ts" setup>
  import { ref } from 'vue'
  
  const currentDate = ref(new Date())
  </script>
  
  <style scoped>

.font-setter{
    font-family:fantasy;
}

  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .button {
    padding: 0;
    min-height: auto;
  }
  
  .image {
    width: 100%;
    display: block;
  }
  </style>