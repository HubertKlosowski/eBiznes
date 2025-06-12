<script setup>
import {reactive} from 'vue'
import FormButton from "@/components/FormButton.vue";
import FormInputText from "@/components/FormInputText.vue";
import FormInputSelect from "@/components/FormInputSelect.vue";
import FormTextArea from "@/components/FormTextArea.vue";
import axios from "axios";


const user = defineModel('user')
const courses = defineModel('courses')
const show_course = defineModel('show_course')
const course = reactive({
  description: '',
  duration: 0,
  level: '',
  price: '',
  subject: user.value.specialty,
  teacher_id: user.value.id,
  title: ''
})

// ścieżka do backendu
const addCourse = async () => {
  try {
    const res = await axios.post(`http://localhost:5000/courses`, course)

    if (res.data.course_id) {
      courses.value.push({ course_id: res.data.course_id, ...course })
    }

    resetInputs()
    return res.data
  } catch (e) {
    console.error('Błąd przy tworzeniu kursu:', e)
    throw e
  }
}

const resetInputs = () => {
  show_course.value = false
}
</script>

<template>
  <div class="create-course">
    <h2>Nowy kurs z {{ user.specialty }}</h2>
    <form @submit.prevent="addCourse">
      <FormInputText
          :label_for="'title'"
          :label="'Tytuł'"
          v-model:input_value="course.title"
      ></FormInputText>

      <FormInputText
          :label_for="'duration'"
          :label="'Czas trwania'"
          v-model:input_value="course.duration"
      ></FormInputText>

      <FormInputSelect
        :select_values="['podstawowka', 'liceum', 'technikum', 'studia']"
        :input_value="course.level"
      >
        <label>Poziom nauczania</label>
      </FormInputSelect>

      <FormInputText
          :label_for="'price'"
          :label="'Cena'"
          v-model:input_value="course.price"
      ></FormInputText>

      <FormTextArea
            :label_for="'description'"
            :label="'Opis kursu'"
            :placeholder="'Podaj opis kursu'"
            v-model:input_value="course.description"
        ></FormTextArea>

      <FormButton :reset="true" @redEvent="() => { resetInputs() }">
        <template v-slot:green>
          Dodaj kurs
        </template>
        <template v-slot:red>
          Wróć
        </template>
      </FormButton>
    </form>
  </div>
</template>

<style scoped>
.create-course {
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