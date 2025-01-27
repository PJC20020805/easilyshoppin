<template>
  <div>
    <h1>欢迎来到全栈项目！</h1>
    <p>前端运行在 Vue + Vite</p>
    <p>后端状态：{{ backendStatus }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const backendStatus = ref('正在检测后端连接...')

// 测试与 Django 后端的连接
axios.get('/api/')
  .then(() => backendStatus.value = '后端连接成功 ✅')
  .catch(() => backendStatus.value = '后端连接失败 ❌')
</script>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
