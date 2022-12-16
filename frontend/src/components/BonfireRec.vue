<template>
  <el-row>
    <el-col>
      <el-card :body-style="{ padding: '0px' }" class="box">
        <img src="../assets/discord.png" class="image" />
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
.font-setter {
  font-family: fantasy;
}



.button {
  padding: 0;
  min-height: auto;
}

.image {
  width: 100%;
  display: block;
}

@media screen and (max-width: 1200px) {
  .box {
    width: 98%;
    margin-bottom: 50px;
  }
}
@media screen and (max-width: 790px){
  .box {
    width: 100%;
    margin-bottom: 50px;
  }
}

</style>