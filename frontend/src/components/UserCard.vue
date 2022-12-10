<template>
  <el-card class="box-card" :style="boxStyleObj">

    <div class="card-header">
      <div class="block">
        <el-avatar :size="80" :src="circleUrl" />
      </div>
      <div class="font-setter">
        <slot name="username"></slot>
      </div>
      <div class="badge-area">
        <div class="little-badge">
          <center>
            <div>5</div>
          </center>
          <center>Tags</center>
        </div>
        <div class="little-badge">
          <center>
            <div>100</div>
          </center>
          <center>comms</center>
        </div>
        <div class="little-badge">
          <center>
            <div>50</div>
          </center>
          <center>articles</center>
        </div>

      </div>
    </div>

    <div class="detailed-area">
      <div class="combo-area">
        <div class="font-setter"><b>
            <center>email</center>
          </b></div>

        <center>
          <slot name="email"></slot>
        </center>
        <el-button round bg>edit</el-button>
      </div>
      <div class="combo-area">
        <div class="font-setter"><b>
            <center>phone number</center>
          </b></div>

        <center>18608133373</center>
        <el-button round bg>edit</el-button>
      </div>
      <div class="combo-area">
        <div class="font-setter"><b>
            <center>location</center>
          </b></div>

        <center>Chengdu</center>
        <el-button round bg>edit</el-button>
      </div>
      <hr>
      <div class="combo-area">
        <div class="font-setter"><b>
            <center>log out</center>
          </b></div>
          <br>
        <el-button round bg type="warning">log out</el-button>
      </div>
    </div>


  </el-card>
</template>
  
<script setup>

import { ref, onMounted, reactive } from 'vue'
import useStore from '../stores/store.js'
////////////////////////////////////////////////////////
const store = useStore()

const boxStyleObj = ref({
  display: 'inline-block',
  width: '320px',
  height: '620px'
})
const userCardInfo = reactive({
  username: '',
  email: '',
  user_avatar: '',
  user_tags: []
})
// replace with server url latter
const circleUrl = ref('https://avatars.githubusercontent.com/u/227713?s=200&v=3')


////////////////////////////////////////////////////////

onMounted(() => {
  if (window.innerWidth <= 1100) {
    // 将box-card类的宽度设置为100%
    boxStyleObj.value.width = '90%'
  } else if (window.innerWidth > 1100) {
    boxStyleObj.value.width = '320px'
  }
  window.onresize = () => {
    if (window.innerWidth <= 1100) {
      // 将box-card类的宽度设置为100%
      boxStyleObj.value.width = '90%'
    } else if (window.innerWidth > 1100) {
      boxStyleObj.value.width = '320px'
    }
  }


})
////////////////////////////////////////////////////////

</script>

<style scoped>
.combo-area {
  display: flex;
  flex-direction: column;
}

.detailed-area {
  margin-top: 5px;
  display: flex;
  flex-direction: column;
}

.little-badge {
  padding: 8px;
  width: 30%;
  border: 0.5px solid #9197F3;
  border-radius: 5px;
  height: 70px;
}

.badge-area {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  margin-top: 10px;
}

.flex {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.block {
  display: block;

}

.card-header {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}

.font-setter {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
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