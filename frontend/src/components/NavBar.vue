<template>
  <!-- Component -->
  <div class="navbar-component">
    <!-- Class `area` is a container -->
    <div class="navbar area">
      <!-- Logo -->
      <router-link to="/"><img class="small-img" src="../assets/canary_banner.jpg"></router-link>
      <!-- List of links -->
      <nav role="navigation" id="navigation" class="list">
        <!-- <span class="item"><i class="fa fa-search"></i></span> -->
        <button class='search-button-container' @click="dialogVisible = true">
          <span class="search-icon-container inline">
            <SearchIcon></SearchIcon>
            <h5 class="inline font-setter margin-search">Search</h5>
          </span>
          <span class="little-box">
            <div class="kb">⌘</div>
            <div class="kb">J</div>
          </span>
        </button>
        
        <router-link to="/" class="item -link margin-bottom">Home</router-link>
        <router-link to="/tags" class="item -link margin-bottom">Tags</router-link>

        <router-link to="/post" class="item -link">
          <el-button color="#626aef" style="margin-bottom:5px;background-color: #545DF2;">Post</el-button>
        </router-link>
        


        <router-link to="/user/userpage" class="margin-left">
          <el-avatar :size="35" :src="circleUrl" :key="circleUrl" id="avatar-image"
           style="margin-top: 10px;"/>
        </router-link>
      </nav>
      <!-- Button to toggle the display menu  -->
      <button data-collapse data-target="#navigation" class="toggle">
        <!-- Hamburger icon -->
        <span class="icon"></span>
      </button>
    </div>
  </div>

  <el-dialog v-model="dialogVisible" title="Mixed Search" :width="dialogWidthComputed" draggable
    style="background-color:#FAFAFA; " class="search-dialog">
    <center>
      <h5>
        <p class="font-setter-normal">Search</p>
      </h5>
    </center>
    <el-input v-model="searchText" class="search-bar" placeholder="Search around the site" type="search" />
    <el-button :inline="true" @click="subSearchContent">search</el-button>
    <div style="overflow: scroll;max-height: 300px;">
      <div v-if="searchResList.length != 0">
        <div class="search-res" v-for="(item, index) in searchResList" :key="index">
          <div shadow="always" class="res-card" @click="router.push({ name: 'article', params: { id: item.article_id} })" >

            <h6 class="font-setter-d">{{ item.article_name }}</h6>
            <center>
              <div class="author-area" type="success">
                <el-tag type="success">{{ item.article_author }}</el-tag>
              </div>
            </center>
            <div class="tag-area">
              <div class="" v-for="(it, index) in item.article_tags" :key="index">
                <center>
                  <el-tag >{{ it.tag_name }}</el-tag>
                  &nbsp;
                </center>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>

    <div v-if="searchResList.length == 0">
      <div class="flex-area" style="display: flex;">
        <img src="../assets/mf-trans.webp" class="small-img-search">
        <div class="indicate-group">
          <h5 class="font-setter-b" style="display: inline-block;">Aggregate Search</h5>
          <center>
            <h6 class="font-setter no-id">no content yet</h6>
          </center>
        </div>
      </div>
    </div>
    <div class="footer dialog-footer">
      <div class="kb_inner">⌘</div>
      <div class="kb_inner">J</div>
      <span class="fter-instruct-open font-setter-normal">To toggle</span>
      <div class="kb_inner">ESC</div>
      <span class="fter-instruct font-setter-normal">to quit</span>
    </div>
  </el-dialog>
</template>
<script setup>
//////////////////////////////////////////////////////
import GithubIcon from './icons/GithubIcon.vue'
import SearchIcon from './icons/SearchIcon.vue'
import router from '../router/index.js'
import { ref, onMounted, reactive } from 'vue'
import { searchCon } from '../http/api'
import axios from 'axios'
//////////////////////////////////////////////////////

const dialogVisible = ref(false);
const circleUrl = ref('')
const dialogWidthComputed = ref('55%');

