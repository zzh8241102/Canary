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
                            <h1 class="fs-5 card-title fw-bold mb-5 font-setter">Login</h1>
                            <ElContainer>
                                <el-form :label-position="labelPosition" label-width="100px" :model="loginData"
                                    style="max-width: 360px">
                                    <el-form-item label="username">
                                        <el-input placeholder="length should bewteen 3-20 chars" v-model="loginData.username" />
                                    </el-form-item>
                                    <el-form-item label="password">
                                        <el-input show-password type="password" placeholder="length should bewteen 6-20 chars"
                                            v-model="loginData.password" />
                                    </el-form-item>
                                    <el-form-item style="display:inline-block">

                                        <el-checkbox v-model="remeber" label="remeber me" size="default" />
                                    </el-form-item>
                                    <el-form-item style="display:inline-block">
                                        <el-button type="primary" @click="submitForm">Submit</el-button>
                                    </el-form-item>
                                </el-form>
                            </ElContainer>

                        </div>
                        <hr>
                        <div class="card-footer py-1 border-0 filter">
                            <div class="text-center">
                                Don't have an account?
                                <RouterLink to="/register">Register one!</RouterLink>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </section>
</template>
<script setup>
////////////  resolve imports //////////// 
import { ElContainer, ElMessage } from 'element-plus';
import { reactive, ref, onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import router from "../router/index.js"
import { login } from '../http/api.js'
import useStore from '../stores/store.js'
////////////  resolve imports //////////// 

////////////////////////////////// 
const store = useStore()
const labelPosition = ref('right')
const loginData = reactive({
    username: '',
    password: '',
})
const remeber = ref(false)
////////////////////////////////// 
// store.loggedError= false
const submitForm = () => {
    if (!loginData.username || !loginData.password) {
        ElMessage.error("Please fill in all the fields")
        return
    }

    // 确保用户名长度在6-20之间
    if (loginData.username.length < 3 || loginData.username.length > 20) {
        loginData.username = ''
        loginData.password = ''
        ElMessage.error("Username should be between 6 and 20 characters")
        return
    }
    // 确保密码长度在6-20之间
    if(loginData.password.length < 6 || loginData.password.length > 20){
        loginData.username = ''
        loginData.password = ''
        ElMessage.error("Password should be between 6 and 20 characters")
        return
    }
    console.log(loginData)
    login(loginData).
        then(res => {

            if (res.data.success == "true") {
                ElMessage.success("Login success")
                // store user data into sessionStorag         
                // redirect to home page
                //  store access_token in local storage
                localStorage.setItem('access_token', res.data.token.access_token)
                localStorage.setItem('refresh_token', res.data.token.refresh_token)
                if (!remeber) { sessionStorage.setItem('user_name', res.data.session) }
                else {
                    sessionStorage.setItem('user_name', res.data.session)
                    localStorage.setItem('user_name', res.data.session)
                }
                router.push({ path: "/" })
            }
        }).catch(err => {
            ElMessage.error(err.response.data.message)
        })

}


onMounted(() => {
    // set the bottom-space css 
    document.getElementById("bottom-space").style.setProperty("margin-bottom", "30px")

    if (store.loggedError) {
        ElMessage.error("You must sign in first to experience canary")
    }
})



</script>
<style scoped>
.font-banner {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 20px;
    display: inline-block;
}

.font-setter {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.small-img {
    width: 60px;
    height: 60px;
    display: inline-block;
    margin-bottom: 20px;
    margin-right: 10px;
}
</style>