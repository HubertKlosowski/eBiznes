<script setup>
import { useRouter } from 'vue-router';
import FormButton from "@/components/FormButton.vue";

const router = useRouter()

// ścieżka do backendu
const deleteAccount = () => {
  localStorage.removeItem('user')
}
</script>

<template>
  <div class="delete-account">
    <h3>Czy chcesz usunąć konto?</h3>
    <form @submit.prevent="deleteAccount">
      <FormButton :reset="true" @redEvent="() => { router.back() }">
        <template v-slot:green>
          Tak
        </template>
        <template v-slot:red>
          Nie
        </template>
      </FormButton>
    </form>
  </div>
</template>

<style scoped>
.delete-account {
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