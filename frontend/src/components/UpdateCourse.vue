<script setup>
import FormButton from "@/components/FormButton.vue";
import FormInputText from "@/components/FormInputText.vue";
import FormInputSelect from "@/components/FormInputSelect.vue";
import FormTextArea from "@/components/FormTextArea.vue";
import axios from "axios";
import _ from "lodash";


const courses = defineModel('courses')
const show_update_course = defineModel('show_update_course')
const update_course = defineModel('update_course')

// ścieżka do backendu
const updateCourse = async () => {
  try {
    const courseId = update_course.value.id
    const res = await axios.put(`http://localhost:5000/courses/${courseId}`, update_course.value)

    const courseIndex = _.findIndex(courses.value, { id: courseId })
    if (courseIndex !== -1) {
      courses.value[courseIndex] = { ...courses.value[courseIndex], ...update_course.value }
    }
    resetInputs()
    return res.data
  } catch (e) {
    console.error('Błąd przy aktualizacji kursu:', e)
    throw e
  }
}

const resetInputs = () => {
  show_update_course.value = false
}
</script>

<template>
  <div class="update-course">
    <h2>Aktualizacja kursu z {{ update_course.title }}</h2>
    <form @submit.prevent="updateCourse">
      <FormInputText
          :label_for="'title'"
          :label="'Tytuł'"
          :placeholder="update_course.title"
          v-model:input_value="update_course.title"
      ></FormInputText>

      <FormInputText
          :label_for="'duration'"
          :label="'Czas trwania'"
          :placeholder="update_course.duration"
          v-model:input_value="update_course.duration"
      ></FormInputText>

      <FormInputSelect
        :select_values="['podstawowka', 'liceum', 'technikum', 'studia']"
        :input_value="update_course.level"
      >
        <label>Poziom nauczania</label>
      </FormInputSelect>

      <FormInputText
          :label_for="'price'"
          :label="'Cena'"
          :placeholder="update_course.price"
          v-model:input_value="update_course.price"
      ></FormInputText>

      <FormTextArea
            :label_for="'description'"
            :label="'Opis kursu'"
            :placeholder="update_course.description"
            v-model:input_value="update_course.description"
        ></FormTextArea>

      <FormButton :reset="true" @redEvent="() => { resetInputs() }">
        <template v-slot:green>
          Zapisz zmiany
        </template>
        <template v-slot:red>
          Wróć
        </template>
      </FormButton>
    </form>
  </div>
</template>

<style scoped>
.update-course {
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