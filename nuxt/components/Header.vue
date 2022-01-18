<template>
  
  <div class="header-wrapper">
    
    <div class="h-logo">
      1
    </div>
    
    <div class="h-navbar">
      2
    </div>
        
    <div class='h-usermenu'>
      3
    </div>
  </div>

</template>

<script>
  export default {
    name: "Header",
  }
</script>


<style scoped>
  .header-wrapper {
    display: grid;
    grid-template-columns: 50px auto 100px;
    gap: 20px;
    background-color: blueviolet;
    height: 100%;
    /* align-items: center; */
    /* align-content: center; */
    align-self: center  ;
  }

  .h-logo {
    background-color: #545c64;
  }
  .h-navbar {
    background-color: coral;
  }

  .h-usermenu {
    background-color: darkcyan;
  }

  
</style>