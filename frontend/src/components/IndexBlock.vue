<template >
    <!-- v for in article list -->
    <div v-for=" i in articlesList.articles">
        <div class="article-block black-border mg-b8 mg-t4">
            <div class="text-area">
                <p>
                    
                </p>
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
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.16), 0 2px 10px rgba(0, 0, 0, 0.12);
}
.article-block {
    /* height: 90px; */
    height: 90px;
    word-wrap: break-word;
    max-width: 55vw;

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