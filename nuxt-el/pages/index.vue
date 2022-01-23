<template>
  <div>
    <h1>Привет, это главная страница</h1>
    <div v-for="post in posts" :key="post.slug" class="blog">
      <div class="blog-title">{{ post.title }}</div>
      <div class="blog-introtext">{{ post.desc }}</div>
      <div class="blog-tag">{{ post.tags }}</div>
    </div>
  </div>
  
  
</template>

<script>
import axios from "axios";

export default {
  async asyncData(ctx) {
    const { data } = await axios.get(`http://127.0.0.1:8000/api/posts/`);
    return {
      posts: data.results,
    }
  }
}
</script>
