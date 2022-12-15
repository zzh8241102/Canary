<template >

    <div class="choose-area flex">

        <div class="left-choose-area flex">
            <div class="liked" @click="subLikeAct">
                <el-button id="fr-bt">
                    <LikeTagBVue></LikeTagBVue>
                    &nbsp;
                    Liked
                </el-button>
            </div>
            &nbsp;
            <div class="commented" @click="subCommentAct">
                <el-button id="mid-bt">
                    <CommentTagBVue></CommentTagBVue>
                    &nbsp;
                    Commented
                </el-button>
            </div>
            &nbsp;
            <div class="published" @click="subPubAct">
                <el-button id="end-bt">
                    <BookTag></BookTag>
                    &nbsp;
                    Published
                </el-button>
            </div>
        </div>
      
    </div>
    <div class="container">
    <!-- v for in article list -->
    <div v-for=" i in articlesList.articles">
        <div class="article-block black-border mg-b8 mg-t4 flex ">
            <div class="info-area flex">
                <div class="like-area">

                    <center><span >{{ i.like }}</span></center>
                    <center><span  style="display:block;">likes</span></center>

                </div>
                <div class="comment-area">
                    <center><span>{{ i.comment }}</span></center>
                    <center><span  style="display:block;">Ans</span></center>

                </div>
            </div>
            <div class="title-tag-area flex column">
                <div class="title-area font-setter">
                    <span  @click="
                    router.push({ name: 'article', params: { id: i.id} })
                    ">
                        <p class="no-more-than-oneline">{{ i.title }}</p>
                    </span>
                </div>
                <div class="tag-author-area flex">
                    <div class="flex tag-area">
                        <div v-for="(item, index) in i.tags" :key="index">
                            <span style="margin-right: 5px;display: inline-block;" class="font-setter">
                                <el-tag round color="">{{ item }}</el-tag>
                            </span>
                        </div>
                    </div>

                    <div class="author-data-area">
                        <GitAvatar></GitAvatar>
                        <span style="margin-left:6px;margin-right: 10px;max-width: 65;overflow: hidden;">{{ i.author }}</span>
                        <span>{{ i.date }}</span>
                    </div>
                </div>
            </div>
        </div>
        <hr>
    </div>
</div>
</template>
<script setup>

import { computed, ref, onMounted, reactive } from 'vue'
import { getArticlesList,getUserActivity } from '../http/api';
import GitAvatar from './icons/GitAvatar.vue'
import LikeTagBVue from './icons/LikeTagB.vue';
import CommentTagBVue from './icons/CommentTag.vue';
import BookTag from './icons/BookTag.vue';
import router from '../router';
// 引入Math.random

// import { isDark } from '~/composables/dark'
// import PublishTagBVue from './icons/PublishTag.vue'; 

/////////////////////////////////////////////////
const articlesList = reactive({
    articles: []
})
/////////////////////////////////////////////////
// getArticlesList().then(res => {
//     articlesList.articles = res.data.data.articles
// })

const dataToSubmit = reactive({
    params:{
        'user_name':'',
        'is_liked':'false',
        'is_commented':'false',
        'is_published':'false',
    }
})


const subLikeAct = () => {
    // set color
    // get the element named fr-bt
    var frbt = document.getElementById("fr-bt");
    frbt.style.backgroundColor = "#616AEF";
    frbt.style.color = "white";
    // set other two no style
    var midbt = document.getElementById("mid-bt");
    midbt.style.backgroundColor = "white";
    midbt.style.color = "gray";
    var endbt = document.getElementById("end-bt");
    endbt.style.backgroundColor = "white";
    endbt.style.color = "gray";


    dataToSubmit.params.user_name = sessionStorage.getItem('user_name')
    dataToSubmit.params.is_liked = true;
    dataToSubmit.params.is_commented = false;
    dataToSubmit.params.is_published = false;

    getUserActivity(dataToSubmit).then(res => {
        articlesList.articles = res.data.data.articles
    })
}

const subCommentAct = () => {
    var midbt = document.getElementById("mid-bt");
    midbt.style.backgroundColor = "#616AEF";
    midbt.style.color = "white";
    var frbt = document.getElementById("fr-bt");
    frbt.style.backgroundColor = "white";
    frbt.style.color = "gray";
    var endbt = document.getElementById("end-bt");
    endbt.style.backgroundColor = "white";
    endbt.style.color = "gray";

    dataToSubmit.params.user_name = sessionStorage.getItem('user_name')
    dataToSubmit.params.is_commented = true;
    dataToSubmit.params.is_liked = false;
    dataToSubmit.params.is_published = false;
    getUserActivity(dataToSubmit).then(res => {
        articlesList.articles = res.data.data.articles
    })
}