// 按下command+j toggle search dialog
document.addEventListener('keydown', (e) => {
  if (e.key === 'j' && e.metaKey) {
    dialogVisible.value = !dialogVisible.value;
  }
});

let searchResList = reactive([]);



onMounted(() => {

  if (window.innerWidth <= 800) {
    dialogWidthComputed.value = '80%';
  } else if (window.innerWidth > 800) {
    dialogWidthComputed.value = '55%';
  }


  window.onresize = () => {
    if (window.innerWidth <= 800) {
      dialogWidthComputed.value = '80%';
    } else if (window.innerWidth > 800) {
      dialogWidthComputed.value = '55%';
    }
  }
})

let searchText = ref('');

const searchContent = reactive({
  params: {
    search_content: searchText
  }
});

const subSearchContent = () => {
  // ensure the input is less than 200 words
  if(searchText.value.length > 200){
    Elmessage('Search content should be less than 200 words')
    return
  }
  searchCon(searchContent).then(res => {
    console.log(res.data)
    searchResList = res.data.article
    console.log(searchResList)
    // 刷新对话框内容
    dialogVisible.value = false;
    setTimeout(() => {
      dialogVisible.value = true;
    }, 1);

  })
}

const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
  timeout: 1000,
  responseType: 'blob'
});

instance.interceptors.request.use(function (config) {
  config.headers.Authorization = localStorage.getItem('access_token')
  return config;
}, function (error) {
  return Promise.reject(error);
});


const getUserByLocalOrSession = () => {
  if (sessionStorage.getItem('user_name') != null) {
    return sessionStorage.getItem('user_name')
  } else if (localStorage.getItem('user_name') != null) {
    return localStorage.getItem('user_name')
  } 
}

instance.get('api/find/avatar', {
    params: {
      // username: sessionStorage.getItem('user_name')
      username: getUserByLocalOrSession()
    }
  }).then((res) => {
    console.log(res)
    let blob = new Blob([res.data], { type: 'image/png' })
    let url = window.URL.createObjectURL(blob)
    circleUrl.value = url
  }).catch((err) => {
    console.log(err)

  });



//////////////////////////////////////////////////////
(function () {

  // Definition of caller element
  var getTriggerElement = function (el) {
    var isCollapse = el.getAttribute('data-collapse');
    if (isCollapse !== null) {
      return el;
    } else {
      var isParentCollapse = el.parentElement.getAttribute('data-collapse');
      return (isParentCollapse !== null) ? el.parentElement : undefined;
    }
    return el;
  };

  // A handler for click on toggle button
  var collapseClickHandler = function (event) {

    var triggerEl = getTriggerElement(event.target);
    // If trigger element does not exist
    if (triggerEl === undefined) {
      event.preventDefault();
      return false;
    }

    // If the target element exists
    var targetEl = document.querySelector(triggerEl.getAttribute('data-target'));
    if (targetEl) {
      triggerEl.classList.toggle('-active');
      targetEl.classList.toggle('-on');
    }
  };

  // Delegated event

  
  document.addEventListener('click', collapseClickHandler, false);

})(document, window);

// 上面的代码在跳转页面后就失效了，所以每次跳转都重新绑定
router.afterEach((to, from) => {
  (function () {

    // Definition of caller element
    var getTriggerElement = function (el) {
      var isCollapse = el.getAttribute('data-collapse');
      if (isCollapse !== null) {
        return el;
      } else {
        var isParentCollapse = el.parentElement.getAttribute('data-collapse');
        return (isParentCollapse !== null) ? el.parentElement : undefined;
      }
      return el;
    };

    // A handler for click on toggle button
    var collapseClickHandler = function (event) {

      var triggerEl = getTriggerElement(event.target);
      // If trigger element does not exist
      if (triggerEl === undefined) {
        event.preventDefault();
        return false;
      }

      // If the target element exists
      var targetEl = document.querySelector(triggerEl.getAttribute('data-target'));
      if (targetEl) {
        triggerEl.classList.toggle('-active');
        targetEl.classList.toggle('-on');
      }
    };

    // Delegated event

    
    document.addEventListener('click', collapseClickHandler, false);

  })(document, window);
})



