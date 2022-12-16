<template>

    <NavBar></NavBar>
    <div class="body">
        <div class="banner-area">
            <div class="left-title">
                <h2 class="font-setter" style="display:none">Customize your experience</h2>
            </div>
        </div>
        <div class="main-area flex">
            <div class="user-card">
                <UserCard userInfo="userInfo">
                    <template #username>
                        {{ userInfo.username }}
                    </template>
                    <template #email>
                        {{ userInfo.email }}
                    </template>
                    <template #phoneNumber>
                        {{ userInfo.phoneNumber }}
                    </template>
                    <template #location>
                        {{ userInfo.location }}
                    </template>
                    <template #tagNumber>
                        {{userNumInfo.likeNumber}}
                    </template>
                    <template #commentsNumber>
                        {{userNumInfo.commentsNumber}}
                     </template>

                     <template #articleNumber>
                        {{userNumInfo.articleNumber}}
                    </template>
                </UserCard>
            </div>
            <div class="setting-area flex column">
                <div class="safety-area black-border">

                    <div class="safe-setter">
                        <hr>
                        <div>
                            <h5 class="font-setter">Password and account management</h5>
                            <el-button type="info" class="change-button" @click="dialogPasswordVisible = true">Reset your
                                password</el-button>
                        </div>
                        <hr>
                        <div class="delete-area">
                            <p>
                                Once you delete your account, it is irreverseable.<b>Please be careful.</b>
                            </p>

                            <el-button type="danger" class="delete-button" @click="dialogDeleteVisible=true">Delete your account</el-button>
                        </div>
                        <hr>

                    </div>
                    <div class="pic-container">
                        <PasswordPic></PasswordPic>
                    </div>
                    <hr>
                </div>
                <h4 class="font-setter rec-banner">
                    <RecentTag></RecentTag>
                    Recent Activities
                </h4>
                <div class="recent-area">

                    <RecentBlock>

                    </RecentBlock>
                </div>
            </div>
        </div>
<!-- 
    Dialogs
 -->

        <el-dialog v-model="dialogDeleteVisible" title="change your password" width="30%">
            <div style="display: flex;flex-direction: column;">
                <h6>Once you delete your account, it is irreverseable.<b>Please be careful.</b></h6>

            </div>
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="dialogDeleteVisible = false">Cancel</el-button>
                    <el-button type="danger" @click="deleteAccountSub">
                        Confirm Delete
                    </el-button>
                </span>
            </template>
        </el-dialog>


        <el-dialog v-model="dialogPasswordVisible" title="change your password" width="30%">
            <div style="display: flex;flex-direction: column;">
                <span class="font-setter">
                    <h6>Your old password</h6>
                </span>
                <el-input v-model="passwordGroup.oldPassword" type="password"
                show-password  placeholder="Please input your old password" />
                <br>
                <span class="font-setter">
                    <h6>Your new password</h6>
                </span>
                <el-input   v-model="passwordGroup.newPassword" type="password"
                show-password placeholder="Please input your new password"  />

            </div>
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="dialogPasswordVisible = false">Cancel</el-button>
                    <el-button type="primary" @click="changePassWordSub">
                        Confirm
                    </el-button>
                </span>
            </template>
        </el-dialog>
    </div>
</template>
<script setup>
////////////////////////////////////////////////////////////
import NavBar from '../components/NavBar.vue'
import UserCard from '../components/UserCard.vue'
import RecentBlock from '../components/RecentBlock.vue'
import PasswordPic from '../components/icons/PasswordPic.vue'
import useStore from '../stores/store.js'
import { getUserInfo, changePassword,deleteAccount, getUserInfoStats} from '../http/api'
import { ref, reactive } from 'vue'
import { ElMessage } from 'element-plus'
import RecentTag from '../components/icons/RecentTag.vue'

// ////////////////////////////////////////////////////////////

let dialogPasswordVisible = ref(false)
let dialogDeleteVisible = ref(false)

const passwordGroup = reactive({
    username:'',
    oldPassword: '',
    newPassword: ''
})

const userInfo = reactive({
    username: '',
    email: '',
    phoneNumber: '',
    location: ''
})

const userNumInfo = reactive({
    likeNumber: '',
    commentsNumber: '',
    articleNumber: ''
})

const userIndex = reactive({
    username: '',
})

const userStat = reactive({
    tagNumber: '',
    commentsNumber: '',
    articleNumber: ''
})


userIndex.username = sessionStorage.getItem('user_name')
passwordGroup.username = sessionStorage.getItem('user_name')
////////////////////////////////////////////////////////////
console.log(userIndex)

