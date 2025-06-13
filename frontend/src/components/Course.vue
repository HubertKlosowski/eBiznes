<script setup>
import { useRoute } from 'vue-router'
import {onMounted, reactive, ref} from "vue";
import _ from "lodash";
import FormInputText from "@/components/FormInputText.vue";
import FormInputSelect from "@/components/FormInputSelect.vue";
import FormButton from "@/components/FormButton.vue";
import FormTextArea from "@/components/FormTextArea.vue";
import axios from "axios";
import Shop from "@/components/Shop.vue";
import ResponseOutput from "@/components/ResponseOutput.vue";

const route = useRoute()
const courseId = route.params.id

const course = reactive(_.find(JSON.parse(localStorage.getItem('courses')), ['id', courseId]))
const teacher = reactive({
  name: '',
  username: ''
})
const lessons = ref([])
const opinions = ref(null)
const tests = ref([])
const opinion = reactive({
  title: '',
  content: '',
  score: 0
})

const user = reactive(JSON.parse(localStorage.getItem('user')))
const type = ref('')
const student_in_course = ref([])
const show_shop = ref(false)
const show_test = reactive({
  test: -1,
  form: false
})

const test = reactive({
  title: '',
  content: {},
  course_id: course.id
})

const show_lesson = reactive({
  lesson: -1,
  form: false
})
const lesson = reactive({
  title: '',
  content: {},
  course_id: course.id
})

const after_create = ref([])
const title = ref('')
const subtitle = ref('')
const response_status = ref(0)

// ścieżka do backendu
const getStudentsForCourse = async () => {
  try {
    const res = await axios.get(`http://localhost:5000/courses/${course.id}/students`)
    return res.data
  } catch (e) {
    console.error('Błąd przy pobieraniu studentów kursu:', e)
    throw e
  }
}

// ścieżka do backendu
const getTeacherInfo = async () => {
  try {
    const res = await axios.get(`http://localhost:5000/teachers/${course.teacher_id}`)
    Object.assign(teacher, {
      name: res.data['name'],
      username: res.data['username']
    })
    return res.data
  } catch (e) {
    console.error('Błąd przy pobieraniu studentów kursu:', e)
    throw e
  }
}

// ścieżka do backendu
const deleteStudentFromCourse = async (studentId) => {
  try {
    const res = await axios.delete(`http://localhost:5000/courses/${course.id}/students/${studentId}`)
    _.remove(student_in_course.value, ['student_id', studentId])
  } catch (e) {
    console.error('Błąd przy usuwaniu studenta z kursu:', e)
    throw e
  }
}

const getOpinions = async () => {
  try {
    const res = await axios.get(`http://localhost:5000/courses/${course.id}/opinions`)
    opinions.value = res.data
  } catch (e) {
    console.error('Błąd przy pobieraniu opinii:', e)
  }
}

const addOpinion = async () => {
  try {
    const res = await axios.post(`http://localhost:5000/courses/${course.id}/opinions`, opinion)
    opinions.value.push({ ...opinion })
    resetInputs()
  } catch (e) {
    console.error('Błąd przy dodawaniu opinii:', e)
  }
}

const getLessonsByCourse = async () => {
  try {
    const res = await axios.get(`http://localhost:5000/courses/${course.id}/lessons`)
    if (!_.isEmpty(res.data)) {
      lessons.value = res.data
    }
  } catch (e) {
    console.error('Błąd przy pobieraniu lekcji:', e)
  }
}

const getTestsByCourse = async () => {
  try {
    const res = await axios.get(`http://localhost:5000/courses/${course.id}/tests`)
    if (!_.isEmpty(res.data)) {
      tests.value = res.data
    }
  } catch (e) {
    console.error('Błąd przy pobieraniu testów:', e)
  }
}

