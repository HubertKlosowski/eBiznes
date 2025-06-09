<script setup>
import { useRoute } from 'vue-router'
import {onMounted, reactive, ref} from "vue";
import _ from "lodash";
import FormInputText from "@/components/FormInputText.vue";
import FormInputSelect from "@/components/FormInputSelect.vue";
import FormButton from "@/components/FormButton.vue";
import FormTextArea from "@/components/FormTextArea.vue";

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
const tests = ref(null)
const opinion = reactive({
  title: '',
  content: '',
  score: 0
})

// ścieżka do backendu
const getLessonsByCourse = () => {

}

// ścieżka do backendu
const getTestsByCourse = () => {

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
        <dl>
          <div class="info-item">
            <dt>Cena:</dt>
            <dd>{{ course.price }} zł</dd>
          </div>
          <div class="info-item">
            <dt>Ocena:</dt>
            <dd>{{ course.score }}/5</dd>
          </div>
          <div class="info-item">
            <dt>Ilość godzin:</dt>
            <dd>{{ course.duration }}</dd>
          </div>
          <div class="info-item">
            <dt>Poziom materiału:</dt>
            <dd>{{ course.level }}</dd>
          </div>
          <div class="info-item">
            <dt>Nauczyciel:</dt>
            <dd>Hubert</dd>
          </div>
        </dl>
      </div>
    </div>
    <div class="course-lessons">
      <h3>Lekcje</h3>
      <div class="lessons" v-if="!_.isEmpty(lessons)">
        <div class="lesson" v-for="(lesson, i) in lessons" :key="i"></div>
      </div>
      <p v-else><b>Na ten moment nauczyciel nie dodał żadnych lekcji do kursu!</b></p>
    </div>
    <div class="course-tests">
      <h3>Testy</h3>
      <div class="tests" v-if="!_.isEmpty(tests)">
        <div class="test" v-for="(test, i) in tests" :key="i"></div>
      </div>
      <p v-else><b>Na ten moment nauczyciel nie dodał żadnych testów do kursu!</b></p>
    </div>
    <div class="course-opinions">
      <div class="form">
        <h3>Opinie</h3>
        <form @submit.prevent="addOpinion">
          <FormInputText
              :label_for="'minimum'"
              :label="'Tytuł'"
              :placeholder="'Wpisz tytuł'"
              v-model:input_value="opinion.title"
          ></FormInputText>

          <FormTextArea
              :label_for="'minimum'"
              :label="'Treść opinii'"
              :placeholder="'Podaj treść opinii'"
              v-model:input_value="opinion.content"
          ></FormTextArea>

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
      <div class="opinions" v-if="!_.isEmpty(tests)">
        <div class="opinion" v-for="(opinion, i) in opinions" :key="i"></div>
      </div>
      <p v-else><b>Na ten moment kurs nie posiada opinii!</b></p>
    </div>
  </div>
</template>

<style scoped>
.form {
  width: 50%;
  border-right: 2px solid green;
}

form {
  width: 80%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.courses-main {
  width: 90%;
  margin: 0 auto;
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
  justify-content: center;
  gap: 2rem;
  width: 100%;
}

.course-info, .course-scope {
  width: 40%;
  background-color: #f0fdf4;
  padding: 1.5rem;
  border-radius: 1rem;
  border-left: 4px solid #10b981;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
}

.course-info h3 {
  margin-bottom: 1rem;
  color: #064e3b;
  font-size: 1.2rem;
}

dl {
  margin: 0;
  padding: 0;
}

.info-item {
  display: flex;
  justify-content: space-between;
  padding: 0.4rem 0;
  border-bottom: 1px solid #e5e7eb;
}

dt {
  font-weight: 600;
  color: #1f2937;
}

dd {
  margin: 0;
  color: #374151;
}

.course-opinions {
  width: 90%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  background-color: white;
  padding: 1.5rem;
  border-radius: 0.75rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.course-lessons, .course-tests {
  width: 90%;
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
