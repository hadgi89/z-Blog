<template>
  <div class="wrapper">
    <div class="header"><Header /></div>
    <div class="content"><Nuxt /></div>
    <div class="aside">ASIDE</div>
    <div class="footer">FOOTER</div>
  </div>
</template>


<script>
import Header from '~/components/Header'

export default {
    components: {Header}
  
}

</script>

<style scoped>
  .wrapper {
    display: grid;
    gap: 0 30px;
    min-height: 100vh;
    grid-template-columns: auto minmax(320px, 1200px) 300px auto;
    grid-template-rows: auto 1fr auto; 
    grid-template-areas: 
      ". header header ."
      ". content aside ."
      "footer footer footer footer"
  }

  .header {
    grid-area: header;
  }

  .content {
    grid-area: content;
  }

  .aside {
    grid-area: aside;
  }

  .footer {
    grid-area: footer;
    
  }

  @media (max-width: 765px) {
    .wrapper {
      grid-template-columns: minmax(320px, 1fr);
      grid-template-areas: 
        "header"
        "content"
        "footer"
    }

    .aside {
      display: none;
    }

  }
</style>