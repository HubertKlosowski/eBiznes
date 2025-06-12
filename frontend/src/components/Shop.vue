<script setup>
import FormButton from "@/components/FormButton.vue";
import axios from "axios";
import { useRoute } from 'vue-router'

const route = useRoute()

const couseId = route.params.id

const user = defineModel('user')
const show_shop = defineModel('show_shop')

// ścieżka do backendu
const addStudentToCourse = async () => {
  try {
    const res = await axios.post(`http://localhost:5000/courses/${couseId}/students/${user.value.id}`)

    resetInputs()
    return res.data
  } catch (e) {
    console.error('Błąd przy dodawaniu studenta do kursu:', e)
    throw e
  }
}

const resetInputs = () => {
  show_shop.value = false
}
</script>

<template>
  <div class="shop">
    <h2>Potwierdź zakup kursu</h2>
    <form @submit.prevent="addStudentToCourse">
      <FormButton :reset="true" @redEvent="() => { resetInputs() }">
        <template v-slot:green>
          Zapisz się
        </template>
        <template v-slot:red>
          Wróć
        </template>
      </FormButton>
    </form>
  </div>
</template>

<style scoped>
.shop {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(245, 245, 245, 0.95);
  border-radius: 1rem;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  z-index: 1000;
  color: #333;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
}

form {
  width: 100%;
  max-width: 400px;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

h2 {
  margin-bottom: 1rem;
  font-size: 1.5rem;
}
</style>