const subPubAct = () => {
    var endbt = document.getElementById("end-bt");
    endbt.style.backgroundColor = "#616AEF";
    endbt.style.color = "white";
    var frbt = document.getElementById("fr-bt");
    frbt.style.backgroundColor = "white";
    frbt.style.color = "gray";
    var midbt = document.getElementById("mid-bt");
    midbt.style.backgroundColor = "white";
    midbt.style.color = "gray";

    dataToSubmit.params.user_name = sessionStorage.getItem('user_name')
    dataToSubmit.params.is_published = true;
    dataToSubmit.params.is_commented = false;
    dataToSubmit.params.is_liked = false;
    getUserActivity(dataToSubmit).then(res => {
        articlesList.articles = res.data.data.articles
    })
}
onMounted(() => {
    dataToSubmit.params.user_name = sessionStorage.getItem('user_name')
    dataToSubmit.params.is_commented = true;
    dataToSubmit.params.is_liked = false;
    dataToSubmit.params.is_published = false;
    var midbt = document.getElementById("mid-bt");
    midbt.style.backgroundColor = "#616AEF";
    midbt.style.color = "white";
    var frbt = document.getElementById("fr-bt");
    frbt.style.backgroundColor = "white";
    frbt.style.color = "gray";
    var endbt = document.getElementById("end-bt");
    endbt.style.backgroundColor = "white";
    endbt.style.color = "gray";
    getUserActivity(dataToSubmit).then(res => {
        articlesList.articles = res.data.data.articles
        console.log(articlesList.articles)
        articlesList.articles.forEach(element => {
            console.log(element)
        });
    })
})


/////////////////////////////////////////////////

</script>
<style scoped>

.bg-cc{
    background-color: #616AEF;
    color:white
}
.container{
    margin-bottom: 5px;
}
.rec-banner{
    margin-left: 5%;
    margin-top: 5px;
    margin-bottom: 5px;
}
.left-choose-area{
    margin-left: 25%;
    width: 40%;
    height: 100%;
    margin-top: 15px;
}
.choose-area{
    height: 50px;
    width: 100%;
    margin-bottom: 10px;
}
.tag-area {
    width: 65%;
}



.author-data-area {
    width: 35%;
}


.info-area {
    height: 70%;
    width: 18%;
    /* background-color: red; */
    display: flex;
    margin: auto;
}

.like-area {
    padding: 8px;
    margin-left: 5%;
    width: 40%;
    border:0.5px solid #9197F3;
    border-radius: 5px;
    margin-right: 5%;
    
}

.small-font-setter{
    font-size: px;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}

.comment-area {
    padding: 8px;
    margin-right: 5%;
    width: 40%;
    border:0.5px solid #9197F3;
    border-radius: 5px;
    margin-right: 5%;
    
}

.title-tag-area {
    height: 90%;
    width: 75%;
    /* background-color: blue; */
    margin: auto;

}

.column {
    flex-direction: column;
}

.flex {
    display: flex;
}

.mg-t4 {
    margin-top: 4px;
}

.mg-b8 {
    margin-bottom: 8px;
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

.black-border {
    /* border: 1px solid black; */
    /* shadow */
    /* box-shadow: 0 2px 3px rgba(0, 0, 0, 0.16), 0 2px 10px rgba(0, 0, 0, 0.12); */
    border-radius: 5px;
    background-color: white;;
}

.article-block {
    /* height: 90px; */
    height: 90px;
    word-wrap: break-word;
    max-width: 55vw;

}

.no-more-than-oneline {
    cursor: pointer;
    padding: 10px;
    padding-top: 15px;
    padding-left: 0px;
    /* 只显示一排文字 */
    overflow: hidden;
    /* 文字超出部分用省略号代替 */
    text-overflow: ellipsis;
    /* 文字超出部分用省略号代替 */
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
    height: 80%;
    margin-bottom: auto;
    min-height: 52px;
    /* background-color: black; */

}

.font-setter {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

@media screen and (max-width: 1200px) {
    .article-block {
        /* height: 90px; */
        height: 90px;
        word-wrap: break-word;
        max-width: 90vw;

    }

}

@media screen and (max-width: 600px) {
    .article-block {
        /* height: 90px; */
        height: 90px;
        word-wrap: break-word;
        max-width: 100vw;

    }
}
</style>