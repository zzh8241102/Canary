<template>
  <el-card class="box-card" :style="boxStyleObj">

    <div class="card-header">
      <div class="block">
        <el-avatar :size="80" :src="circleUrl" :key="circleUrl" id="avatar-image" />

        <div class="avatar">
        </div>
      </div>
      <div class="font-setter">
        <AdminBanner></AdminBanner>
        &nbsp;
        <slot name="username"></slot>
      </div>
      <div class="badge-area">
        <div class="little-badge">
          <center>
            <div>
              <slot name="tagNumber"></slot>
            </div>
          </center>
          <center>likes</center>
        </div>
        <div class="little-badge">
          <center>
            <div>
              <slot name="commentsNumber"></slot>
            </div>
          </center>
          <center>comms</center>
        </div>
        <div class="little-badge">
          <center>
            <div>
              <slot name="articleNumber"></slot>
            </div>
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
        <el-button round bg @click="dialogVisible = true">edit</el-button>
      </div>
      <div class="combo-area">
        <div class="font-setter"><b>
            <center>Phone</center>
          </b></div>

        <center>
          <slot name="phoneNumber"></slot>
        </center>
        <el-button round bg @click="dialogVisible = true">edit</el-button>
      </div>
      <div class="combo-area">
        <div class="font-setter"><b>
            <center>location</center>
          </b></div>

        <center>
          <slot name="location"></slot>
        </center>
        <el-button round bg @click="dialogVisible = true">edit</el-button>
      </div>
      <hr>
      <div class="combo-area">
        <div class="font-setter"><b>
            <center>change avatar</center>

          </b></div>
        <el-upload class="upload-demo" drag action="" multiple=False :before-upload="beforeAvatarUpload"
          :http-request="uploadFile">
          <el-icon class="el-icon--upload">
            <upload-filled />
          </el-icon>
          <div class="el-upload__text">
            Drop file here to upload your new avatar
          </div>
          <template #tip>
            <div class="el-upload__tip">
              jpg/png files with a size less than 2MB
            </div>
          </template>
        </el-upload>
      </div>
      <div class="combo-area">
        <div class="font-setter mb-4"><b>
            <center>log out</center>
          </b>
        </div>
        <el-button round bg type="warning" @click="logOut">log out</el-button>
      </div>
    </div>


  </el-card>

  <el-dialog v-model="dialogVisible" title="Change your personal info" :width="dialogWidthOfForm">
    <hr>
    <div style="display: flex;flex-direction: column;">

      <span class="font-setter">
        <h6>Change your email</h6>
      </span>

      <el-input v-model="userInfo.email" placeholder="Please input" />
      <br>
      <span class="font-setter">
        <h6>Change your phone number</h6>
      </span>

      <el-input v-model="userInfo.phoneNumber" placeholder="Please input" />
      <br>
      <span class="font-setter">
        <h6>Change your location</h6>
      </span>

      <el-input v-model="userInfo.location" placeholder="Please input" />
      <hr>
    </div>

    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click="submitForm">
          Confirm
        </el-button>
      </span>
    </template>
  </el-dialog>

</template>
  
<script setup lang="ts">
////////////////////////////////////////////////////////

import { defineProps } from 'vue'
import { ref, onMounted, reactive } from 'vue'
import { ElMessage } from 'element-plus'
import AdminBanner from './icons/AdminBanner.vue';
import { UploadFilled } from '@element-plus/icons-vue'
import useStore from '../stores/store.js'
import type { UploadProps } from 'element-plus'
import axios from 'axios'
import { getUserInfo, changeUserInfo, getAvatar } from '../http/api';


////////////////////////////////////////////////////////

////////////////////////////////////////////////////////
const dialogWidthOfForm = ref('50%')
const circleUrl = ref('')
let dialogVisible = ref(false)
let imageUrl = ref('')
const boxStyleObj = ref({
  display: 'inline-block',
  width: '320px',
  height: '900px'
})

// replace with server url latter

// set username



const userInfo = reactive({
  username: '',
  email: '',
  phoneNumber: '',
  location: ''
})

// typescript assign the sessionStorage('username') to userIndex.username



////////////////////////////////////////////////////////

