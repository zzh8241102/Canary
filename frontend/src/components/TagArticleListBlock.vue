<template >
    <!-- v for in article list -->
    <div v-for=" i in articlesList.articles">
        <div class="article-block black-border mg-b8 mg-t4 flex ">
            <div class="info-area flex">
                <div class="like-area">

                    <center><span>{{ i.likes }}</span></center>
                    <center><span style="display:block;">like</span></center>

                </div>
                <div class="comment-area">
                    <center><span>{{ i.comments }}</span></center>
                    <center><span style="display:block;">Ans</span></center>

                </div>
            </div>
            <div class="title-tag-area flex column">
                <div class="title-area font-setter" @click="
                    router.push({ name: 'article', params: { id: i.id} })
                    ">
                    <span>
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
                        <span style="margin-left:6px;margin-right: 10px;max-width: 65;overflow: hidden;">{{ i.author
                        }}</span>
                        <span>{{ i.date }}</span>
                    </div>
                </div>
            </div>
        </div>
        <hr>
    </div>

</template>
<script setup>

////////////////////////////////////////////////
import NavBar from '../components/NavBar.vue'




import { ref, reactive } from 'vue'
import router from '../router';
import { getArticlesListByTag } from '../http/api.js';
////////////////////////////////////////////////  

const currentTagInfo = reactive({
   tag_name: '',
   tag_description: '',
   tag_id: ''
})
// 拿到路由最后参数

const articlesList = reactive({
    articles: []
})

const currentId =  router.currentRoute.value.params.id

const currentIdData = reactive({
   params:{
      tag_id: currentId
   }
   
})

getArticlesListByTag(currentIdData).then((res) => {
   articlesList.articles = res.data.data.articles
//    console.log(res.data)
    console.log(articlesList.articles)
})

</script>
<style scoped>
.tag-area {
    margin-top: 2px;
    width: 65%;
}

.title-area{
    cursor: pointer;
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
    border: 0.5px solid #9197F3;
    border-radius: 5px;
    margin-right: 5%;

}

.small-font-setter {
    font-size: px;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}

.comment-area {
    padding: 8px;
    margin-right: 5%;
    width: 40%;
    border: 0.5px solid #9197F3;
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
    background-color: white;
    ;
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
    padding-top: 8px;
    padding-left: 0px;
    /* 只显示一排文字 */
    overflow: hidden;
    /* 文字超出部分用省略号代替 */
    text-overflow: ellipsis;
    /* 文字超出部分用省略号代替 */
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    height: 80%;
    margin-bottom: auto;
    min-height: 52px;

}

.font-setter {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}


@media screen and (max-width: 600px) {
    .article-block {
        /* height: 90px; */
        height: 90px;
        word-wrap: break-word;
        max-width: 100vw;

    }
}

@media screen and (max-width: 1200px) {
    .article-block {
        /* height: 90px; */
        height: 90px;
        word-wrap: break-word;
        max-width: 90vw;

    }
    
}

@media screen and (max-width: 768px) {
    .article-block {
        /* height: 90px; */
        height: 90px;
        word-wrap: break-word;
        max-width: 100vw;

    }

    .info-area {
        flex-direction: column;
    }

    .like-area {
        height: 65%;
        display: flex;
        width: 90%;
        display: flex;
        /* around */
        justify-content: space-around;
    }

    .comment-area {
        margin-top: 4px;
        height: 65%;
        display: flex;
        width: 90%;
        margin-left: 5%;
        display: flex;
        /* around */
        justify-content: space-around;
    }

    .author-data-area {
        display: flex;
        flex-direction: column;

        height: 30%;

    }

    .author-data-area-inner {
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        margin-bottom: 40px;
        position: relative;
        bottom: 100%;
    }

    .title-box {
        max-width: 20%;
    }

    .no-more-than-oneline {

        margin-right: 0px;
        padding-right: 0px;
    }

    .title-area{
        display: flex;
        flex-direction: row;
        width: 40%;
    }
    .author-data-area-inner{
        align-items: center;
    }
}
</style>