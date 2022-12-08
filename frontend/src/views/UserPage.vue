<template>

    <NavBar></NavBar>
    <div class="main-area flex">
        <div class="user-card">
            <UserCard></UserCard>
        </div>
        <div class="setting-area flex column">
            <div class="safety-area black-border">
                <PasswordPic></PasswordPic>
            </div>
            <div class="recent-area">
                <div class="article-block black-border mg-b8 ">
                </div>
                <div class="article-block black-border mg-b8 ">
                </div>
                <div class="article-block black-border mg-b8 ">
                </div><div class="article-block black-border mg-b8 ">
                </div><div class="article-block black-border mg-b8 ">
                </div><div class="article-block black-border mg-b8 ">
                </div><div class="article-block black-border mg-b8 ">
                </div><div class="article-block black-border mg-b8 ">
                </div><div class="article-block black-border mg-b8 ">
                </div><div class="article-block black-border mg-b8 ">
                </div><div class="article-block black-border mg-b8 ">
                </div><div class="article-block black-border mg-b8 ">
                </div>
            </div>


        </div>



    </div>

</template>
<script setup>
import NavBar from '../components/NavBar.vue'
import UserCard from '../components/UserCard.vue'
import PasswordPic from '../components/icons/PasswordPic.vue'
import useStore from '../stores/store.js'

const store = useStore()

</script>
<style scoped>

.recent-area{
    margin-top: 30px;
    margin-left: 2.5%;
    width: 95%;
    height: 100%;
    overflow: auto;
}

.safety-area {
    height: 125px;
    width: 88%;
    margin-top: 10px;
    margin-left: 6%;
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

.black-border {
    /* border: 1px solid black; */
    /* shadow */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.16), 0 2px 10px rgba(0, 0, 0, 0.12);
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
    margin-top: 40px;
    margin-bottom: 20px;
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
    .main-area {
        width: 100%;
        flex-direction: column;
    }
    .user-card{ 
        text-align: center;
        width: 80vw;
        margin: auto;
    }
    .setting-area{
        width: 100vw;
        
    }
    .recent-area{
        margin-left: 0;
        width: 100%;
    }
    .article-block{
        max-width: 100%;;   
        
        width: 100%;
        
        
    }

}
</style>