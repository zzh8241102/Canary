<template>
    <section class="h-100">
        <div class="container h-100">
            <div class="row justify-content-sm-center h-100">
                <div class="col-xxl-4 col-xl-5 col-lg-5 col-md-7 col-sm-9">
                    <div class="text-center my-4" id="bottom-space">
                        <img class="small-img" src="../assets/mf-trans.webp">
                        <h1 class="font-banner">Canary</h1>
                    </div>
                    <div class="card shadow-lg">
                        <div class="card-body p-4">
                            <h1 class="fs-5 card-title fw-bold mb-5 font-banner">Sign Up</h1>
                            <ElContainer>
                                <el-form :label-position="labelPosition" label-width="100px" :model="regData"
                                    style="max-width: 360px">
                                    <el-form-item label="username" >
                                        <el-input placeholder="Please input your username" v-model="regData.username" />
                                    </el-form-item>
                                    <el-form-item label="password">
                                        <el-input show-password type="password" placeholder="Please input password" v-model="regData.password" />
                                    </el-form-item>
                                    <el-form-item label="email">
                                        <el-input v-model="regData.email" placeholder="Please input your email" />
                                    </el-form-item>
                                    <el-form-item >
                                        <el-button type="primary" @click="submitForm()" class="inline-block">Register</el-button>
                                    </el-form-item>
                                </el-form>
                            </ElContainer>

                        </div>
                        <hr>
                        <div class="card-footer py-1 border-0 filter">
                            <div class="text-center">
                                Already have a account?
                                <RouterLink to="/login">Click to Login!</RouterLink>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </section>
</template>
<script setup>
import { ElContainer,ElMessage } from 'element-plus';
import { reactive, ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import router from "../router/index.js"
import {register} from '../http/api.js'
import useStore from '../stores/store.js'
const store = useStore()


const labelPosition = ref('right')

const regData = reactive({
    username: '',
    password: '',
    email: '',
})
const submitForm = () => {
    if(!regData.username || !regData.password || !regData.email){
        ElMessage.error("Please fill in all the fields")
        return
    }
    //  保证usernmae的长度是在3-20之间
    if(regData.username.length < 3 || regData.username.length > 20){
        regData.username = ''
        regData.password = ''
        regData.email = ''
        ElMessage.error("The length of username should be between 3 and 20")
        return
    }
    // 保证password的长度是在6-20之间
    if(regData.password.length < 6 || regData.password.length > 20){
        regData.username = ''
        regData.password = ''
        regData.email = ''
        ElMessage.error("The length of password should be between 6 and 20")
        return
    }
    
    // 如果不符合email的格式（用regex判断）
    if(!regData.email.match(/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/)){
        regData.username = ''
        regData.password = ''
        regData.email = ''
        ElMessage.error("The email is invaild,notice your email format")
        return
    }
    register(regData)
    .then(res => { 
        if(res.data.success == "true"){
            localStorage.setItem('access_token', res.data.token.access_token)
            localStorage.setItem('refresh_token', res.data.token.refresh_token)
            ElMessage.success("Register successfully")
            sessionStorage.setItem('user_name', res.data.session)
            router.push({path: '/'})
        }
    })
    .catch(err => {
            regData.username = ''
            regData.password = ''
            regData.email = ''
            ElMessage.error(err.response.data.message)
    })
  
}

</script>
<style scoped>
inline-block {
    display: inline-block;
}
.small-img{
    width: 60px;
    height: 60px;
    display: inline-block;
    margin-bottom: 20px;
    margin-right: 10px ;
}
.font-banner {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    display: inline-block;
    margin: 20px;
}
</style>