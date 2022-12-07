<template>
    <NavBar></NavBar>
<div class="main-area flex column">

    <div class="info-area flex black " style="height: 100px;">
    </div>
        <div class="tag-grid grid ">
            <SingleTag></SingleTag>
            <SingleTag></SingleTag>
            <SingleTag></SingleTag>
            <SingleTag></SingleTag>
            <SingleTag></SingleTag>
            <SingleTag></SingleTag>
            <SingleTag></SingleTag>
            <SingleTag></SingleTag>
            <SingleTag></SingleTag>
    </div>
</div>
</template>
<script setup>
import SingleTag from '../components/SingleTag.vue'
import NavBar from '../components/NavBar.vue'

// 当窗口
</script>
<style scoped>

.black{
    /* border: 1px solid black; */
    /* 很浅的阴影 */
    box-shadow: 0 0 5px rgba(0,0,0,0.1);
}
.flex {
    display: flex;
}
.grid{
    display: grid;
}
.flex1 {
    flex: 1;
}

.column {
    flex-direction: column;
}

.tag-grid{
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    grid-gap: 20px;
	place-items: center;
    margin: 20px;

}

.main-area {
    /* 在宽屏时候，总是占据78%的空间,剧中显示 */
    width: 80%;
    margin: auto;
    margin-top: 20px;
    margin-bottom: 20px;
    /*高度随滚动增加  */
    min-height: 100vh;

}

@media screen and (max-width: 1250px) {
    .main-area {
        width: 100%;
    }
}
</style>
