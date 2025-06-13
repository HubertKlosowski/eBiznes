<script setup>
import {reactive, ref, watch} from 'vue'
import FormButton from "@/components/FormButton.vue";
import FormInputText from "@/components/FormInputText.vue";
import FormInputSelect from "@/components/FormInputSelect.vue";
import FormTextArea from "@/components/FormTextArea.vue";
import axios from "axios";
import ResponseOutput from "@/components/ResponseOutput.vue";


const show_meeting = defineModel('show_meeting')
const props = defineProps(['date', 'user'])
const meeting = reactive({
  title: '',
  teacher_id: props.user.id,
  date: '',
  description: '',
  start_date: '',
  end_date: '',
  student_mail: '',
  student_id: '',
  link: ''
})

const after_create = ref([])
const title = ref('')
const subtitle = ref('')
const response_status = ref(0)

const parseTime = (timeStr) => {
  const [h, m] = timeStr.split(':').map(Number)
  return h * 60 + m
}

const addMeeting = async () => {
  meeting.teacher = props.user.id

  if (parseTime(meeting.start_date) >= parseTime(meeting.end_date)) {
    after_create.value = ['Godzina zakończenia musi być późniejsza niż rozpoczęcia.']
    response_status.value = 400
    title.value = 'Błąd w godzinach'
    subtitle.value = 'Sprawdź godziny spotkania i spróbuj ponownie.'
    return
  }

  meeting.start_date = `${meeting.date} ${meeting.start_date}:00`
  meeting.end_date = `${meeting.date} ${meeting.end_date}:00`

  try {
    const response = await axios.get(`http://localhost:5000/students/${meeting.student_mail}`)
    if (response.data && response.data.student && response.data.student.id) {
      meeting.student_id = response.data.student.id
    } else {
      after_create.value = ['Nie znaleziono studenta o podanym adresie email.']
      response_status.value = 404
      title.value = 'Nie znaleziono studenta'
      subtitle.value = 'Upewnij się, że adres email jest poprawny.'
      return
    }
  } catch (e) {
    if (typeof e.response === 'undefined') {
      after_create.value = ['Nie udało się połączyć z serwerem.']
      response_status.value = 500
      title.value = 'Problem z serwerem'
      subtitle.value = 'Proszę poczekać, serwer nie jest teraz dostępny.'
    } else {
      const error_response = e.response
      after_create.value = [error_response.data.error || 'Błąd pobierania studenta.']
      response_status.value = error_response.status
      title.value = 'Problem z danymi'
      subtitle.value = 'Dane przekazane do formularza są błędne. Proszę je poprawić.'
    }
    return
  }

  try {
    const response = await axios.post('http://localhost:5000/meetings', meeting)
    after_create.value = ['Spotkanie zostało pomyślnie dodane.']
    response_status.value = response.status
    title.value = 'Sukces!'
    subtitle.value = ''
    resetInputs()
    show_meeting.value = false
  } catch (e) {
    if (typeof e.response === 'undefined') {
      after_create.value = ['Nie udało się połączyć z serwerem.']
      response_status.value = 500
      title.value = 'Problem z serwerem'
      subtitle.value = 'Proszę poczekać, serwer nie jest teraz dostępny.'
    } else {
      const error_response = e.response
      after_create.value = [error_response.data.error || 'Nie udało się zapisać spotkania.']
      response_status.value = error_response.status
      title.value = 'Problem z danymi'
      subtitle.value = 'Dane przekazane do formularza są błędne. Proszę je poprawić.'
    }
  }
}

const resetInputs = () => {
  Object.assign(meeting, {
    title: '',
    teacher_id: props.user.id,
    date: '',
    description: '',
    start_date: '',
    end_date: '',
    student_mail: '',
    student_id: '',
    link: ''
  })
}

watch(() => props.date, (newDate) => {
  meeting.date = newDate?.toISOString().slice(0, 10) ?? ''
}, { immediate: true })
</script>

<template>
  <ResponseOutput
      v-model:response_status="response_status"
      :after_create="after_create"
      v-if="response_status >= 100"
      :title="title"
      :subtitle="subtitle"
  ></ResponseOutput>
  <div class="meeting">
    <h2>Nowe spotkanie {{ meeting.date }}</h2>
    <form @submit.prevent="addMeeting">
      <FormInputText
          :label_for="'title'"
          :label="'Temat'"
          :placeholder="'Podaj temat spotkania'"
          v-model:input_value="meeting.title"
      ></FormInputText>

      <FormInputText
          :label_for="'student'"
          :label="'Uczeń'"
          :placeholder="'Podaj adres mail ucznia'"
          v-model:input_value="meeting.student_mail"
      ></FormInputText>

      <FormTextArea
          :label_for="'description'"
          :label="'Opis spotkania'"
          :placeholder="'Podaj opis spotkania'"
          v-model:input_value="meeting.description"
      ></FormTextArea>

      <FormInputSelect
        :select_values="['16:00', '17:00', '18:00', '19:00', '20:00', '21:00']"
        v-model:input_value="meeting.start_date"
      >
        <label>Godzina rozpoczęcia</label>
      </FormInputSelect>

      <FormInputSelect
        :select_values="['16:00', '17:00', '18:00', '19:00', '20:00', '21:00']"
        v-model:input_value="meeting.end_date"
      >
        <label>Godzina zakończenia</label>
      </FormInputSelect>

      <FormButton :reset="true" @redEvent="() => { show_meeting = false }">
        <template v-slot:green>
          Dodaj spotkanie
        </template>
        <template v-slot:red>
          Anuluj
        </template>
      </FormButton>
    </form>
  </div>
</template>

<style scoped>
.meeting {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(245, 245, 245, 0.95);
  border-radius: 1rem;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  z-index: 5;
  color: #333;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  overflow-y: auto;
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