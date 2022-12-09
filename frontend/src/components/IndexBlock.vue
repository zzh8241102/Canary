<template >
    <!-- v for in article list -->
    <div v-for=" i in articlesList.articles">
        <div class="article-block black-border mg-b8 mg-t4 flex">
            <div class="info-area flex">
                <div class="like-area">
                    
                    <span>{{i.likes}}</span>
                    <span style="display:block;">likes</span>
                    
                </div>
                <div class="comment-area">
                        <span>{{i.comments}}</span>
                        <span style="display:block;">comments</span>
                    
                </div>
            </div>
            <div class="title-tag-area flex column">
                <div class="title-area">
                    <span><p class="no-more-than-oneline">{{i.title}}</p></span>
                </div>
                <div class="tag-area flex">
                    <div v-for="(item, index) in i.tags" :key="index">
                        <span style="margin-right: 5px;">{{item}}</span>
                    </div>
                    <div class="spacer">
                    </div>
                    <div class="author-data-area">
                        <span style="margin-left:30px;margin-right: 10px;">{{i.author}}</span>
                        <span>{{i.date}}</span>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>
<script setup>
import { computed, ref, onMounted,reactive } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { getArticlesList } from '../http/api';
/////////////////////////////////////////////////
const articlesList = reactive({
    articles: []
})
/////////////////////////////////////////////////
getArticlesList().then(res => {
    // console.log(res.data.data.articles)
    // console.log(res.data.data.articles[0].author)
    articlesList.articles = res.data.data.articles
    console.log(articlesList.articles)
    console.log(articlesList.articles[0].title)
})



/////////////////////////////////////////////////

</script>
<style scoped>

.spacer{
    width: 10%;
}
.info-area{
    height: 80%;
    width: 25%;
    background-color: red;
    display: flex;
    margin: auto;
}

.like-area{
    margin-left: 5%;
    width: 45%;
    background-color: yellow;
}

.comment-area{
    margin-right: 5%;
    width: 45%;
    background-color: green;
}
.title-tag-area{
    height: 90%;
    width: 70%;
    background-color: blue;
    margin: auto;
}
.column{
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

.text-area{
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
    box-shadow: 0 2px 3px rgba(0, 0, 0, 0.16), 0 2px 10px rgba(0, 0, 0, 0.12);
    border-radius: 5px;
}
.article-block {
    /* height: 90px; */
    height: 90px;
    word-wrap: break-word;
    max-width: 55vw;

}
.no-more-than-oneline{
    padding: 10px;
    padding-top: 15px;
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
    background-color: black;
    
}

@media screen and (max-width: 1200px) {
    .article-block {
    /* height: 90px; */
    height: 90px;
    word-wrap: break-word;
    max-width: 90vw;

}

}

@media screen and (max-width: 600px){
    .article-block {
    /* height: 90px; */
    height: 90px;
    word-wrap: break-word;
    max-width: 100vw;

}
}
</style>