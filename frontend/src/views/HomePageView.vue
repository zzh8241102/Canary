<template>
    <NavBar></NavBar>
    <div class="body">
        <div class="banner-area">
            <div class="left-title">
                <h2 class="font-setter">Questions</h2>
            </div>
            <div class="big-post">
                <router-link to="/post">
                    <el-button color="#626aef" size="large" style="margin-bottom:5px">
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
                        <el-button color="#626aef" size="small">
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
</template>
<script setup>
////////////////////////////////////////////////
import NavBar from '../components/NavBar.vue'
import IndexBlockVue from '../components/IndexBlock.vue';
import BonfireRec from '../components/BonfireRec.vue'
import useStore from '../stores/store.js'
import { getUserTags } from '../http/api.js'
import { ref, reactive } from 'vue'
const store = useStore()
////////////////////////////////////////////////  
const user_tag_list = reactive({
    tags: []
})

getUserTags().then((res) => {
    user_tag_list.tags = res.data.tags
})
////////////////////////////////////////////////
</script>
<style scoped>

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
    min-height: 220px;
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
    height: 80px;
    padding-top: 20px;
    margin-left: 10%;
    background-color: rgb(241, 239, 239);
}

.left-title {
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
    }

    .article-block {
        /* height: 90px; */
        height: 90px;
        word-wrap: break-word;
        max-width: 90vw;

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

    .article-block {
        /* height: 90px; */
        height: 90px;
        word-wrap: break-word;
        max-width: 100vw;

    }
}
</style>