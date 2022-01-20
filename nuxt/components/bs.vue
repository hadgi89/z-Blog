<template>
  
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand href="#">
        <!-- z-BLOG -->
        <img src="logo9.png" :width="40" alt="Kitten">
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="#">ГЛАВНАЯ</b-nav-item>
          <b-nav-item href="#">СТАТЬИ</b-nav-item>
          <b-nav-item href="#">ХАБЫ</b-nav-item>
          <b-nav-item href="#">АВТОРЫ</b-nav-item>
          <b-nav-item href="#">КОНТАКТЫ</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="Поиск..."></b-form-input>
            <b-button size="sm" variant="outline-success" class="my-2 my-sm-0" type="submit">
              Поиск
              <!-- <b-icon icon="search"></b-icon> -->
            </b-button>
          </b-nav-form>

          <b-nav-item-dropdown right  toggle-class="text-decoration-none" no-caret>
            <template #button-content>
              <b-icon icon="globe"></b-icon>
            </template> 
            <b-dropdown-item href="#">EN</b-dropdown-item>
            <b-dropdown-item href="#">ES</b-dropdown-item>
            <b-dropdown-item href="#">RU</b-dropdown-item>
            <b-dropdown-item href="#">FA</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template #button-content>
              <em>User</em>
            </template>
            <b-dropdown-item href="#">Profile</b-dropdown-item>
            <b-dropdown-item href="#">Sign Out</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>

</template>

<script>
  import { BNavbar, BNavbarNav, BNavbarBrand, BNavbarToggle} from 'bootstrap-vue'
  
  export default {
    name: "Header",
    components: { BNavbar, BNavbarNav, BNavbarBrand, BNavbarToggle },
  }
</script>


<style scoped>
  .btn-search {
    color: var(--gray);
  }

  .btn-search:hover {
    color: var(--gray-light);
  }

</style>