const addTest = async () => {
  try {
    const response = await axios.post('http://localhost:5000/tests', test)
    tests.value.push(response.data.test)
    title.value = 'Test dodany pomyślnie'
    subtitle.value = 'Nowy test został utworzony i dodany do listy.'
  } catch (e) {
    if (typeof e.response === 'undefined') {
      after_create.value = ['Nie udało się połączyć z serwerem.']
      response_status.value = 500
      title.value = 'Problem z serwerem'
      subtitle.value = 'Proszę poczekać, serwer nie jest teraz dostępny.'
    } else {
      const error_response = e.response
      after_create.value = error_response.data.error
      response_status.value = error_response.status
      title.value = 'Problem z danymi'
      subtitle.value = 'Dane przekazane do formularza są błędne. Proszę je poprawić, zgodnie z komunikatami wyświetlanymi poniżej:'
    }
  }
  Object.assign(test, {
    title: '',
    content: {},
    course_id: course.id
  })
}

const deleteTest = async (testId) => {
  try {
    const response = await axios.delete(`http://localhost:5000/tests/${testId}`, test)
    _.remove(tests.value, function (o) {
      return _.isEqual(o, response.data.test)
    })
    title.value = 'Test usunięty pomyślnie'
    subtitle.value = 'Test został trwale usunięty z systemu.'
  } catch (e) {
    if (typeof e.response === 'undefined') {
      after_create.value = ['Nie udało się połączyć z serwerem.']
      response_status.value = 500
      title.value = 'Problem z serwerem'
      subtitle.value = 'Proszę poczekać, serwer nie jest teraz dostępny.'
    } else {
      const error_response = e.response
      after_create.value = error_response.data.error
      response_status.value = error_response.status
      title.value = 'Problem z danymi'
      subtitle.value = 'Dane przekazane do formularza są błędne. Proszę je poprawić, zgodnie z komunikatami wyświetlanymi poniżej:'
    }
  }
}

const addLesson = async () => {
  try {
    const response = await axios.post('http://localhost:5000/lessons', lesson)
    lessons.value.push(response.data.lesson)
    title.value = 'Lekcja dodana pomyślnie'
    subtitle.value = 'Nowa lekcja została utworzona i dodana do listy.'
  } catch (e) {
    if (typeof e.response === 'undefined') {
      after_create.value = ['Nie udało się połączyć z serwerem.']
      response_status.value = 500
      title.value = 'Problem z serwerem'
      subtitle.value = 'Proszę poczekać, serwer nie jest teraz dostępny.'
    } else {
      const error_response = e.response
      after_create.value = error_response.data.error
      response_status.value = error_response.status
      title.value = 'Problem z danymi'
      subtitle.value = 'Dane przekazane do formularza są błędne. Proszę je poprawić, zgodnie z komunikatami wyświetlanymi poniżej:'
    }
  }
  Object.assign(lesson, {
    title: '',
    content: {},
    course_id: course.id
  })
}

const deleteLesson = async (lessonId) => {
  try {
    const response = await axios.delete(`http://localhost:5000/lessons/${lessonId}`, lesson)
    _.remove(lessons.value, function (o) {
      return _.isEqual(o, response.data.lesson)
    })
    title.value = 'Lekcja usunięta pomyślnie'
    subtitle.value = 'Lekcja została trwale usunięta z systemu.'
  } catch (e) {
    if (typeof e.response === 'undefined') {
      after_create.value = ['Nie udało się połączyć z serwerem.']
      response_status.value = 500
      title.value = 'Problem z serwerem'
      subtitle.value = 'Proszę poczekać, serwer nie jest teraz dostępny.'
    } else {
      const error_response = e.response
      after_create.value = error_response.data.error
      response_status.value = error_response.status
      title.value = 'Problem z danymi'
      subtitle.value = 'Dane przekazane do formularza są błędne. Proszę je poprawić, zgodnie z komunikatami wyświetlanymi poniżej:'
    }
  }
}

const resetInputs = () => {
  Object.assign(opinion, {
    title: '',
    content: '',
    score: 0
  })
}

