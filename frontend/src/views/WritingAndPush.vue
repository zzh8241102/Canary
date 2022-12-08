<template>
        <NavBar></NavBar>
        <div class="title-group">
            <el-input v-model="articleTitle" placeholder="Please input Your Title Here" class="title-input"
                :inline="true" />
            <el-button round id="post-button" :inline="true">Post</el-button>
        </div>
        <div class="editor">
            <v-md-editor v-model="markDownContent" height="500px"></v-md-editor>
        </div>
</template>
<script setup>
import { ref } from 'vue'
import NavBar from '../components/NavBar.vue'
const articleTitle = ref('')
const markDownContent = ref('')
</script>
<style scoped>
.title-group {
    position: relative;
    top: 30px;
    left: 20vw;
    display: flex;
    flex-direction: row;
    align-items: center;
    margin: 0 0 1rem 0;
    margin-bottom: 80px;
}

.title-input {
    margin-right: 5px;
    width: 63vw;
}

.editor {
    margin: 15px;
}
/* 当超宽屏时候 */
@media screen and (min-width: 1400px) {
    .editor {
        margin-left: 15vw;
        margin-right: 15vw;
    }
    .title-group {
        left: 15vw;
        width: 70vw;
    }
}
</style>