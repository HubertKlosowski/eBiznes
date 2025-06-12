<script setup>
import { useRouter } from 'vue-router';
import FormButton from "@/components/FormButton.vue";
import axios from "axios";
import ResponseOutput from "@/components/ResponseOutput.vue";
import {reactive, ref} from "vue";

const router = useRouter()
const user = reactive(JSON.parse(localStorage.getItem('user')))
const after_create = ref([])
const title = ref('')
const subtitle = ref('')
const response_status = ref(0)
const move_to = ref('')

// ścieżka do backendu
const deleteAccount = async () => {
  try {
    const isTeacher = user.specialty !== ''
    const url = isTeacher
      ? `http://localhost:5000/teachers/${user.id}`
      : `http://localhost:5000/students/${user.id}`

    const response = await axios.delete(url)

    after_create.value = [
      ['Nazwa użytkownika', user['username']],
      ['Adres email', user['email']],
    ]
    title.value = response.data.success
    subtitle.value = 'Użytkownik został poprawnie usunięty.'
    response_status.value = response.status
    localStorage.removeItem('user')
    move_to.value = '/'
  } catch (e) {
    if (typeof e.response === 'undefined') {
      after_create.value = ['Nie udało się połączyć z serwerem.']
      response_status.value = 500
      title.value = 'Problem z serwerem'
      subtitle.value = 'Proszę poczekać, serwer nie jest teraz dostępny.'
    } else {
      const error_response = e.response
      response_status.value = error_response.status
      after_create.value = error_response.data.error
      subtitle.value = 'Próba usunięcia konta użytkownika się nie powiodła. Proszę zapoznać się z komunikatami wyświetlanymi poniżej:'
    }
  }
}
</script>

<template>
  <ResponseOutput
      v-model:response_status="response_status"
      :after_create="after_create"
      v-if="response_status >= 100 && response_status !== 403"
      :move_to="move_to"
      :title="title"
      :subtitle="subtitle"
  ></ResponseOutput>

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