const getUserByLocalOrSession = () => {
  if (sessionStorage.getItem('user_name') != null) {
    return sessionStorage.getItem('user_name')
  } else if (localStorage.getItem('user_name') != null) {
    return localStorage.getItem('user_name')
  }
}
// verify the file type and size

const beforeAvatarUpload: UploadProps['beforeUpload'] = (rawFile) => {
  const isJPG = rawFile.type === 'image/jpeg'
  const isPNG = rawFile.type === 'image/png'
  if (!isJPG && !isPNG) {
    ElMessage.error('Avatar picture must be JPG/P NG format!')
    return false
  } else if (rawFile.size / 1024 / 1024 > 2) {
    ElMessage.error('Avatar picture size can not exceed 2MB!')
    return false
  }
  return true
}
const userIndex = reactive({
  username: getUserByLocalOrSession()!
})
userIndex.username = getUserByLocalOrSession()!
const uploadFile = (param) => {
  let fileObj = param.file
  let form = new FormData()

  form.append("fileToUpload", fileObj)
  form.append("username", userIndex.username)
  const AvAinstance = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
    timeout: 1000,
  });
  AvAinstance.interceptors.request.use(function (config) {
    config.headers!.Authorization = localStorage.getItem('access_token')
    return config;
  }, function (error) {
    return Promise.reject(error);
  });
  AvAinstance.post("http://127.0.0.1:8000/api/upload/avatar", form, {
    headers: { 'content-type': 'multipart/form-data' }
  }).then(res => {
    imageUrl = res.data.avatar
    setTimeout(() => {
      window.location.reload()
    }, 600)
  }).catch(err => {
    ElMessage.error('Avatar picture upload failed!')
    return false
  })
  ElMessage.success('Avatar picture uploaded successfully!')

}



////////////////////////////////////////////////////////

const data = reactive({
  params: {
    username: userIndex.username
  }
})

getUserInfo(data).then((res) => {
  // console.log(res.data.data.user)
  userInfo.username = res.data.data.user.username
  userInfo.email = res.data.data.user.email
  userInfo.location = res.data.data.user.location
  userInfo.phoneNumber = res.data.data.user.phoneNumber
}).catch((err) => {
  console.log(err)
})


const submitForm = () => {
  dialogVisible.value = false
  changeUserInfo(userInfo).then((res) => {
    ElMessage.success('Change successfully!')
    console.log(res)
    setTimeout(() => {
      window.location.reload()
    }, 600)
  }).catch((err) => {
    ElMessage.error('Change failed!')
  })
}



const data_for_img = reactive({
  params: {
    username: getUserByLocalOrSession()!
  }
})



const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
  timeout: 1000,
  responseType: 'blob'
});

instance.interceptors.request.use(function (config) {
  config.headers!.Authorization = localStorage.getItem('access_token')
  return config;
}, function (error) {
  return Promise.reject(error);
});

instance.get('api/find/avatar', {
  params: {
    username: getUserByLocalOrSession()!
  }
}).then((res) => {
  console.log(res)
  let blob = new Blob([res.data], { type: 'image/png' })
  let url = window.URL.createObjectURL(blob)
  circleUrl.value = url
}).catch((err) => {
  console.log(err)
})

////////////////////////////////////////////////////////
onMounted(() => {
  // circleUrl.value = 'https://avatars.githubusercontent.com/u/227713?s=200&v=3'
  // findUserAvatar(data_for_img)


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


  if (window.innerWidth <= 800) {
    dialogWidthOfForm.value = '80%';
  } else if (window.innerWidth > 800) {
    dialogWidthOfForm.value = '55%';
  }


  window.onresize = () => {
    if (window.innerWidth <= 800) {
      dialogWidthOfForm.value = '80%';
    } else if (window.innerWidth > 800) {
      dialogWidthOfForm.value = '55%';
    }
  }

})

const logOut = () => {
  console.log('log out')
  sessionStorage.clear()
  localStorage.clear()
  window.location.href = '/login'
}

////////////////////////////////////////////////////////

</script>

<style scoped>
.mb-4 {
  margin-bottom: 1px;
}

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
  cursor: pointer;
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

@media screen and (max-width: 490px) {
  .little-badge {
    width: 70px;
    margin-right: 5px;
  }
}
</style>