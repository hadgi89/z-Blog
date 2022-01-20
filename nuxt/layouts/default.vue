<template>
  <div class="wrapper">
    <div class="header"><Header /></div>
    <div class="content">CONTENT</div>
    <div class="aside">ASIDE</div>
    <div class="footer">FOOTER</div>
  </div>
</template>


<script>
import Header from '@/components/Header'

export default {
    components: {Header}
  
}

</script>

<style scoped>
  .wrapper {
    display: grid;
    gap: 0 30px;
    min-height: 100vh;
    grid-template-columns: 1fr 300px;
    grid-template-rows: auto 1fr auto; 
    grid-template-areas: 
      "header header"
      "content aside"
      "footer footer"
  }

  .header {
    background-color: #617777;
    grid-area: header;
  }

  .content {
    background-color: #b8e0e0;
    grid-area: content;
  }

  .aside {
    background-color: #b289d8;
    grid-area: aside;
  }

  .footer {
    background-color: #617777;
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