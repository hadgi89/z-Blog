<template>
  
  <div class="header-wrapper">
    
    <div class="h-logo">
      <nuxt-link to="/">
        <el-image style="height: 40px" src="logo9.png"></el-image>
      </nuxt-link>
    </div>
    
    <div class="h-navbar">
      <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
        <el-menu-item index="2">
          <nuxt-link to="/">ГЛАВНАЯ</nuxt-link>
        </el-menu-item>
        <el-menu-item index="3">
          <nuxt-link to="/posts">СТАТЬИ</nuxt-link>
        </el-menu-item>
        <el-menu-item index="4">
          <nuxt-link to="/habs">ХАБЫ</nuxt-link>
        </el-menu-item>
        <el-menu-item index="5">
          <nuxt-link to="/users">АВТОРЫ</nuxt-link>
        </el-menu-item>
      </el-menu>
    </div>
        
    <div class='h-usermenu'>
      <!-- <el-form :inline="true" size="mini">
        <el-form-item>
          <el-input placeholder="Найти... "></el-input>
        </el-form-item>
        <el-form-item>
          <nuxt-link class="search-link" to="/search">
        <i class="el-icon-search"></i>
      </nuxt-link>
        </el-form-item>
      </el-form> -->
      <el-input
        class="inp"
        placeholder="Поиск..."
        suffix-icon="el-icon-search"
        size="medium"
        v-model="input1">
      </el-input>
      
      <!-- <nuxt-link class="search-link" to="/search">
        <i class="el-icon-search"></i>
      </nuxt-link> -->
      
      <nuxt-link class='signin-link' to="/signin">Sign in</nuxt-link>
      
      <nuxt-link class='signup-link' to="/signup">Sign up</nuxt-link>
      
      <el-dropdown trigger="click">
        <span class="el-dropdown-link">
          <i class="el-icon-user"></i>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>
            <i class="el-icon-user"></i>
            <nuxt-link to="/prifile">Профиль</nuxt-link>
          </el-dropdown-item>
          <el-dropdown-item>
            <i class="el-icon-setting"></i>
            <nuxt-link to="/settings">Настройки</nuxt-link>
          </el-dropdown-item>
          <el-dropdown-item>
            <i class="el-icon-help"></i>
            <nuxt-link to="/support">Поддержка</nuxt-link>
          </el-dropdown-item>
          <el-dropdown-item>
            <i class="el-icon-turn-off"></i>
            <nuxt-link to="/logout">Выйти</nuxt-link>
          </el-dropdown-item>
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
        input1: '',
      }
    }
  }
</script>


<style scoped>
  .header-wrapper {
    display: grid;
    grid-template-columns: 50px auto auto;
    gap: 20px;
    background-color: rgb(175, 111, 235);
    height: 100%;
    align-items: center;
  }

  .h-logo {
    background-color: #e7c451;
    display: flex;
    justify-content: center;

  }
  .h-navbar {
    background-color: rgb(128, 201, 121);
  }

  .h-usermenu {
    background-color: rgb(83, 185, 185);
    display: inline-flex;
    justify-self : end;
    align-items: center;
  }

  .search-link {
    font-size: 24px;
    color: #fff;
    margin-right: 15px;
  }

  .search-link:hover {
    color: #ffd04b;
  }

  .signup-link {
    white-space: nowrap;
    color: #fff;
    border: solid 1px #fff;
    border-radius: 3px;
    padding-bottom: 3px;
    padding-inline: 10px;
    margin-right: 12px;
  }

  .signup-link:hover {
    color: #ffd04b;
    border-color: #ffd04b;
  }


  .signin-link {
    white-space: nowrap;
    color: #fff;
    padding-bottom: 3px;
    padding-inline: 10px;
    margin-right: 12px;
  }

  .signin-link:hover {
    color: #ffd04b;
  }

  .el-dropdown-link {
    font-size: 24px;
    color: #fff;
  }
  
  .el-dropdown-link:hover {
    color: #ffd04b;
  }

  .el-dropdown-menu__item {
    font-size: 14px;
    font-weight: 500;
  }

  .el-dropdown-menu__item i {
    font-size: 18px;
    font-weight: 500;
    margin-right: 10px;
  }

  .el-dropdown-menu__item:hover {
    background-color: #545c64;
    color: #ffd04b;
  }

  .el-form {
    background-color: #ffd04b;
    
  }

  .el-input {
    margin-right: 12px;
  }

  .el-input__inner:focus {
    border: solid 1px #ffd04b !important;
  }
</style>