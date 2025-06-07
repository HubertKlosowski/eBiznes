<script setup>
import { useRoute } from 'vue-router'
import {onMounted, reactive, ref} from "vue";
import _ from "lodash";
import FormInputText from "@/components/FormInputText.vue";
import FormInputSelect from "@/components/FormInputSelect.vue";
import FormButton from "@/components/FormButton.vue";

const route = useRoute()
const courseId = route.params.id

const course = reactive({
  subject: '',
  title: '',
  desc: '',
  level: '',
  duration: 0,
  price: 0,
  score: 0
})
const lessons = ref(null)
const opinions = ref(null)
const opinion = reactive({
  title: '',
  content: '',
  score: 0
})

// ścieżka do backendu
const getLessonsByCourse = () => {

}

// ścieżka do backendu
const addOpinion = () => {

}

// ścieżka do backendu
const getOpinions = () => {

}

const resetInputs = () => {
  Object.assign(opinion, {
    title: '',
    content: '',
    score: 0
  })
}

onMounted(() => {
  Object.assign(course, JSON.parse(localStorage.getItem('courses'))[courseId])
})
</script>
<template>
  <div class="courses-main">
    <div class="course-header">
      <h2>{{ course.title }}</h2>
      <RouterLink to="/shop" class="link">
        Kup
      </RouterLink>
      <RouterLink to="/courses" class="link">
        Wróć
      </RouterLink>
    </div>
    <div class="courses-intro">
      <div class="course-scope">
        <h3>Zakres kursu</h3>
        <div class="content">
          <span v-for="(sentence, i) in course.desc.split('.')" :key="i">{{ sentence }}</span>
        </div>
      </div>
      <div class="course-info">
        <h3>Dane ogólne</h3>
        <ol type="I">
          <li>Cena: {{ course.price }} zł</li>
          <li>Ocena: {{ course.score }}/5</li>
          <li>Ilość godzin: {{ course.duration }}</li>
          <li>Poziom materiału: {{ course.level }}</li>
          <li>Nauczyciel: Hubert</li>
        </ol>
      </div>
    </div>
    <div class="course-lessons" v-if="!_.isEmpty(lessons)">
      <h3>Lekcje</h3>
      <div class="lessons">
        <div class="lesson" v-for="(lesson, i) in lessons" :key="i"></div>
      </div>
    </div>
    <div class="course-lessons" v-else>
      <h3>Lekcje</h3>
      <p><b>Na ten moment nauczyciel nie dodał żadnych lekcji do kursu!</b></p>
    </div>
    <div class="course-tests">
      <h3>Testy</h3>
      <div class="tests">

      </div>
    </div>
    <div class="course-opinions">
      <h3>Opinie</h3>
      <form @submit.prevent="addOpinion">
        <FormInputText
            :label_for="'minimum'"
            :label="'Tytuł'"
            :placeholder="'Wpisz tytuł'"
            v-model:input_value="opinion.title"
        ></FormInputText>

        <FormInputText
            :label_for="'minimum'"
            :label="'Treść opinii'"
            :placeholder="'Podaj treść opinii'"
            v-model:input_value="opinion.content"
        ></FormInputText>

        <FormInputSelect
            :select_values="[1, 2, 3, 4, 5]"
            v-model:input_value="opinion.score"
        >
          <label>Ocena</label>
        </FormInputSelect>

        <FormButton :reset="true" @redEvent="() => { resetInputs() }">
          <template v-slot:green>
            Zatwierdź
          </template>
          <template v-slot:red>
            Wyczyść
          </template>
        </FormButton>
      </form>
    </div>
  </div>
</template>

<style scoped>
form {
  width: 80%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.courses-main {
  max-width: 100%;
  margin: 0 auto;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  background-color: #f9fafb;
  border-radius: 1rem;
  box-shadow: 0 0 12px rgba(0, 0, 0, 0.05);
}

.course-header {
  width: 80%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.courses-intro {
  display: flex;
  flex-direction: row;
  gap: 2rem;
  width: 100%;
  flex-wrap: wrap;
}

.course-scope,
.course-info {
  flex: 1;
  min-width: 280px;
  background-color: #ecfdf5;
  padding: 1rem;
  border-radius: 0.75rem;
  border-left: 4px solid #10b981;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
}

.course-lessons,
.course-tests,
.course-opinions {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: white;
  padding: 1.5rem;
  border-radius: 0.75rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.course-lessons h3,
.course-tests h3,
.course-opinions h3 {
  margin-bottom: 1rem;
  color: #065f46;
}

@media (max-width: 768px) {
  .courses-intro {
    flex-direction: column;
  }

  .link {
    font-size: 0.9rem;
  }
}
</style>
