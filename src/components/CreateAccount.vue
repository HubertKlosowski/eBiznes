<script setup>
import {reactive} from "vue";
import FormInputText from "@/components/FormInputText.vue";
import FormInputSelect from "@/components/FormInputSelect.vue";
import FormButton from "@/components/FormButton.vue";
import { useRouter } from "vue-router";

const user = reactive({
  name: '',
  username: '',
  email: '',
  type: '',
  password: ''
})
const router = useRouter()

const createAccount = () => {

}

const resetInputs = () => {
  user.name = ''
  user.email = ''
  user.username = ''
  user.type = ''
  user.password = ''
}
</script>

<template>
  <div class="create-account-container">
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
          v-model:input_value="user.username"
      ></FormInputText>

      <FormInputText
          :label_for="'email'"
          :label="'Adres mail'"
          :placeholder="'Wpisz adres mail'"
          v-model:input_value="user.email"
      ></FormInputText>

      <FormInputSelect
          :select_values="['Uczeń/Student', 'Nauczyciel', 'Administrator']"
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

.link-row {
  margin-top: 1rem;
  padding: 1rem;
  text-align: center;
  font-size: 0.95rem;
  color: #6b7280;
  display: flex;
  flex-direction: row;
  justify-content: center;
}
</style>