const data = reactive({
    params: {
        username: userIndex.username
    }
})

getUserInfoStats(data).then((res) => {
    console.log(res.data.data)
    userNumInfo.likeNumber = res.data.data.liked
    userNumInfo.commentsNumber = res.data.data.commented
    userNumInfo.articleNumber = res.data.data.published
}).catch((err) => {
    console.log(err)
})

getUserInfo(data).then((res) => {
    // console.log(res.data.data.user)
    userInfo.username = res.data.data.user.username
    userInfo.email = res.data.data.user.email
    userInfo.phoneNumber = res.data.data.user.phoneNumber
    userInfo.location = res.data.data.user.location

}).catch((err) => {
    console.log(err)
})

const deleteAccountSub = () => {
    deleteAccount(userIndex).then((res) => {
        console.log(res)
        dialogDeleteVisible.value = false
        window.location.href = '/login'
        ElMessage.success('Delete your account successfully')
    }).catch((err) => {
        console.log(err.response.data.message)
        ElMessage.error(err.response.data.message)
    })
}

const changePassWordSub = () => {
    dialogPasswordVisible.value = false
    changePassword(passwordGroup).then((res) => {
        console.log(res)
        
    }).catch((err) => {
        console.log(err.response.data.message)
        ElMessage.error(err.response.data.message)
    })

}

////////////////////////////////////////////////////////////////////////////////////
</script>
<style scoped>
.rec-banner{
    margin-top: 13px;
    margin-left: 20px;
}

.delete-button {
    width: 53%;
}

.delete-area {
    display: flex;
    flex-direction: column;
    width: 88%;

    margin-top: 2%;
    margin-right: 5%;
}

.change-button {
    margin-top: 15px;
    width: 45%;
}

.safe-setter {
    display: flex;
    flex-direction: column;
    width: 85%;
    margin-left: 5%;
    margin-top: 2%;
    margin-right: 5%;
}

.pic-container {
    margin-right: 2%;
    margin-top: 10px;
    margin-bottom: 10px;
    width: 110px;
}

.banner-area {
    height: 20px;
    padding-top: 20px;
    margin-left: 10%;
    background-color: rgb(241, 239, 239);
}

.font-setter {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
}

.body {
    background-color: #F1EFEF;
}

.recent-area {
    box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.1);
    margin-top: 10px;
    margin-left: 2.5%;
    margin-bottom: 15px;
    width: 95%;
    height: 100%;
    overflow: auto;
    background-color: white;
}

.safety-area {
    /* 边框浅shadow */
    display: flex;
    box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.1);
    background-color: white;
    min-height: 300px;
    width: 95%;
    margin-top: 10px;
    margin-left: 2.5%;
}

.setting-area {
    width: 75%;

    min-height: 300px;
    overflow: auto;
}

.user-card {
    width: 35%;
}

.mg-b8 {
    margin-bottom: 8px;
}

.mg-t4 {
    margin-top: 4px;
}



.flex {
    display: flex;
}

.column {
    flex-direction: column;
}

.main-area {
    /* 在宽屏时候，总是占据78%的空间,剧中显示 */
    width: 80%;
    margin: auto;
    margin-top: 0px;
    /* margin-bottom: 20px; */
    /*高度随滚动增加  */
    min-height: 100vh;
}


.mg-r8 {
    margin-right: 8px;
}

/* .content-area {}

.recommend-area {} */

.article-block {
    /* height: 90px; */
    height: 90px;
    margin-left: 1%;
    width: 98%;
    word-wrap: break-word;
    max-width: 55vw;

}

.white-bg {
    background-color: white;
}

.text-area {
    width: 80%;
    background-color: aqua;
    height: 50%;
    /* 只显示一排文字 */
    overflow: hidden;
    /* 文字超出部分用省略号代替 */
    text-overflow: ellipsis;
    /* 文字超出部分用省略号代替 */
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
}

/* 当宽度小于1150的时候 */
@media screen and (max-width: 1100px) {
    .change-button{
        width: 65%;
    }
    .delete-button{
        width: 80%;
    }
    .main-area {
        width: 100%;
        flex-direction: column;
    }

    .user-card {
        text-align: center;
        width: 80vw;
        margin: auto;
    }

    .setting-area {
        width: 100vw;

    }

    .recent-area {
        
        width: 95%;
        margin: auto;
    }

    .article-block {
        max-width: 100%;
        ;

        width: 100%;


    }

}


</style>