onMounted(async () => {
  await getOpinions()
  await getTestsByCourse()
  await getLessonsByCourse()
  await getTeacherInfo()
  if (user !== null) {
    type.value = (user.hasOwnProperty('specialty') && user.id === course.teacher_id) ? 'teacher' : 'student'
  } else {
    type.value = ''
  }

  if (type.value === 'teacher') {
    student_in_course.value = await getStudentsForCourse()
  }
})
</script>
<template>
  <ResponseOutput
      v-model:response_status="response_status"
      :after_create="after_create"
      v-if="response_status >= 100"
      :title="title"
      :subtitle="subtitle"
  ></ResponseOutput>
  <div class="courses-main" :style="{
    opacity: response_status < 200 ? '1' : '0.3',
    pointerEvents: response_status < 200 ? 'auto' : 'none'
  }">
    <div class="course-header">
      <h2>{{ course.title }}</h2>
      <button type="button" @click="show_shop = true" class="link">
        Kup
      </button>
      <RouterLink to="/courses" class="link">
        Wróć
      </RouterLink>
    </div>
    <div class="courses-intro">
      <div class="course-scope">
        <h3>Zakres kursu</h3>
        <div class="content">
          <span v-for="(sentence, i) in course.description.split('.')" :key="i">{{ sentence }}</span>
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
            <dd>{{ teacher.name }}</dd>
          </div>
        </dl>
      </div>
    </div>
    <div class="course-lessons">
      <h3>Lekcje</h3>
      <div class="lessons">
        <div class="lesson" v-for="(lesson, i) in lessons" :key="i">
          <div class="el">{{ i + 1 }}</div>
          <div class="el">{{ lesson.title }}</div>
          <div
              class="reset-btn"
              @click="deleteLesson(lesson.id)"
              @mouseenter="show_lesson.lesson = 0"
              @mouseleave="show_lesson.lesson = -1"
              v-if="type === 'teacher'"
          >
            <font-awesome-icon :icon="['fas', 'minus']" />
            <span v-if="show_lesson.lesson === 0">Usuń lekcję</span>
          </div>
        </div>
        <div class="lesson" v-if="show_lesson.form === false && type === 'teacher'">
          <div
              class="submit-btn"
              @mouseenter="show_lesson.lesson = 1"
              @mouseleave="show_lesson.lesson = -1"
              @click="show_lesson.form = true"
          >
            <font-awesome-icon :icon="['fas', 'plus']" />
            <span v-if="show_lesson.lesson === 1">Dodaj lekcję</span>
          </div>
        </div>
        <div class="lesson-form" v-if="show_lesson.form === true && type === 'teacher'">
          <form @submit.prevent="addLesson">
            <FormInputText
                :placeholder="'Tytuł testu'"
                v-model:input_value="lesson.title"
            ></FormInputText>

            <div class="info-btn">
              <font-awesome-icon :icon="['fas', 'file-import']" />
              <span>Dodaj plik</span>
            </div>

            <FormButton :reset="true" @redEvent="() => { show_lesson.form = false; show_lesson.lesson = -1 }">
              <template v-slot:green>
                Dodaj lekcję
              </template>
              <template v-slot:red>
                Ukryj
              </template>
            </FormButton>
          </form>
        </div>
      </div>
      <p v-if="_.isEmpty(lessons)"><b>Na ten moment nauczyciel nie dodał żadnych lekcji do kursu!</b></p>
    </div>
    <div class="course-tests">
      <h3>Testy</h3>
      <div class="tests">
        <div class="test" v-for="(test, i) in tests" :key="i">
          <div class="el">{{ i + 1 }}</div>
          <div class="el">{{ test.title }}</div>
          <div
              class="reset-btn"
              @click="deleteTest(test.id)"
              @mouseenter="show_test.test = 0"
              @mouseleave="show_test.test = -1"
              v-if="type === 'teacher'"
          >
            <font-awesome-icon :icon="['fas', 'minus']" />
            <span v-if="show_test.test === 0">Usuń test</span>
          </div>
        </div>
        <div class="test" v-if="show_test.form === false && type === 'teacher'">
          <div
              class="submit-btn"
              @mouseenter="show_test.test = 1"
              @mouseleave="show_test.test = -1"
              @click="show_test.form = true"
          >
            <font-awesome-icon :icon="['fas', 'plus']" />
            <span v-if="show_test.test === 1">Dodaj test</span>
          </div>
        </div>
        <div class="test-form" v-if="show_test.form === true && type === 'teacher'">
          <form @submit.prevent="addTest">
            <FormInputText
                :placeholder="'Tytuł testu'"
                v-model:input_value="test.title"
            ></FormInputText>

            <div class="info-btn">
              <font-awesome-icon :icon="['fas', 'file-import']" />
              <span>Dodaj plik</span>
            </div>

            <FormButton :reset="true" @redEvent="() => { show_test.form = false; show_test.test = -1 }">
              <template v-slot:green>
                Dodaj test
              </template>
              <template v-slot:red>
                Ukryj
              </template>
            </FormButton>
          </form>
        </div>
      </div>
      <p v-if="_.isEmpty(tests)"><b>Na ten moment nauczyciel nie dodał żadnych testów do kursu!</b></p>
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
      <div class="opinions" v-if="!_.isEmpty(opinions)">
        <div class="opinion" v-for="(op, i) in opinions" :key="i">
          <h4 class="opinion-title">{{ op.title }}</h4>
          <p class="opinion-content">{{ op.content }}</p>
          <p class="opinion-score">Ocena: {{ op.score }}/5</p>
        </div>
      </div>
      <p v-else><b>Na ten moment kurs nie posiada opinii!</b></p>
    </div>
    <div class="course-students" v-if="type === 'teacher'">
      <h3>Studenci zapisani do kursu</h3>
      <div class="students" v-if="!_.isEmpty(student_in_course)">
        <div class="student" v-for="(student, i) in student_in_course" :key="i">
          <div class="student-info">
            <p><strong>Id studenta:</strong> {{ student.student_id }}</p>
            <p><strong>Email:</strong> {{ student.email }}</p>
            <p><strong>Imię i nazwisko:</strong> {{ student.name }}</p>
          </div>
          <button type="button" @click="deleteStudentFromCourse(student.student_id)" class="reset-btn">Usuń z kursu</button>
        </div>
      </div>
      <p v-else><b>Na ten moment żaden student nie dołączył do kursu!</b></p>
    </div>
    <Shop
        v-if="show_shop"
        v-model:user="user"
        v-model:students="student_in_course"
        v-model:show_shop="show_shop"
    ></Shop>
  </div>
