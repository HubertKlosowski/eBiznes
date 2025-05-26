<script setup>
import {reactive, ref} from "vue";

const user = reactive({
  username: '',
  password: ''
})
const change_view = ref(false)

const logIn = () => {

}
</script>

<template>
  <div class="login-container">
    <form @submit.prevent="logIn" class="login-form">
      <h2 class="form-title">Zaloguj się</h2>

      <div class="form-group">
        <label for="username">Nazwa użytkownika</label>
        <input type="text" id="username" v-model="user.username" placeholder="Wpisz login" />
      </div>

      <div class="form-group">
        <label for="password">Hasło</label>
        <input type="password" id="password" v-model="user.password" placeholder="••••••••" />
      </div>

      <button type="submit" class="submit-btn">Zaloguj się</button>

      <div class="link-row">
        <RouterLink to="/forgot_passwd" class="link">Nie pamiętasz hasła?</RouterLink>
      </div>

      <div class="link-row">
        Nie masz konta?
        <span class="link-action" @click="change_view = true">Stwórz konto</span>
      </div>

      <div class="link-row">
        <RouterLink to="/" class="link">Wróć</RouterLink>
      </div>
    </form>
  </div>
</template>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  width: 50%;
  background: #f9fafb;
  padding: 2rem;
}

.login-form {
  background: #fff;
  padding: 2.5rem;
  border-radius: 1rem;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
  width: 100%;
  max-width: 400px;
}

.form-title {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 2rem;
  text-align: center;
  color: #10b981;
}

.form-group {
  margin-bottom: 1.5rem;
  display: flex;
  flex-direction: column;
}

label {
  font-size: 0.95rem;
  margin-bottom: 0.5rem;
  color: #374151;
}

input {
  padding: 0.75rem 1rem;
  border: 1px solid #d1d5db;
  border-radius: 0.5rem;
  font-size: 1rem;
  outline: none;
  transition: border-color 0.3s ease;
}

input:focus {
  border-color: #10b981;
  box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.2);
}

.submit-btn {
  width: 100%;
  padding: 0.75rem 1rem;
  background-color: #10b981;
  color: #fff;
  font-weight: 600;
  font-size: 1rem;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-btn:hover {
  background-color: #059669;
}

.link-row {
  margin-top: 1rem;
  padding: 1rem;
  text-align: center;
  font-size: 0.95rem;
  color: #6b7280;
}

.link-action {
  color: #10b981;
  cursor: pointer;
  margin-left: 0.3rem;
  text-decoration: underline;
}
</style>