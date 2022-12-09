<template>
    <NavBar></NavBar>
    <div>
        <div class="main-area flex">
            <div class="content-area white-bg flex3 flex column mg-r8" >
                <div class="article-area flex column black-border">
                    <!-- block b 能够撑开父级别元素 -->
                    <div class="article-block-b  black-border">
                        <!-- article content here -->

                    </div>
                </div>
                <div class="comment-area">
                        <!-- comment content here -->
                        <div class="comment-block black-border mg-b8"></div>
                        <div class="comment-block black-border mg-b8"></div>
                        <div class="comment-block black-border mg-b8"></div>
                        <div class="comment-block black-border mg-b8"></div>
                        <div class="comment-block black-border mg-b8"></div>
                </div>
            </div>
            <div class="recommend-area flex1 black-border flex column mg-r8">
                <div class="tag-area black-border mg-b8" style="height:150px"></div>
                <div class="passage-area black-border mg-t4" style="overflow: auto;"></div>

            </div>
        </div>
    </div>
</template>]
<script setup>
import NavBar from '../components/NavBar.vue'
import useStore from '../stores/store.js'
const store = useStore()

</script>
<style scoped>
.mg-b8 {
    margin-bottom: 8px;
}
.white-bg{
    background-color: white;
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

.article-area {
    min-height: 100px;
    overflow: auto;
}
.comment-area{
    margin-top: 30px;
    min-height: 100px;
    overflow: auto;
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

.mg-r8 {
    margin-right: 8px;
}

.content-area {
    /* 能够被撑大 */
    min-height: 100px;
    
}

/* .recommend-area {} */
.comment-block{
    height: 50px;
}

.article-block-b {
    height: 300px;
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