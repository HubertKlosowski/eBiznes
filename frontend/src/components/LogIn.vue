<script setup>
import {reactive, ref} from "vue";
import FormInputText from "@/components/FormInputText.vue";
import CreateAccount from "@/components/CreateAccount.vue";
import { useRouter } from 'vue-router'
import FormButton from "@/components/FormButton.vue";
import Header from "@/components/Header.vue";
import axios from "axios";
import FormInputSelect from "@/components/FormInputSelect.vue";

const router = useRouter()

const user = reactive({
  username: '',
  password: '',
  type: ''
})
const change_view = ref(false)

const logIn = async () => {
  try {
    const response = user.type === 'Nauczyciel' ?
        await axios.post('http://localhost:5000/teachers/login', user) :
        await axios.post('http://localhost:5000/students/login', user)

    const data = response.data
    const login_user = data.student || data.teacher

    localStorage.setItem('user', JSON.stringify(login_user))
    router.push(user.type === 'Nauczyciel' ? '/account/teacher' : '/account/student')
    resetInputs()
  } catch (e) {
    console.log(e)
  }
}

const resetInputs = () => {
  Object.assign(user, {
    username: '',
    password: '',
    type: ''
  })
}

console.log(change_view.value)
</script>

<template>
  <Header></Header>
  <div class="login-container" v-if="!change_view">
    <form @submit.prevent="logIn" class="login-form">
      <h2 class="form-title">Zaloguj się</h2>

      <FormInputText
          :label_for="'username'"
          :label="'Nazwa użytkownika'"
          :placeholder="'Wpisz login'"
          v-model:input_value="user.username"
      ></FormInputText>

      <FormInputSelect
          :select_values="['Uczeń/Student', 'Nauczyciel']"
          v-model:input_value="user.type"
      >
        <label>Typ użytkownika</label>
      </FormInputSelect>

      <FormInputText
          :label_for="'password'"
          :label="'Hasło'"
          :placeholder="'••••••••'"
          :is_passwd="true"
          v-model:input_value="user.password"
      ></FormInputText>

      <FormButton :reset="false">
        <template v-slot:green>
          Zaloguj się
        </template>
      </FormButton>

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
  <CreateAccount
      v-else
      v-model:change_view="change_view"
  ></CreateAccount>
</template>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.link-row > .link {
  width: 100%;
}

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
  width: 100%;
  margin-top: 1rem;
  padding: 1rem;
  text-align: center;
  font-size: 0.95rem;
  color: #6b7280;
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.link-action {
  color: #10b981;
  cursor: pointer;
  margin-left: 0.3rem;
  text-decoration: underline;
}
</style>