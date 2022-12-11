<template>
    <NavBar></NavBar>
    <div class="body">
        <div class="info-area flex black ">

            <h3 class="font-setter tag-banner">
                <div style="display: inline-block;">
                    <TagdecVue></TagdecVue> &nbsp;
                </div>Tags
            </h3>
            <div class="slogan">
                <p class="font-setter">
                    Explore your interests by tags.
                    It can link similar articles together.
                    As well as original articles in a better way.
                </p>
            </div>
            <div class="tag-box">
                <el-input v-model="tagInputted" class="w-50 m-2" placeholder="Search your tag"/>
            </div>
            
        </div>
        <div class="main-area flex column">

            <div class="tag-grid grid ">
                <TagsArea></TagsArea>
            </div>
        </div>
    </div>
</template>
<script setup>
/////////////////////////////////////////////////
import TagsArea from '../components/TagsArea.vue'
import NavBar from '../components/NavBar.vue'
import TagdecVue from '../components/icons/Tagdec.vue'
import {ref} from 'vue'
/////////////////////////////////////////////////

</script>
<style scoped>
.slogan {

    margin-bottom: 0px;
}

.tag-banner {
    margin-top: 18px;
    margin-bottom: 18px;
}

.info-area {
    display: flex;
    flex-direction: column;
    width: 76%;
    margin: auto;
}

.font-setter {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.body {
    background-color: #F1EFEF;
}


.flex {
    display: flex;
}

.grid {
    display: grid;
}

.flex1 {
    flex: 1;
}

.column {
    flex-direction: column;
}

.tag-grid {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    grid-gap: 20px;
    place-items: center;
    margin: 20px;

}

.main-area {
    /* 在宽屏时候，总是占据78%的空间,剧中显示 */
    width: 80%;
    margin: auto;
    margin-top: 5px;
    margin-bottom: 20px;
    /*高度随滚动增加  */
    min-height: 100vh;

}

@media screen and (max-width: 1050px) {
    .main-area {
        width: 100%;
    }
}
</style>
