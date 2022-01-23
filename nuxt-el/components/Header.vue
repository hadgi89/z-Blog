<template>
  <div class="header-wrapper">
    <div class="h-logo">
      <nuxt-link to="/">
        <el-image style="height: 70px" src="logo8.png"></el-image>
      </nuxt-link>
    </div>
    
    <div class="h-navbar">
      <el-menu
      default-active="2"
      mode="horizontal"
      background-color="var(--blueGrey-50)"
      text-color="var(--el-secondaryText)"
      active-text-color="var(--el-brandColor)">
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
    
    <div class="h-menu">
      <el-input
        placeholder="Поиск..."
        suffix-icon="el-icon-search"
        size="medium"
        v-model="input1">
      </el-input>
      
      <nuxt-link class="search-link" to="/search">
        <i class="el-icon-search"></i>
      </nuxt-link>

      <nuxt-link class='signin-link' to="/signin">Sign in</nuxt-link>
      
      <nuxt-link class='signup-link' to="/signup">Sign up</nuxt-link>
      
      <el-dropdown trigger="click">
        <span class="el-dropdown-link">
          <i class="el-icon-user"></i>
        </span>
        <el-dropdown-menu slot="dropdown">
          <nuxt-link to="/profile">
            <el-dropdown-item>
              <i class="el-icon-user"></i>
              Профиль
            </el-dropdown-item>
          </nuxt-link>
          <el-dropdown-item>
            <i class="el-icon-setting"></i>
            Настройки
          </el-dropdown-item>
          <el-dropdown-item>
            <i class="el-icon-help"></i>
            Поддержка
          </el-dropdown-item>
          <el-dropdown-item>
            <i class="el-icon-turn-off"></i>
            Выйти
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
    /* margin: 0 20px; */
    min-height: 60px;
    grid-template-columns: auto 1fr auto;
    grid-template-rows: auto; 
    grid-template-areas: 
      "h-logo h-navbar h-menu"
  }

  .h-logo {
    grid-area: h-logo;
    display: flex;
    align-items: center;
    margin-right: 30px;
    
  }

  .h-navbar {
    grid-area: h-navbar;
  }

  .h-menu {
    grid-area: h-menu;
    display: flex;
    align-items: center;
  }


  /* --------------------------------- */
  .el-menu--horizontal {
    border: none;
    background-color: var(--blueGrey-50);
    font-size: 14px;
    font-weight: 700;
  }

  .el-menu--horizontal>.el-menu-item {
    border: none;
  }

  .el-menu--horizontal>.el-menu-item:hover,
  .el-menu--horizontal>.el-menu-item:focus,
  .el-menu--horizontal>.el-menu-item:active {
    background-color: var(--blueGrey-50) !important;
  }
  /* --------------------------------- */

  .el-input {
    margin-right: 15px;
  }
  .el-input::v-deep .el-input__inner {
    border-color: var(--el-secondaryText);
  }
  .el-input::v-deep .el-input__inner:focus,
  .el-input::v-deep .el-input__inner:hover { 
    border-color: var(--el-brandColor);
  }

  /* --------------------------------- */
  .search-link {
    font-size: 22px;
    color: var(--el-regularText);
    margin-right: 15px;
  }

  .search-link:hover {
    color: var(--el-brandColor);
  }

  .signin-link {
    white-space: nowrap;
    color: var(--el-regularText);
    padding-bottom: 3px;
    padding-inline: 10px;
    margin-right: 12px;
  }

  .signin-link:hover {
    color: var(--el-brandColor);
  }

  .signup-link {
    white-space: nowrap;
    color: var(--el-regularText);
    border: solid 1px var(--el-regularText);
    border-radius: 3px;
    padding-bottom: 3px;
    padding-inline: 10px;
    margin-right: 12px;
  }

  .signup-link:hover {
    color:  var(--el-brandColor);
    border-color: var(--el-brandColor);
  }
  /* --------------------------------- */


  /* --------------------------------- */
  .el-dropdown-link {
    font-size: 24px;
    color: var(--el-regularText);
  }
  
  .el-dropdown-link:hover,
  .el-dropdown-link:active,
  .el-dropdown-link:focus {
    color: var(--el-brandColor);
  }

  .el-dropdown-menu__item {
    font-size: 15px;
    font-weight: 500;
  }

  .el-dropdown-menu__item:hover {
    /* background-color: #545c64; */
    /* color: var(--el-brandColor); */
  }

  .el-dropdown-menu__item i {
    font-size: 18px;
    font-weight: 500;
    margin-right: 10px;
  }

  
  /* --------------------------------- */


  
  

  

  
</style>