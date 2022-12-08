<template>
     <NavBar></NavBar>
    <div>
        <div class="main-area flex">
            <div class="content-area flex3 mg-r8">
                <div class="article-block black-border mg-b8 mg-t4">
                    <div class="text-area">
                        <p>
                            This is a test
                        </p>
                    </div>
                </div>
                <div class="article-block black-border mg-b8 ">
                </div>
                <div class="article-block black-border mg-b8 ">
                </div>
                <div class="article-block black-border mg-b8 ">
                </div>
                <div class="article-block black-border mg-b8 ">
                </div>
                <div class="article-block black-border mg-b8 ">
                </div>
                <div class="article-block black-border mg-b8 ">
                </div>
                <div class="article-block black-border mg-b8 ">
                </div>
                <div class="article-block black-border mg-b8 ">
                </div>
                <div class="article-block black-border mg-b8 ">
                </div>
                <div class="article-block black-border mg-b8 mg-t4">
                </div>
                <div class="article-block black-border mg-b8 ">

                </div>
                <div class="article-block black-border mg-b8 ">
                </div>
                <div class="article-block black-border mg-b8 ">
                </div>
                <div class="article-block black-border mg-b8 ">
                </div>
                <div class="article-block black-border mg-b8 ">
                </div>
                <div class="article-block black-border mg-b8 ">
                </div>
                <div class="article-block black-border mg-b8 ">
                </div>
                <div class="article-block black-border mg-b8 ">
                </div>
                <div class="article-block black-border mg-b8 ">
                </div>
            </div>
            <div class="recommend-area flex1 black-border flex column mg-r8">
                <div class="tag-area black-border mg-b8" style="height:150px"></div>
                <div class="passage-area black-border mg-t4" style="overflow: auto;"></div>

            </div>
        </div>
    </div>
</template>
<script setup>
import NavBar from '../components/NavBar.vue'
import useStore from '../stores/store.js'
const store = useStore()

</script>
<style scoped>
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
    margin-top: 40px;
    margin-bottom: 20px;
    /*高度随滚动增加  */
    min-height: 100vh;

}

.flex3 {
    flex: 2.8;
}

.mg-r8{
    margin-right: 8px;
}
/* .content-area {}

.recommend-area {} */

.article-block {
    /* height: 90px; */
    height: 90px;
    word-wrap: break-word;
    max-width: 55vw;

}

.white-bg {
    background-color: white;
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


@media screen and (max-width: 1200px) {
    .main-area {
        width: 100%;
    }
    .main-area{
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
    .main-area{
        flex-direction: column;
        width: 100%;
    }
    .content-area{
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