<script setup>
import {reactive, watch} from 'vue'
import FormButton from "@/components/FormButton.vue";
import FormInputText from "@/components/FormInputText.vue";
import FormInputSelect from "@/components/FormInputSelect.vue";


const show_meeting = defineModel('show_meeting')
const props = defineProps({
  date: Date
})
const meeting = reactive({
  title: '',
  teacher: '',
  date: '',
  time: ''
})

// ścieżka do backendu
const addMeeting = () => {
  console.log('Nowe spotkanie:', meeting)
  show_meeting.value = false
}

watch(() => props.date, (newDate) => {
  meeting.date = newDate?.toISOString().slice(0, 10) ?? ''
}, { immediate: true })
</script>

<template>
  <div class="meeting">
    <h2>Nowe spotkanie {{ meeting.date }}</h2>
    <form @submit.prevent="addMeeting">
      <FormInputText
          :label_for="'title'"
          :label="'Temat'"
          v-model:input_value="meeting.title"
      ></FormInputText>

      <FormInputText
          :label_for="'teacher'"
          :label="'Nauczyciel'"
          v-model:input_value="meeting.teacher"
      ></FormInputText>

      <FormInputSelect
        :select_values="['16:00', '17:00', '18:00', '19:00', '20:00', '21:00']"
        :input_value="meeting.time"
      >
        <label>Godzina</label>
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