<template>
  <div class="home">
    <Header></Header>

    <Footer></Footer>
  </div>
</template>

<script setup>
// vite中导入非ts.js文件时，必须填写文件后缀
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"

// 测试CORS的跨域配置是否有问题
// import axios from "axios"
//
// const http = axios.create()

import http from "../utils/http";

// 测试服务端的跨域是否配置成功
http.get("/home/test/").then(response=>{
  console.log(response.data);
})
</script>

<style scoped>

</style>