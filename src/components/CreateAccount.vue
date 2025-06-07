<script setup>
import {reactive} from "vue";
import FormInputText from "@/components/FormInputText.vue";
import FormInputSelect from "@/components/FormInputSelect.vue";
import FormButton from "@/components/FormButton.vue";

const user = reactive({
  name: '',
  username: '',
  email: '',
  type: '',
  password: ''
})

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

      <FormButton :reset="true">
        <template v-slot:green>
          Utwórz konto
        </template>
        <template v-slot:red @redEvent="() => { resetInputs() }">
          Resetuj
        </template>
      </FormButton>

      <div class="link-row">
        <RouterLink to="/" class="link">Wróć</RouterLink>
      </div>
    </form>
  </div>
</template>

<style scoped>
.create-account-container {
  display: flex;
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
}

.submit-btn {
    width: 50%;
}
</style>