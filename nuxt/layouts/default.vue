<template>
    <el-container>
      <el-header><Header/></el-header>
      <el-container>
        <el-container>
          <el-main>Main</el-main>
          <el-footer>Footer</el-footer>
        </el-container>
        <el-aside width="200px">Aside</el-aside>
      </el-container>
    </el-container>
</template>


<script>
import Header from '@/components/Header'

export default {
    components: {Header}
  
}

</script>

<style scoped>
    .el-header {
      /* margin: 0; */
      /* padding: 0; */
      background-color: #a2e430;
    }
</style>