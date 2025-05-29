<script setup>
import {reactive, ref} from "vue";
import FormInputText from "@/components/FormInputText.vue";
import CreateAccount from "@/components/CreateAccount.vue";
import { useRouter } from 'vue-router'

const router = useRouter()

const user = reactive({
  username: '',
  password: ''
})
const change_view = ref(false)

const logIn = () => {
  const usertmp = {
    name: 'Hubert Kłosowski',
    username: 'YsOtUuRdMeUnMt',
    email: 'example@ex.pl',
    level: 'primary school'
  }
  localStorage.setItem('user', JSON.stringify(usertmp))
  router.push('/account')
}
</script>

<template>
  <div class="login-container" v-if="!change_view">
    <form @submit.prevent="logIn" class="login-form">
      <h2 class="form-title">Zaloguj się</h2>

      <FormInputText
          :label_for="'username'"
          :label="'Nazwa użytkownika'"
          :placeholder="'Wpisz login'"
          v-model:input_value="user.username"
      ></FormInputText>

      <FormInputText
          :label_for="'password'"
          :label="'Hasło'"
          :placeholder="'••••••••'"
          :is_passwd="true"
          v-model:input_value="user.password"
      ></FormInputText>

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
  <CreateAccount v-else></CreateAccount>
</template>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  width: 50%;
  background: #f9fafb;
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