</script>
<style lang="less" scoped>
// Scaffolding
*,
*:before,
*:after {
  box-sizing: border-box;
}

body {
  background-color: #f5f5f5;
  color: #333;
  font-size: 14px;
  line-height: 20px;
}

a {
  text-decoration: none;
  transition: all 0.3s linear 0s;
}

.area {
  display: flex;
  flex-flow: row wrap;
  align-items: stretch;
  margin-left: auto;
  margin-right: auto;

  @media (min-width: 768px) {
    width: 750px;
  }

  @media (min-width: 992px) {
    width: 970px;
  }

  @media (min-width: 1200px) {
    width: 1140px;
  }
}
.tag-area{
  display: flex;
  // 每行最多2个
  flex-wrap: wrap;
  margin-top: 25px;
  flex-direction: column;
    
  }
  

// Navigation component
// ----------

// Variables
@navbar-height: 64px;
@navbar-background: #fff;
@navbar-border: #ddd;

@navbar-collapse-breakpoint: 768px;

@navbar-item-font-size: 14px;
@navbar-item-border-width: 4px;
@navbar-item-color: #555;
@navbar-item-active-color: #333;
@navbar-item-border: transparent;
@navbar-item-active-border: #673ab7;

.res-card {
  margin-top: 10px;
  height: 70px;
  display: flex;
  margin-bottom: 10px;
  overflow: scroll;
}

.res-title {
  display: flex;
}

.res-card:hover {
  background-color: rgb(165, 165, 231);
}

.author-area {
  margin-right: 40px;
  margin-top: 27px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.fter-instruct {
  position: relative;
  top: 5px;
  left: 5px;
}

.search-res {
  // 四周阴影
  cursor: pointer;
  box-shadow: 0 0 2px rgba(0, 0, 0, 0.2);
  margin-left: 5%;
  width: 90%;
  padding: 0px;
}

.fter-instruct-open {
  position: relative;
  top: 5px;
  left: 4px;
}

.indicate-group {
  display: flex;
  flex-direction: column;
}

.dialog-footer {
  background-color: rgb(234, 233, 233);
  // 位于最底部
  position: absolute;
  // 左对齐
  left: 0;
  bottom: -2px;
  height: 30px;
  width: 100%;
}


.white-banner {
  background-color: #FAFAFA;
  height: 10px;
  width: 100%;
}

.margin-left {
  margin-left: 10px;
  margin-right: 10px;

}

.search-button-container {
  align-items: center;
  background: #efecec;
  border: 0;
  border-radius: 40px;
  color: #000;
  cursor: pointer;
  display: flex;
  font-weight: 500;
  height: 36px;
  justify-content: space-between;
  margin: 0 0 0 16px;
  padding: 0 8px;
  user-select: none;
  margin-right: 20px;
  ;
  margin-top: 6px;
}

.search-button-container:hover {
  background-color: #f5f5f5;
  border: 2px solid #673ab7;

}

.kb {
  align-items: center;
  background: #f5f5f5;
  border-radius: 3px;
  box-shadow: 0 3px 3px rgba(0, 0, 0, 0.2);
  // color:var(--docsearch-muted-color);
  margin: 2px;
  color: #555;
  display: flex;
  height: 21px;
  justify-content: center;
  position: relative;
  border: 0;
  top: -1px;
  width: 20px;
  font-family: monospace, monospace;
  font-size: 1em;
  border: 10px;
  display: inline-block;
}

.kb_inner {
  background: #f5f5f5;
  border-radius: 3px;
  box-shadow: 0 3px 3px rgb(0 0 0 / 20%);
  margin: 5px;
  color: #555;
  display: flex;
  justify-content: center;
  position: relative;
  top: 3px;
  left: 5px;
  border: 0;
  padding: 3px;
  font-family: monospace, monospace;
  font-size: 1em;
  border: 10px;
  display: inline;
  width: 20px;
  align-items: center;
}

.font-setter {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: small;
  color: #626262;
}

.font-setter-normal {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #626262;
}

.margin-search {
  margin: 5px;
}

.inline {
  display: inline-block;
}

.tags-area {

  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}

// Component skeleton
.navbar-component {
  // 永远在顶部
  position: sticky;
  top: 0;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1), 0 2px 1px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(10px);
  // 支持Safari
  -webkit-backdrop-filter: blur(10px);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  z-index: 10;


  &>.navbar {
    justify-content: space-between;

    // the box bottom a shadow
    box-shadow: none;
  }
}

