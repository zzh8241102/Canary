<template>
    <NavBar></NavBar>
    <div class="body">
        <div class="banner-area">
            <div class="left-title">
                <QuestionTagVue></QuestionTagVue>
                <h3 class="font-setter">Questions</h3>
            </div>
            <div class="big-post">
                <router-link to="/post">
                    <el-button color="#626aef" size="large" style="margin-bottom:5px" st>
                        Ask a question
                    </el-button>
                </router-link>
            </div>
        </div>
        <div class="main-area flex">
            <div class="content-area flex3 mg-r8">
                <IndexBlockVue></IndexBlockVue>
            </div>
            <div class="recommend-area flex1 flex column mg-r8">
                <div class="tag-area black-border mg-b8">
                    <div class="tag-title-area" style="display:inline-block">
                        <h5 class="font-setter tag-banner">You Tags</h5>
                    </div>
                    <div class="tag-manage-bottom" style="display:inline-block">
                        <el-button color="#626aef" size="small" @click="manageUserTag">
                            manage
                        </el-button>
                    </div>
                    <hr>
                    <div class="tags-area">
                        <div class="tag-inner-area">
                            <div v-for="(item, index) in user_tag_list.tags" :key="index">
                                <span>
                                    <el-tag size="large" effect="light" class="small-tags"><b>{{ item }}</b>
                                    </el-tag>
                                </span>
                            </div>

                        </div>

                    </div>
                </div>

                <div class="bonfire">
                    <BonfireRec></BonfireRec>
                </div>

            </div>
        </div>
    </div>
    <el-dialog v-model="dialogTagManVisible" title="Unfollow the tags you no longer interested"
        :width="dialogWidthComputed" draggable>
        <center>
            <h5 class="font-setter">Select your tags for Unfollowing</h5>
        </center>
        <br>
        <center>
            <el-select v-model="tag_selected" placeholder="Select" style="width: 300px" @change="getSelectedTags">
                <el-option v-for="item in tag_options" :value="item" :label="item" :key="item" />
            </el-select>
        </center>
        <template #footer>
            <span class="dialog-footer">
                <el-button @click="dialogTagManVisible = false">Cancel</el-button>
                <el-button type="primary" @click="userUnFollSub">
                    Confirm
                </el-button>
            </span>
        </template>
    </el-dialog>

    <div id="cookie-area">
        <div class="ck-style">
            <div style="padding-bottom:10px;margin-top: 10px;">
                <cookievue></cookievue>
            </div>
            <span style="margin-left: 10px;padding-top:10px;">We use cookies to personalise your experience</span>
            <el-button type="warning" round class="bt-ck" @click="setCookieUser">Accpet</el-button>
        </div>
    </div>
</template>
<script setup>
////////////////////////////////////////////////
import NavBar from '../components/NavBar.vue'
import IndexBlockVue from '../components/IndexBlock.vue';
import BonfireRec from '../components/BonfireRec.vue'
import { getUserTags, getTags, unFollowTag } from '../http/api.js'
import { ref, reactive, onMounted } from 'vue'
import QuestionTagVue from '../components/icons/QuestionTag.vue';
import { ElMessage } from 'element-plus';
import cookievue from '../components/icons/Cookie.vue'
////////////////////////////////////////////////
const dialogWidthComputed = ref('55%');
const getUserByLocalOrSession = () => {
    if (sessionStorage.getItem('user_name') != null) {
        return sessionStorage.getItem('user_name')
    } else if (localStorage.getItem('user_name') != null) {
        return localStorage.getItem('user_name')
    }
}

let tag_options = reactive([])

const tag_selected = ref('')

const dialogTagManVisible = ref(false)

const user_tag_list = reactive({
    tags: []
})

const data_user = reactive({
    params: {
        username: getUserByLocalOrSession()
    }
})

const manageUserTag = () => {
    dialogTagManVisible.value = true
}


getUserTags(data_user).then((res) => {
    tag_options = res.data.tags
    user_tag_list.tags = res.data.tags
})

const data_unfollow = reactive({
    user_name: getUserByLocalOrSession(),
    tag_name: tag_selected
})



const userUnFollSub = () => {
    dialogTagManVisible.value = false
    unFollowTag(data_unfollow).then((res) => {
        console.log(res)
        ElMessage({
            message: 'Unfollowed',
            type: 'success'
        })
        setTimeout(() => {
            window.location.reload()
        }, 800)
    }).catch((err) => {
        console.log(err)
        ElMessage({
            message: 'Unfollow failed',
            type: 'error'
        })
    })
}


const getSelectedTags = (item) => {
    console.log(item)
    return item
}


const setCookieUser = () => {
    // use cookie to store the user name
     const cookieArea = document.getElementById('cookie-area')
    const user_name = getUserByLocalOrSession()
    let date = new Date()
    date.setTime(date.getTime() + 30 * 24 * 60 * 60 * 1000)
    // set the cookie name as user_name+time, value as user_name
    document.cookie = user_name + '=' + user_name + ';expires=' + date.toGMTString()

    cookieArea.style.display = 'none'
}

