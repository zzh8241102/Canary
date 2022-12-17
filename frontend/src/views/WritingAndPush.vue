<template>
    <NavBar></NavBar>
    <div class="body">
        <div class="text-banner font-setter ">
            <PostIconVue></PostIconVue>
            &nbsp;&nbsp;
            <h3>Post your Piazzas</h3>
        </div>
        <div class="title-group">
            <el-input v-model="articleTitle" placeholder="Please input Your Title Here" class="title-input"
                :inline="true" />
            <el-button round id="post-button" :inline="true" @click="postArticleInter">Post</el-button>
        </div>
        <div class="tag-selector">
            <!-- <TagSelector></TagSelector> -->
            <el-select v-model="tag_selected" multiple placeholder="Select" style="width: 300px" @change="getSelectedTags">
                <el-option v-for="item in tag_options" :value="item.tag_name" :label="item.tag_name" :key="item.tag_name" />
            </el-select>
        </div>
        <div class="editor">
            <v-md-editor v-model="markDownContent" height="500px"></v-md-editor>
        </div>
    </div>
</template>
<script setup>

/////////////////////////////////////////////
import PostIconVue from '../components/icons/PostIcon.vue';
import { ref,reactive,onMounted } from 'vue'
import NavBar from '../components/NavBar.vue'
import TagSelector from '../components/TagSelector.vue';
import { getTags,postArticle } from '../http/api';
import router from '../router';

/////////////////////////////////////////////
const articleTitle = ref('')
const markDownContent = ref('')

const tag_selected = ref('')

let tag_options = reactive([{"tag_name": "test", "tag_description": "test"}])

onMounted(() => {  
  getTags().then((res) => {
    tag_options = res.data.tags
  }).catch((err) => {
    console.log(err)
  })
  
})

const getSelectedTags = (item) => {
  console.log(item)
  return item
}

const article_info = reactive({
    title: '',
    content: '',
    tags:[],
    author: ''
})

const getUserByLocalOrSession = () => {
  if (sessionStorage.getItem('user_name') != null) {
    return sessionStorage.getItem('user_name')
  } else if (localStorage.getItem('user_name') != null) {
    return localStorage.getItem('user_name')
  } 
}

const postArticleInter = () => {
    
    article_info.title = articleTitle.value
    article_info.content = markDownContent.value
    article_info.tags = tag_selected.value
 
    // convert the tags to object
    
        
    
    article_info.author = getUserByLocalOrSession()
    
    console.log(article_info)
    
    postArticle(article_info).then((res) => {
        console.log(res)
        // 0.3s jump to home page
        // router.push({path: '/'})
        
        
            ElNotification({
                title: 'Success',
                message: 'Your article is posted successfully',
                type: 'success'
            })
        
        // redirect to the article page
        // router.push({path: '/article/' + res.data.article_id})
        // redirect to the home page after 0.8s
        // clear the input
        articleTitle.value = ''
        markDownContent.value = ''
        tag_selected.value = ''
        
    }).catch((err) => {
        console.log(err)
    })
}


/////////////////////////
</script>
<style scoped>
.text-banner{
    display: flex;
    flex-direction: row;
    width: 50%;
    background-color: #F1EFEF;
    margin-left:15%;
    padding-top: 20px;
    margin-bottom: 0px;
    padding-bottom: 0px;
}
.body {
    background-color: #F1EFEF;
    height: 100vh;
}

.font-setter{
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
}

.title-group {
    position: relative;
    top: 15px;
    left: 20vw;
    display: flex;
    flex-direction: row;
    align-items: center;
    margin: 0 0 1rem 0;
    margin-bottom: 40px;
}

.tag-selector {
    position: relative;
    left: 20vw;
    display: flex;
    flex-direction: row;
    align-items: center;
}

.title-input {
    margin-right: 5px;
    width: 63vw;
}

.editor {
    margin: 15px;
    margin-bottom: 0px;

}

/* 当超宽屏时候 */
@media screen and (min-width: 1200px) {
    .editor {
        margin-left: 15vw;
        margin-right: 15vw;
    }

    .title-group {
        left: 15vw;
        width: 70vw;
    }

    .tag-selector {
        left: 15vw;
    }
}
</style>