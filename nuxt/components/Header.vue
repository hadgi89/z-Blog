<template>
    <div class="container">
        <div class="h-logo">
            <el-link>
                <el-image style="height: 40px" src="logo9.png"></el-image>
            </el-link>
            
        </div>
        <div class="h-nav">
            
            <el-menu
            :default-active="activeIndex"
            class="el-menu-demo"
            mode="horizontal"
            @select="handleSelect"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b">
                <el-menu-item index="2">ГЛАВНАЯ</el-menu-item>
                <el-menu-item index="3">СТАТЬИ</el-menu-item>
                <el-menu-item index="4">ХАБЫ</el-menu-item>
                <el-menu-item index="5">АВТОРЫ</el-menu-item>
            </el-menu>
        </div>
        
        <div class='h-menu'>
            <el-link class="search-link" :underline="false" icon="el-icon-search">
                <!-- <i class="el-icon-search"></i> -->
            </el-link>
             
             
           
            <el-dropdown trigger="click">
                <el-link class="el-dropdown-link" :underline="false" icon="el-icon-user"></el-link>
                <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item>
                        <el-button plain>Войти</el-button>
                        <el-button type="info">Регистрация</el-button>
                    </el-dropdown-item>
                    <el-dropdown-item icon="el-icon-circle-plus">Как стать автором</el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown>
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
        grid-template-columns: 50px auto 100px;
        gap: 20px;
        align-items: center;
    }

    .h-nav {
        justify-self : start;
    }
    
    .h-menu {
        display: inline-flex;
        justify-self : end;
        align-items: center;
        /* justify-content: center; */
        /* align-content : center; */
        /* text-align: center; */
    }


    .search-link {
        font-size: 24px;
        color: #fff;
        /* align-self : center; */
        margin-right: 15px;
    }

    .search-link:hover {
        color: #ffd04b;
    }

    .el-dropdown-link {
        font-size: 24px;
        color: #fff;
        /* align-self : center; */
    }

    .el-dropdown-link:hover {
        color: #ffd04b;
        /* cursor: pointer; */
    }

    .el-dropdown-menu__item:hover {
        background-color: transparent;
    }
        
</style>