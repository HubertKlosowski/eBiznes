<script setup>
import {reactive, ref, watch} from "vue";
import FormInputText from "@/components/FormInputText.vue";
import FormInputSelect from "@/components/FormInputSelect.vue";
import FormButton from "@/components/FormButton.vue";
import { useRouter } from "vue-router";
import axios from "axios";
import ResponseOutput from "@/components/ResponseOutput.vue";

const user = reactive({
  name: '',
  username: '',
  email: '',
  type: '',
  specialty: '',
  level: '',
  experience: 0,
  password: ''
})
const change_view = defineModel('change_view')
const router = useRouter()
const student_levels = ref(['podstawówka', 'liceum', 'technikum', 'studia'])
const teacher_levels = ref(['Matematyka', 'Fizyka', 'Biologia', 'Chemia'])

const after_create = ref([])
const title = ref('')
const subtitle = ref('')
const response_status = ref(0)

const createAccount = async () => {
  try {
    const response = user.specialty === '' ?
        await axios.post('http://localhost:5000/students/register', user) :
        await axios.post('http://localhost:5000/teachers/register', user)

    after_create.value = [
      ['Imię i nazwisko', user['name']],
      ['Nazwa użytkownika', user['username']],
      ['Adres email', user['email']],
    ]
    title.value = response.data.success
    response_status.value = response.status
    resetInputs()
    change_view.value = !change_view.value
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
  Object.assign(user, {
    name: '',
    username: '',
    email: '',
    type: '',
    specialty: '',
    level: '',
    experience: 0,
    password: ''
  })
}
</script>

<template>
  <ResponseOutput
      v-model:response_status="response_status"
      :after_create="after_create"
      v-if="response_status >= 400"
      :title="title"
      :subtitle="subtitle"
  ></ResponseOutput>
  <div class="create-account-container" :style="{
    opacity: response_status < 200 ? '1' : '0.3',
    pointerEvents: response_status < 200 ? 'auto' : 'none'
  }">
    <form @submit.prevent="createAccount" class="create-account-form">
      <h2 class="form-title">Utwórz konto</h2>

      <FormInputText
          :label_for="'username'"
          :label="'Nazwa użytkownika'"
          :placeholder="'Wpisz login'"
          v-model:input_value="user.username"
      ></FormInputText>

      <FormInputText
          :label_for="'name'"
          :label="'Imię i nazwisko'"
          :placeholder="'Wpisz imię i nazwisko'"
          v-model:input_value="user.name"
      ></FormInputText>

      <FormInputText
          :label_for="'email'"
          :label="'Adres mail'"
          :placeholder="'Wpisz adres mail'"
          v-model:input_value="user.email"
      ></FormInputText>

      <FormInputSelect
          :select_values="['Uczeń/Student', 'Nauczyciel']"
          v-model:input_value="user.type"
      >
        <label>Typ użytkownika</label>
      </FormInputSelect>

      <FormInputSelect
          v-if="user.type === 'Uczeń/Student'"
          :select_values="student_levels"
          v-model:input_value="user.level"
      >
        <label>Poziom nauczania</label>
      </FormInputSelect>

      <FormInputSelect
          v-if="user.type === 'Nauczyciel'"
          :select_values="teacher_levels"
          v-model:input_value="user.specialty"
      >
        <label>Specjalność</label>
      </FormInputSelect>

      <FormInputText
          v-if="user.type === 'Nauczyciel'"
          :label_for="'experience'"
          :label="'Długość stażu'"
          :placeholder="'Wpisz długość stażu'"
          v-model:input_value="user.experience"
      ></FormInputText>

      <FormInputText
          :label_for="'password'"
          :label="'Hasło'"
          :placeholder="'••••••••'"
          :is_passwd="true"
          v-model:input_value="user.password"
      ></FormInputText>

      <div class="rules">
        <h4>Zasady tworzenia hasła:</h4>
        <ul>
          <li>co najmniej <strong>8 znaków</strong></li>
          <li>zawiera <strong>jedną wielką literę</strong> (A–Z)</li>
          <li>zawiera <strong>jedną małą literę</strong> (a–z)</li>
          <li>zawiera <strong>jedną cyfrę</strong> (0–9)</li>
          <li>zawiera <strong>jeden znak specjalny</strong> (!@#$%^&*)</li>
        </ul>
      </div>

      <FormButton :reset="true">
        <template v-slot:green>
          Utwórz konto
        </template>
        <template v-slot:red @redEvent="() => { resetInputs() }">
          Resetuj
        </template>
      </FormButton>
    </form>
    <button @click="router.back()" class="link">Wróć</button>
  </div>
</template>

<style scoped>
.rules {
  background-color: #fefce8;
  border-left: 4px solid #facc15;
  padding: 1rem;
  margin-top: 1rem;
  border-radius: 0.5rem;
  color: #444;
  font-size: 0.95rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.rules h4 {
  margin-bottom: 0.5rem;
  font-size: 1rem;
  color: #92400e;
}

.rules ul {
  list-style-type: "✔️ ";
}

.create-account-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  width: 50%;
  background: #f9fafb;
}

.create-account-form {
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
</style>