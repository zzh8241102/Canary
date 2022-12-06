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
    // ensure the username and password is valid string length less than 20
    if(regData.username.length > 20 || regData.password.length > 20 || regData.username.length < 2 || regData.password.length < 2){
        // reset the loginData
        regData.username = ''
        regData.password = ''
        regData.email = ''
        ElMessage.error("The length of Username or password is invaild")
        ElMessage.info("The filed are reset for you")
        return
    }
    register(regData)
    .then(res => { 
        if(res.data.success == "true"){
            ElMessage.success("Register successfully")
            console.log(res.data)
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