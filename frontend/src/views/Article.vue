<template>
    <NavBar></NavBar>
    <div class="body">
        <div class="index-area">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item :to="{ path: '/' }" style="font-size: ;"><b>Homepage</b></el-breadcrumb-item>
                <el-breadcrumb-item style="font-size: medium;">
                    <a href="/">article</a>
                </el-breadcrumb-item>
                <el-breadcrumb-item>
                    {{ article.title }}
                </el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="main-area flex">
            <div class="content-area flex3 flex column mg-r8">
                <!-- block b 能够撑开父级别元素 -->
                <div class="article-block-b white-bg black-border flex column">
                    <!-- article content here -->
                    <div class="article-title">
                        <h2 class="font-setter">{{ article.title }}</h2>
                        <hr>
                    </div>
                    <div class="author-time flex">
                        <div class="author-little">
                            <GitAvatarVue></GitAvatarVue>
                            {{ article.author }}
                        </div>
                        <!-- vertical divider -->
                        <div class="vertical-divider"></div>
                        <div>
                            <el-tag>{{ article.date }}</el-tag>
                        </div>
                    </div>
                    <div class="content-render">
                        <v-md-editor :model-value="article.content" mode="preview"></v-md-editor>
                    </div>
                    <div class="like-area">
                        <el-button class="font-setter" @click="subLike">

                            <Liketag></Liketag>
                            &nbsp;
                            {{ article.likes }} likes
                        </el-button>
                        <el-button @click="showCommentArea">
                            <CommentTag></CommentTag>
                            &nbsp;
                            Comment
                        </el-button>
                    </div>
                </div>
                <div id="new-ans">
                    <div class="banner-com font-setter">
                        <h5>Your Comment</h5>
                    </div>
                    <div class="comment-block flex column">
                        <v-md-editor v-model="currComment_content.content" height="300px"></v-md-editor>

                        <el-button class="sub-comment " type="primary" @click="submitComment">
                            <CommentSub></CommentSub>
                            &nbsp;
                            Submit
                        </el-button>
                    </div>
                </div>
                <div class="banner-com font-setter">
                    <h4>Comments</h4>
                </div>

                <div class="comment-area white-bg black-border">
                    <div class="comment-header font-setter">
                        <hr>
                    </div>
                    <div v-for="(comment, index) in comments" :key="index">
                        <div class="comment-block">

                            <div class="flex">
                                <div class="comment-author">
                                    <GitAvatarVue></GitAvatarVue>
                                    {{ comment.comment_author }}
                                </div>
                                <div class="vertical-divider"></div>
                                <div class="comment-date">

                                    <el-tag>{{ comment.comment_time }}</el-tag>
                                </div>
                            </div>
                            <div class="comment-content">
                                <v-md-editor :model-value="comment.comment_content" mode="preview"></v-md-editor>
                            </div>
                            <hr>
                        </div>

                    </div>
                </div>


            </div>

            <div class="recommend-area flex1 flex column mg-r8">
                <div class="tag-area black-border mg-b8">
                    <div class="tag-title-area" style="display:inline-block">
                        <h5 class="font-setter tag-banner">Tags for this question</h5>
                    </div>
                    <hr>

                    <div class="tag-inner-area">
                        <div v-for="(item, index) in article_tag_list.tags" :key="index">
                            <span>
                                <el-tag size="large" effect="light" class="small-tags"><b>{{ item }}</b>
                                </el-tag>
                            </span>
                        </div>

                    </div>


                </div>
                <div class="related-questions black-border">
                    <div class="tag-title-area" style="display:inline-block">
                        <h5 class="font-setter tag-banner">Related questions</h5>
                    </div>

                    <hr>
                </div>

            </div>
        </div>

    </div>
</template>
<script setup>

//////////////////////////////////////////////////////////////////
import NavBar from '../components/NavBar.vue'
import router from '../router';
import GitAvatarVue from '../components/icons/GitAvatar.vue';
import { getArticle, getUserTags, postComment, getComments, submitLike, findArticleTag } from '../http/api';
import { reactive, onMounted, ref } from 'vue';
import Liketag from '../components/icons/LikeTagB.vue';
import CommentTag from '../components/icons/CommentTag.vue';
import ComentSub from '../components/icons/CommentSub.vue';
import { ElMessage } from 'element-plus';

// get the rounter string
//////////////////////////////////////////////////////////////////

const articleId = router.currentRoute.value.params.id

const showCommentArea = () => {
    document.getElementById('new-ans').style.display = document.getElementById('new-ans').style.display == 'block' ? 'none' : 'block'
}


const article = reactive({
    title: '',
    content: '',
    author: '',
    date: '',
    tags: [],
    likes: 0
})

//////////////////////////////////////////////////////////////////
const currComment_content = reactive(
    {
        article_id: articleId,
        content: '',
        commentor: ''
    }
)

