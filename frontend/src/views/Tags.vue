<template>
    <NavBar></NavBar>
    <div class="body">
        <div class="info-area">

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
            <div class="search-add-area flex">
                <div class="add">
                    <el-button @click="dialogVisible = true"><AddTagVue></AddTagVue>Add a new tag</el-button>
                </div>
            </div>
        </div>
        <div class="main-area flex column">

            <div class="tag-grid grid ">
                <TagsArea></TagsArea>
            </div>
        </div>
    </div>
<el-dialog
    v-model="dialogVisible"
    title="Add a new tag"
    width="40%"
  >
  <div style="display: flex;flex-direction: column;">
                <span class="font-setter">
                    <h6>Tag name</h6>
                </span>
                <el-input v-model="newTagPair.tag_name" 
                  placeholder="Please input tag name" />
                <br>
                <span class="font-setter">
                    <h6>Tag Description</h6>
                </span>
                <el-input  type="textarea" v-model="newTagPair.tag_description" 
               placeholder="Please input tag description"  />
            </div>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click = "subTagAdded">
          Confirm
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>
<script setup>
/////////////////////////////////////////////////
import TagsArea from '../components/TagsArea.vue'
import NavBar from '../components/NavBar.vue'
import TagdecVue from '../components/icons/Tagdec.vue'
import {ref,reactive} from 'vue'
import AddTagVue from '../components/icons/AddTag.vue'
import {addNewTag} from '../http/api.js'
import { ElMessage } from 'element-plus'
/////////////////////////////////////////////////
let dialogVisible = ref(false)

const subTagAdded = () => {
    dialogVisible.value = false
    addNewTag(newTagPair).then(res => {
        console.log(res)
        // refresh the page
        window.location.reload()
    }).catch(err => {
        ElMessage.error('Failed to add a new tag due to the name conflict.')
        console.log(err)
    })
}
const newTagPair = reactive({
    tag_name: '',
    tag_description: ''
})


</script>
<style scoped>

.tag-box{
    width: 50%;
    margin-right: 5px;
}
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
    /*高度随滚动增加  */
    min-height: 100vh;

}

@media screen and (max-width: 1050px) {
    .main-area {
        width: 100%;
    }
}
</style>
