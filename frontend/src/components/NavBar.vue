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
        <router-link to="/tags" class="item -link margin-bottom">tags</router-link>
        
          <router-link to="/post" class="item -link" ><el-button color="#626aef" style="margin-bottom:5px">Post</el-button></router-link>


        <router-link to="/user/userpage" class="margin-left">
          <GithubIcon></GithubIcon>
        </router-link>
      </nav>
      <!-- Button to toggle the display menu  -->
      <button data-collapse data-target="#navigation" class="toggle">
        <!-- Hamburger icon -->
        <span class="icon"></span>
      </button>
    </div>
  </div>

  <el-dialog v-model="dialogVisible" title="Mixed Search" :width="dialogWidthComputed" draggable style="background-color:#FAFAFA; "
    class="search-dialog">
    <center>
      <h5>
        <p class="font-setter-normal">Search</p>
      </h5>
    </center>
    <el-input v-model="searchContent" class="w-80 m-2" placeholder="Search around the site"/>
    <el-card shadow="always" class="res-card" style="margin:8px;"> Result </el-card>
    <el-card shadow="always" class="res-card" style="margin:8px;"> Result </el-card>
    <el-card shadow="always" class="res-card" style="margin:8px;"> Result </el-card>

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
import { ref,onMounted} from 'vue'
//////////////////////////////////////////////////////

const id = ref(0);
const dialogVisible = ref(false);
const searchContent = ref('');
const dialogWidthComputed = ref('55%');

// 按下command+j toggle search dialog
document.addEventListener('keydown', (e) => {
  if (e.key === 'j' && e.metaKey) {
    dialogVisible.value = !dialogVisible.value;
  }
});


onMounted(() => {

  if(window.innerWidth <= 800){
      dialogWidthComputed.value = '80%';
  } else if(window.innerWidth>800){
      dialogWidthComputed.value = '55%';
  }


  window.onresize = () =>{
    if(window.innerWidth <= 800){
      dialogWidthComputed.value = '80%';
  } else if(window.innerWidth>800){
      dialogWidthComputed.value = '55%';
  }
  }  
}),

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
  margin: 8px;
}

.res-card:hover {
  background-color: rgb(165, 165, 231);
}

.fter-instruct {
  position: relative;
  top: 5px;
  left: 5px;
}

.fter-instruct-open {
  position: relative;
  top: 5px;
  left: 4px;
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



.small-img {
  width: 131px;
  height: 44px;
}

// Component
.navbar {

  // Brand
  &>.brand {
    display: block;
    font-size: 16px;
    color: #777;
    margin: round(((@navbar-height - 20)/2), 2); //左右没 
  }

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

    @media (min-width: @navbar-collapse-breakpoint) {
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

    @media (max-width: @navbar-collapse-breakpoint) {
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
      z-index:11;
      flex-direction: column;
    }

    &.-on {
      display: flex;
      z-index:11;
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
</style>