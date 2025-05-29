<script setup>
import FormInputText from "@/components/FormInputText.vue";
import {ref} from "vue";

const email = ref('')

const resetPassword = () => {

}
</script>

<template>
  <div class="forgot-password-container">
    <form @submit.prevent="resetPassword" class="forgot-password-form">
      <h2 class="form-title">Resetuj hasło</h2>

      <FormInputText
          :label_for="'email'"
          :label="'Adres mail'"
          :placeholder="'Wpisz adres mail'"
          v-model:input_value="email"
      ></FormInputText>

      <button type="submit" class="submit-btn">Utwórz konto</button>

      <div class="link-row">
        <RouterLink to="/login" class="link">Wróć</RouterLink>
      </div>
    </form>
  </div>
</template>

<style scoped>
.forgot-password-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  width: 50%;
  background: #f9fafb;
}

.forgot-password-form {
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
</style>