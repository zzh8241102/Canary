<template>
    <section class="h-100">
        <div class="container h-100">
            <div class="row justify-content-sm-center h-100">
                <div class="col-xxl-4 col-xl-5 col-lg-5 col-md-7 col-sm-9">
                    <div class="text-center my-5">
                        <h1 class="font-banner">Canary</h1>
                    </div>
                    <div class="card shadow-lg">
                        <div class="card-body p-5">
                            <h1 class="fs-5 card-title fw-bold mb-5 font-banner">Login</h1>
                            <ElContainer>
                                <el-form :label-position="labelPosition" label-width="100px" :model="formLabelAlign"
                                    style="max-width: 360px">
                                    <el-form-item label="username">
                                        <el-input v-model="formLabelAlign.name" />
                                    </el-form-item>
                                    <el-form-item label="password">
                                        <el-input v-model="formLabelAlign.password" />
                                    </el-form-item>
                                    <el-form-item label="email">
                                        <el-input v-model="formLabelAlign.password" />
                                    </el-form-item>
                                    <el-form-item style="display:inline-block">
                                        <el-button type="primary" @click="submitForm(ruleFormRef)">Register</el-button>
                                    </el-form-item>
                                </el-form>
                            </ElContainer>

                        </div>
                        <hr>
                        <div class="card-footer py-1 border-0 filter">
                            <div class="text-center">
                                Already have a account?
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
import { ElContainer } from 'element-plus';
import { reactive, ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'

const labelPosition = ref('right')

const formLabelAlign = reactive({
    name: '',
    password: '',
    email: '',
})
const submitForm = (formEl) => {
    if (!formEl) return
    formEl.validate((valid) => {
        if (valid) {
            console.log('submit!')
        } else {
            console.log('error submit!')
            return false
        }
    })
}

</script>
<style scoped>
.font-banner {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
</style>