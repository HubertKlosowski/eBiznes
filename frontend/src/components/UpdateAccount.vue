<script setup>
import {reactive, ref} from "vue";
import FormInputText from "@/components/FormInputText.vue";
import { useRouter } from "vue-router";
import FormButton from "@/components/FormButton.vue";
import ResponseOutput from "@/components/ResponseOutput.vue";
import axios from "axios";
import Header from "@/components/Header.vue";


const router = useRouter()
const after_create = ref([])
const title = ref('')
const subtitle = ref('')
const response_status = ref(0)
const old_user = reactive(JSON.parse(localStorage.getItem('user')))
const new_user = reactive(old_user)

// ścieżka do backendu
const updateAccount = async () => {
  try {
    const isTeacher = old_user.specialty !== undefined
    const url = isTeacher
      ? `http://localhost:5000/teachers/${old_user.id}`
      : `http://localhost:5000/students/${old_user.id}`

    const response = await axios.put(url, new_user)

    const updatedUser = isTeacher ? response.data.teacher : response.data.student
    localStorage.setItem('user', JSON.stringify(updatedUser))
    router.back()
  } catch (e) {
    if (typeof e.response === 'undefined') {
      after_create.value = ['Nie udało się połączyć z serwerem.']
      response_status.value = 500
      title.value = 'Problem z serwerem'
      subtitle.value = 'Proszę poczekać, serwer nie jest teraz dostępny.'
    } else {
      const error_response = e.response
      after_create.value = error_response.data.error
      response_status.value = error_response.status
      title.value = 'Problem z danymi'
      subtitle.value = 'Dane przekazane do formularza są błędne. Proszę je poprawić, zgodnie z komunikatami wyświetlanymi poniżej:'
    }
  }
}

const resetInputs = () => {
  Object.assign(new_user, {
    username: '',
    name: '',
    email: '',
    password: ''
  })
}

console.log(old_user.specialty !== '')
</script>

<template>
  <ResponseOutput
      v-model:response_status="response_status"
      :after_create="after_create"
      v-if="response_status >= 400"
      :title="title"
      :subtitle="subtitle"
  ></ResponseOutput>

  <Header></Header>
  <div class="update-account">
    <h2>Zmień dane konta</h2>
    <form @submit.prevent="updateAccount">
      <FormInputText
          :label_for="'username'"
          :label="'Nazwa użytkownika'"
          :placeholder="old_user.username"
          v-model:input_value="new_user.username"
      ></FormInputText>

      <FormInputText
          :label_for="'name'"
          :label="'Imię i nazwisko'"
          :placeholder="old_user.name"
          v-model:input_value="new_user.name"
      ></FormInputText>

      <FormInputText
          :label_for="'email'"
          :label="'Adres mail'"
          :placeholder="old_user.email"
          v-model:input_value="new_user.email"
      ></FormInputText>

      <FormInputText
          :label_for="'password'"
          :label="'Hasło'"
          :placeholder="'Wiesz jakie masz hasło 🙂🙂'"
          :is_passwd="true"
          v-model:input_value="new_user.password"
      ></FormInputText>

      <FormButton :reset="true" @redEvent="() => { resetInputs() }">
        <template v-slot:green>
          Zmień
        </template>
        <template v-slot:red>
          Resetuj
        </template>
      </FormButton>
    </form>
    <button @click="router.back()" class="link">Wróć</button>
  </div>
</template>

<style scoped>
.update-account {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  width: 50%;
  background: #f9fafb;
}

form {
  background: #fff;
  padding: 2.5rem;
  border-radius: 1rem;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
  width: 100%;
  max-width: 400px;
}
</style>