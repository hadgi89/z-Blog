<template>
    <div class="container">
        <!-- <div class="h-logo">
            <el-image
            style="height: 40px"
            src="logo9.png"
            ></el-image>
        </div> -->
        <div class="h-nav">
            <el-menu
            :default-active="activeIndex"
            class="el-menu-demo"
            mode="horizontal"
            @select="handleSelect"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b">
                <el-menu-item index="1" class="logo">
                    <el-image
                    style="width: 40px; height: 40px"
                    src="logo9.png"
                    ></el-image>
                </el-menu-item>
                <el-menu-item index="2">ГЛАВНАЯ</el-menu-item>
                <el-menu-item index="3">ГЛАВНАЯ</el-menu-item>
                <el-menu-item index="4">СТАТЬИ</el-menu-item>
                <el-menu-item index="5">ХАБЫ</el-menu-item>
                <el-menu-item index="6">АВТОРЫ</el-menu-item>
            </el-menu>
        </div>
        
        <div class='h-menu'>
            <el-avatar 
            size="large" 
            src="https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png">
            </el-avatar>
        </div>
    </div>


</template>

<script>
export default {
    name: "Header",
    data() {
        return {
            q : null,
            activeIndex: '2',
    };
    },
    methods: {
    handleSelect(key, keyPath) {
        console.log(key, keyPath);
    }
    }
}
</script>

<style scoped>
    .container {
        display: grid;
        grid-template-columns: auto 100px;
        gap: 20px;
        align-items: center;
    }

    .h-nav {
        justify-self : start;
    }
    
    .h-menu {
        justify-self : end;
    }

    .logo .is-active {
        color: transparent;
        background-color: transparent;
        border: none;
    }

</style>