.small-img-search {
  margin-top: 20px;
  width: 60px;
  height: 60px;
  display: inline-block;
  margin-bottom: 20px;
  margin-left: 15%;
}

.small-img {
  width: 131px;
  height: 44px;
}

.font-setter-d {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  margin-top: 25px;
  width: 30%;
  margin-left: 3%;
  margin-right: 8%;
  min-width: 95px;
  // // 横向超出的部分省略号
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.font-setter-b {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  margin-top: 25px;
  width: 100%;
  margin-left: 20%;
}

.flex-area {
  width: 60%;
  margin-left: 20%;
  display: flex;
}

// Component
.navbar {

  // Brand
  // &>.brand {
  //   display: block;
  //   font-size: 16px;
  //   color: #777;
  //   margin: round(((@navbar-height - 20)/2), 2); //左右没 
  // }

  // Toggle button
  &>.toggle {
    border: 0;
    background-color: transparent;
    outline: none;
    border: 0;
    display: inline-block;
    background-color: transparent;
    background-image: none;
    vertical-align: middle;
    text-align: center;
    white-space: nowrap;
    cursor: pointer;
    touch-action: manipulation;
    user-select: none;
    padding: round(((@navbar-height - 20/2)/2), 2);

    @media (min-width: 768px) {
      display: none;
    }

  }

  &>.toggle>.icon {
    position: relative;
    margin-top: 8px;
    margin-bottom: 8px;

    &,
    &:before,
    &:after {
      display: block;
      width: 24px;
      height: 3px;
      transition: background-color 0.3s linear, transform 0.3s linear;
      background-color: #555555;
    }

    &:before,
    &:after {
      position: absolute;
      content: "";
    }

    &:before {
      top: -8px;
    }

    &:after {
      top: 8px;
    }
  }

  &>.toggle.-active>.icon {
    background-color: transparent;

    &:before {
      transform: translateY(8px) rotate(45deg);
    }

    &:after {
      transform: translateY(-8px) rotate(-45deg);
    }
  }

  // List of items
  &>.list {

    display: none;
    flex-flow: row nowrap;
    align-items: center;
    white-space: nowrap;

    @media (min-width: @navbar-collapse-breakpoint) {
      display: flex;
    }

    @media (max-width: 750px) {
      position: fixed;
      top: @navbar-height+30px;
      left: 1vw;
      width: 98%;
      // backdrop-filter: blur(10px);
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.16), 0 2px 10px rgba(0, 0, 0, 0.12);
      overflow-y: hidden;
      overflow-x: auto;
      border-top: 1px solid @navbar-border;
      background-color: white;
      z-index: 11;
      flex-direction: column;
      padding-bottom: 10px;
    }

    &.-on {
      display: flex;
      z-index: 11;
    }
  }

  &>.list>.item {
    display: block;
    flex-shrink: 0;
    height: @navbar-height;
    line-height: @navbar-height;
    padding-left: round(((@navbar-height - 20)/2), 2);
    padding-right: round(((@navbar-height - 20)/2), 2);
    color: @navbar-item-color;
    font-size: 16px;
  }

  &>.list>.item.-link {
    line-height: @navbar-height + @navbar-item-border-width;
    color: @navbar-item-color;
    border-bottom: @navbar-item-border-width solid @navbar-item-border;

    &.-active,
    &:hover,
    &:focus {
      color: @navbar-item-active-color;
      border-bottom-color: @navbar-item-active-border;
    }
  }
}

.search-dialog {
  border-radius: 0px;
}

.search-bar {
  width: 60%;
  margin-left: 16%;
  margin-right: 2%;
}
</style>