currComment_content.commentor = sessionStorage.getItem('user_name')


const submitComment = () => {
    postComment(currComment_content).then(res => {
        currComment_content.content = ''
        window.location.reload()
    }).catch(err => {
        console.log(err)
    })
}

const dataLike = reactive({

    article_id: articleId,
    user_name: sessionStorage.getItem('user_name')

})

const subLike = () => {
    submitLike(dataLike).then(res => {
        console.log(res)
        article.likes = article.likes + 1
    }).catch(err => {
        console.log(err)
        ElMessage.error('You have already liked this article')
    })

}
//////////////////////////////////////////////////////////////////

const user_tag_list = reactive({
    tags: []
})


const article_tag_list = reactive({
    tags: []
})

const data = reactive({
    params: {
        article_id: articleId
    }
})
//////////////////////////////////////////////////////////////////

let comments = ref([])


onMounted(() => {
    const data = reactive({
        params: {
            article_id: router.currentRoute.value.params.id
        }
    })
    getComments(data).then(res => {
        comments.value = res.data.data
    })
    getArticle(data).then(res => {
        article.title = res.data.data.article.article_title
        article.content = res.data.data.article.article_content
        article.author = res.data.data.article.article_author
        article.date = res.data.data.article.article_date
        article.likes = res.data.data.article.article_likes
    })

    findArticleTag(data).then(res => {
        for (let i = 0; i < res.data.tags.length; i++) {
            console.log(res.data.tags[i].tag_name)
            article_tag_list.tags.push(res.data.tags[i].tag_name)
        }
    }
    )


})

//////////////////////////////////////////////////////////////////
</script>

<style scoped>
#new-ans {
    display: none;
}

.comment-author {
    margin-left: 10px;
}

.related-questions {
    margin-top: 10px;

    min-height: 220px;
    background-color: white;
}

.small-tags {
    margin: 4px;
    font-size: 13px;
}

.tag-inner-area {
    padding: 8px;
    display: flex;
    flex-wrap: wrap;
    place-content: center;
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
    min-height: 220px;
    background-color: white;
}

.sub-comment {
    margin-top: 5px;
    margin-left: 88%;
    width: 12%;
}

.article-title {
    /* 不能超过两行 */
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    margin-bottom: 10px;


}

.vertical-divider {
    width: 1px;
    height: 30px;
    background-color: #F1EFEF;
    margin-left: 10px;
    margin-right: 10px;
}

.author-little {
    margin-left: 10px;

}

.index-area {
    height: 20px;
    width: 80%;
    margin: auto;
    padding-top: 20px;
    margin-bottom: 35px;


}

.font-setter {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
}

.body {
    background-color: #F1EFEF;
}

.mg-b8 {
    margin-bottom: 8px;
}

.white-bg {
    background-color: white;
}

.mg-t4 {
    margin-top: 4px;
}

.black-border {
    /* border: 1px solid black; */
    /* shadow */
    /* box-shadow: 0 2px 5px rgba(0, 0, 0, 0.16), 0 2px 10px rgba(0, 0, 0, 0.12); */
    /* box-shadow: 0 0.1px  rgba(0, 0, 0, 0.16), 0 2px  rgba(0, 0, 0, 0.12); */
    border: 1px solid rgba(0, 0, 0, .125);
    border-radius: 0.25rem;


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

.article-area {
    min-height: 500px;
    overflow: auto;
}

.comment-area {
    margin-top: 10px;
    min-height: 100px;
    overflow: auto;
    padding: 30px;
    padding-top: 0px;
    margin-bottom: 20px;
    padding-left: 15px;
    padding-right: 15px;
}

.main-area {
    /* 在宽屏时候，总是占据78%的空间,剧中显示 */
    width: 80%;
    margin: auto;
    /*高度随滚动增加  */
    min-height: 100vh;

}

.flex3 {
    flex: 2.8;
}

.mg-r8 {
    margin-right: 8px;
}

.content-area {
    /* 能够被撑大 */
    margin-left: 20px;
    margin-right: 20px;

}

/* .recommend-area {} */
.comment-block {
    min-height: 50px;
    margin-top: 5px;
}

.article-block-b {
    min-height: 300px;
    margin-bottom: 20px;
    padding: 30px;
}

.white-bg {
    background-color: white;
}


@media screen and (max-width: 930px) {
    .main-area {
        width: 100%;
    }

    .main-area {
        flex-direction: column;
        width: 90%;
    }


}

/* 屏幕宽度小于600时 */
@media screen and (max-width: 600px) {
    .main-area {
        width: 100%;
    }

    .main-area {
        flex-direction: column;
        width: 100%;
    }

    .content-area {
        margin: 0px;
    }
}
</style>