</template>

<style scoped>
.info-btn, .submit-btn, .reset-btn {
  width: 20%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.test, .lesson {
  width: 80%;
  min-height: 5rem;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  border-top: 2px solid black;
  border-bottom: 2px solid black;
  margin-bottom: 1rem;
}

.test-form, .lesson-form {
  width: 80%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  border-top: 2px solid black;
  border-bottom: 2px solid black;
  padding: 1rem 0 1rem 0;
}

.el {
  width: 33%;
}

.students, .tests, .lessons {
  width: 100%;
  max-height: 300px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.student {
  width: 80%;
  background-color: #ecfdf5;
  border-left: 4px solid #10b981;
  padding: 1rem;
  border-radius: 0.5rem;
  color: #065f46;
}

.opinions {
  height: 100%;
  width: 40%;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow-y: scroll;
}

.opinion {
  width: 80%;
  border: 1px solid #e5e7eb;
  border-radius: 0.75rem;
  padding: 1rem;
  margin: 0.75rem 0;
  background-color: #f9fafb;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.opinion-title {
  font-weight: 600;
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
  color: #111827;
}

.opinion-content {
  font-size: 0.95rem;
  color: #374151;
  margin-bottom: 0.5rem;
}

.opinion-score {
  font-weight: 500;
  color: #2563eb;
}

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
  height: 100vh;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
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
  height: 80vh;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  background-color: white;
  padding: 1.5rem;
  border-radius: 0.75rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.course-lessons, .course-tests, .course-students {
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
.course-opinions h3,
.course-students h3 {
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