const popCookieWindow = () => {
    // check if the user has cookie
    // if cookie value = user_name, then do nothing
    // else, pop the cookie window
    const user_name = getUserByLocalOrSession()
    let cookie_name = user_name
    let cookie_value = user_name
    let cookie = document.cookie
    let cookie_array = cookie.split(';')
    let cookie_flag = false
    for (let i = 0; i < cookie_array.length; i++) {
        let cookie_item = cookie_array[i].split('=')
        if (cookie_item[0].trim() == cookie_name && cookie_item[1].trim() == cookie_value) {
            cookie_flag = true
        }
    }
    if(cookie_flag){
        const cookieArea = document.getElementById('cookie-area')
        cookieArea.style.display = 'none'
        return
    }
    // id="cookie-area"
    const cookieArea = document.getElementById('cookie-area')
    // cookieArea.style.display = 'none'
    // 渐变动画出现，持续1s
    cookieArea.style.opacity = 0
    let op = 0
    let timer = setInterval(() => {
        if (op >= 10000) {
            clearInterval(timer)
        }
        cookieArea.style.opacity = op
        cookieArea.style.filter = 'alpha(opacity=' + op * 1 + ")"
        op += op * 0.1 + 0.1
    }, 10)

}



onMounted(() => {
    popCookieWindow()
    if (window.innerWidth <= 800) {
        dialogWidthComputed.value = '80%';
    } else if (window.innerWidth > 800) {
        dialogWidthComputed.value = '55%';
    }


    window.onresize = () => {
        if (window.innerWidth <= 800) {
            dialogWidthComputed.value = '80%';
        } else if (window.innerWidth > 800) {
            dialogWidthComputed.value = '55%';
        }
    }
})


////////////////////////////////////////////////
</script>
<style scoped>
.bt-ck {
    margin-top: 16px;
    margin-right: 10px;
}

.ck-style {
    margin-top: 1px;
    margin-left: 5px;
    display: flex;
}

#cookie-area {

    display: flex;
    /* display: none; */
    position: fixed;
    /* 在页面下方出现 */
    bottom: 5px;
    /* 在页面右方出现 */
    left: 5px;
    width: 370px;
    height: 70px;
    /* 背景高斯模糊 */
    background-color: aliceblue;
    /* 出现的时候从左到右渐变 */
    border-radius: 5px;
    /* shadow */
    box-shadow: 0 0 2px rgba(0, 0, 0, 0.5);

}

.bonfire {
    margin-top: 30px;
}

.tag-inner-area {
    padding: 8px;
    display: flex;
    flex-wrap: wrap;
    place-content: center;
}

.small-tags {
    margin: 4px;
    font-size: 13px;
}


.tag-manage-bottom {
    position: relative;
    left: 36%;
}

.tag-banner {
    margin-top: 14px;
    margin-left: 20px;
}

.tag-title-area {
    height: 22px;
    background-color: white;
}

.tag-area {
    min-height: 160px;
    background-color: white;
}

.font-setter {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.body {
    background-color: rgb(241, 239, 239);
    z-index: -1;
}

.banner-area {
    display: flex;
    min-height: 80px;
    padding-top: 20px;
    margin-left: 10%;
    background-color: rgb(241, 239, 239);
}

.left-title {
    display: flex !important;
    width: 20%;
    display: inline-block;
}

.big-post {
    width: 15%;
    display: inline-block;
    margin-left: 30%;
}

.mg-b8 {
    margin-bottom: 8px;
}

.mg-t4 {
    margin-top: 4px;
}

.black-border {
    /* border: 1px solid black; */
    /* shadow */
    box-shadow: 0 2px 2px rgba(0, 0, 0, 0.16), 0 2px 2px rgba(0, 0, 0, 0.12);
    background-color: white;
}

.flex {
    display: flex;
}

.flex1 {
    flex: 1;
}

.column {
    flex-direction: column;
}

.main-area {
    /* 在宽屏时候，总是占据78%的空间,剧中显示 */
    width: 80%;
    margin: auto;
    /*高度随滚动增加  */
    min-height: 100vh;


}

.flex3 {
    flex: 2.6;
}

.mg-r8 {
    margin-right: 8px;
}

.content-area {
    background-color: white;
    margin-right: 3%;
    /* shallow shadow*/
    box-shadow: 0 2px 2px rgba(0, 0, 0, 0.16), 0 2px 2px rgba(0, 0, 0, 0.12);
    margin-bottom: 10px;
}

/* .recommend-area {}  */

.article-block {
    /* height: 90px; */
    height: 90px;
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


@media screen and (max-width: 1200px) {
    .main-area {
        width: 100%;
    }

    .main-area {
        flex-direction: column;
        width: 90%;
        margin-left: 6.41%;
    }

    .article-block {
        /* height: 90px; */
        height: 90px;
        word-wrap: break-word;
        max-width: 90vw;

    }

    .tag-area {
        width: 98%;
    }

    .tag-manage-bottom {
        position: relative;
        left: 70%;
    }

    .left-title {
        margin-right: 17%;
    }

    .tag-banner {
        margin-left: 0px;
        position: relative;
        left: 70%;
    }

}

/* 屏幕宽度小于790时 */
@media screen and (max-width: 790px) {
    .main-area {
        width: 100%;
        margin: 0%;
    }


    .content-area {
        width: 100%;
    }

    .tag-area {
        width: 100%;
        margin: 0px;
    }

    .recommend-area {
        width: 100%;
        margin: 0px;
    }

    .tag-manage-bottom {
        position: relative;
        left: 68%;
    }

}



@media screen and (max-width: 490px) {
    .tag-manage-bottom {
        position: relative;
        left: 58%;
    }

    .big-post {
        width: 15%;
        display: inline-block;
        margin-left: 23%;
    }

}
</style>