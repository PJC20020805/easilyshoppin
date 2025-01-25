<template>
  <div class="register-container">
    <h2>注册新账户</h2>
    <form @submit.prevent="handleRegister">
      <input type="text" v-model="username" placeholder="用户名" required>
      <input type="password" v-model="password" placeholder="密码" required>
      <button type="submit">注册</button>
    </form>
    <p>已有账号？<a @click="goToLogin">立即登录</a></p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    handleRegister() {
      // 后续连接注册API
    },
    goToLogin() {
      this.$router.push('/login')
    }
  }
}
</script>