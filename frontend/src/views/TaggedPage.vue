<template>
   <NavBar></NavBar>
   <div class="body">
      <div class="banner-area">
         <div class="left-title">
            <!-- <TagPageBannerVue></TagPageBannerVue> -->
            <h3 class="font-setter"></h3>
         </div>

      </div>
      <div class="main-area flex">
         <div class="content-area flex3 mg-r8">
            <div class="up-down flex column">
               <div class="new-banner-area flex">
                  <div class="left-text-area flex column">
                     <div class="title-area">
                        <TagPageBannerVue></TagPageBannerVue>
                        {{ currentTagInfo.tag_name }}
                     </div>
                     <div class="des-area-inner">
                        {{ currentTagInfo.tag_description }}

                     </div>
                     <div class="follow-area">
                        <el-button size="large" type="info" @click="subFollow">Follow</el-button>
                     </div>
                  </div>
                  <div class="des-right-pic-area">
                     <KnowledgeMapVue></KnowledgeMapVue>
                  </div>
               </div>
               <hr>
               <TagArticleListBlock>/</TagArticleListBlock>
            </div>
         </div>

         <div class="recommend-area flex1 flex column mg-r8">
            <div class="tag-area black-border mg-b8">
               <div class="tag-title-area" style="display:inline-block">
                  <h5 class="font-setter tag-banner">Users Followed the tag</h5>
               </div>
               <hr>
               <div class="tags-area">
                  <div class="tag-inner-area">

                     <div class="single_user_info flex" v-for="(item, index) in followerList" :key="index">
                        &nbsp;&nbsp;
                        <Netrovue></Netrovue>
                        &nbsp;&nbsp;
                        <div class="user_name">{{ item.user_name }}</div>
                        
                        &nbsp;&nbsp;
                        <el-tag class="user_name_b">{{item.user_reg_time}}</el-tag>
                        <hr>
                     </div>
                     
                  </div>
                  
               </div>

            </div>
            <br>
            <br>
            <div class="tag-area black-border mg-b8">
               <div class="tags-area">
                  <div class="tag-inner-area">
                     <img class="small-img" src="../assets/cfp2.png">
                  </div>
                  <div class="tag-title-area-b" style="display:inline-block">
                     <router-link to="/post"><h5 class="font-setter tag-banner">Call For Post!</h5></router-link>
                  </div>
                  <hr>

               </div>

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
import { followTag, getUserTags } from '../http/api.js'
import { ref, reactive, onMounted } from 'vue'
import QuestionTagVue from '../components/icons/QuestionTag.vue';
import router from '../router';
import { getArticlesListByTag, getTagInfo, getUserActivity, getTagFollower } from '../http/api.js';
import TagArticleListBlock from '../components/TagArticleListBlock.vue';
import TagPageBannerVue from '../components/icons/TagPageBanner.vue';
import KnowledgeMapVue from '../components/icons/KnowledgeMap.vue';
import { ElMessage } from 'element-plus';
import GitAvatar from '../components/icons/GitAvatar.vue';
import Netrovue from '../components/icons/Netro.vue';
////////////////////////////////////////////////  



const currentTagInfo = reactive({
   tag_name: '',
   tag_description: '',
   tag_id: ''
})
// 拿到路由最后参数
//  vue 3 assests 下图片



const currentId = router.currentRoute.value.params.id

const currentIdData = reactive({
   params: {
      tag_id: currentId
   }

})


const followInfo = reactive({
   user_name: sessionStorage.getItem('user_name'),
   tag_id: currentId,
})

const followerList = reactive([

])

const subFollow = () => {
   followTag(followInfo).then(res => {
      console.log(res)
      ElMessage.success('Follow Success!')
      // 0.5s后刷新页面
      setTimeout(() => {
         window.location.reload()
      }, 500)
   }).catch(err => {
      console.log(err)
      ElMessage.error('You have followed this tag!')
   })

}

getTagFollower(currentIdData).then(res => {
      followerList.push(...res.data.followers)
      console.log(followerList)
   })

onMounted(() => {
   getTagInfo(currentIdData).then(res => {
      currentTagInfo.tag_name = res.data.tag_info.tag_name
      currentTagInfo.tag_description = res.data.tag_info.tag_description
      currentTagInfo.tag_id = res.data.tag_info.tag_id
   })



})




////////////////////////////////////////////////
</script>
<style scoped>
.user_name{
   width: 60px;
   /* 超出的部分省略号 */
   overflow: hidden;
   text-overflow: ellipsis;
   white-space: nowrap;
   height: 50px;
   padding-top: 5px;
}

.user_name_b{
   margin-top: 10px;
   padding-top:10px;
   padding-bottom: 10px;
}
.single_user_info {
   width: 100%;
   flex-direction: row;
}

.small-img {
   width: 100%;
   height: 100%;
   display: block;
}

.des-right-pic-area {
   margin-top: 6%;
}

.left-text-area {
   padding: 15px;
   padding-bottom: 0px;
   width: 70%;
}

.follow-area {

   margin-left: 10px;
}

.des-area-inner {
   /* 不能超过四排 */

   overflow: hidden;
   text-overflow: ellipsis;
   display: -webkit-box;
   -webkit-line-clamp: 3;
   -webkit-box-orient: vertical;
   font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
   width: 60%;
   font-size: 17px;
   margin-left: 10px;
   border: 0.5px solid #9E8ACF dashed;
   padding: 5px;
   margin-bottom: 10px;
   border-radius: 3px;

}

.title-area {
   font-size: 30px;
   margin-bottom: 10px;
   min-height: 40px;
   font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
   margin-left: 10px;
}

.new-banner-area {
   min-height: 150px;

}

.tag-inner-area {
   padding: 8px;
   display: flex;
   flex-wrap: wrap;
   place-content: center;
   flex-direction: column;
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
   min-height: 160px;
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
   display: flex;
   min-height: 20px;
   padding-top: 20px;
   margin-left: 10%;
   background-color: rgb(241, 239, 239);
   width: 60%;
}

.left-title {
   display: flex !important;
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
   margin-bottom: 10px;
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
   .content-area{
      width: 99.25%;

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
      margin-bottom: 20px;
   }

   .article-block {
      /* height: 90px; */
      height: 90px;
      word-wrap: break-word;
      max-width: 100vw;

   }
}
</style>