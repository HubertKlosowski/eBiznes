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

const route = useRoute()
const courseId = route.params.id

const course = reactive(_.find(JSON.parse(localStorage.getItem('courses')), ['id', courseId]))
const teacher = reactive({
  name: '',
  username: ''
})
const lessons = ref(null)
const opinions = ref(null)
const tests = ref(null)
const opinion = reactive({
  title: '',
  content: '',
  score: 0
})

const user = reactive(JSON.parse(localStorage.getItem('user')))
const type = ref((user.specialty !== undefined && user.id === course.teacher_id) ? 'teacher' : 'student')
const student_in_course = ref([])
const show_shop = ref(false)

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
    lessons.value = res.data
  } catch (e) {
    console.error('Błąd przy pobieraniu lekcji:', e)
  }
}

const getTestsByCourse = async () => {
  try {
    const res = await axios.get(`http://localhost:5000/courses/${course.id}/tests`)
    tests.value = res.data
  } catch (e) {
    console.error('Błąd przy pobieraniu testów:', e)
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
  if (type.value === 'teacher') {
    student_in_course.value = await getStudentsForCourse()
  }
})
</script>
<template>
  <div class="courses-main">
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
.students {
  width: 100%;
  max-height: 300px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
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
