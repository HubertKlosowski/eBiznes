<script setup>
import {onMounted, reactive, ref} from "vue";
import _ from "lodash";
import {useRouter} from "vue-router";
import axios from "axios";
import AddCourse from "@/components/AddCourse.vue";
import UpdateCourse from "@/components/UpdateCourse.vue";

const router = useRouter()

const user = reactive(JSON.parse(localStorage.getItem('user')))
const courses = ref([])
const meetings = ref([])
const num_bought_courses = ref()
const show_course = ref(false)
const show_meeting = ref(false)
const update_course = reactive({
  description: '',
  duration: 0,
  level: '',
  price: '',
  subject: user.specialty,
  teacher_id: user.id,
  title: ''
})
const show_update_course = ref(false)

const logoutUser = async () => {
  localStorage.clear()
  await router.push('/')
}

// ścieżka do backendu
const getNumberofBoughtCourses = async (teacherId) => {
  try {
    const res = await axios.get(`http://localhost:5000/teachers/${teacherId}/courses/count`)
    num_bought_courses.value = res.data
  } catch (e) {
    console.error('Błąd przy pobieraniu liczby kursów:', e)
    throw e
  }
}

// ścieżka do backendu
const updateCourse = (courseItem) => {
  Object.assign(update_course, courseItem)
  show_update_course.value = true
}

// ścieżka do backendu
const deleteCourse = async (courseId) => {
  try {
    const res = await axios.delete(`http://localhost:5000/courses/${courseId}`)
    _.remove(courses.value, { id: courseId })
  } catch (e) {
    console.error('Błąd przy usuwaniu kursu:', e)
    throw e
  }
}

// ścieżka do backendu
const updateMeeting = async (meetingId, meetingData) => {
  try {
    const res = await axios.put(`http://localhost:5000/meetings/${meetingId}`, meetingData)
    return res.data
  } catch (e) {
    console.error('Błąd przy aktualizacji spotkania:', e)
    throw e
  }
}

// ścieżka do backendu
const deleteMeeting = async (meetingId) => {
  try {
    const res = await axios.delete(`http://localhost:5000/meetings/${meetingId}`)
    return res.data
  } catch (e) {
    console.error('Błąd przy usuwaniu spotkania:', e)
    throw e
  }
}

// ścieżka do backendu
const getCoursesForUser = async () => {
  try {
    const response = await axios.get('http://localhost:5000/teachers/' + user['id'] + '/courses')
    courses.value = response.data
  } catch (e) {
    console.log(e)
  }
}

// ścieżka do backendu
const getMeetingsForUser = async () => {
  try {
    const response = await axios.get('http://localhost:5000/teachers/' + user['id'] + '/meetings')
    meetings.value = response.data
  } catch (e) {
    console.log(e)
  }
}

onMounted(() => {
  getCoursesForUser()
  getMeetingsForUser()
  getNumberofBoughtCourses(user.id)
})
</script>

<template>
  <div class="account-first-section">
    <div class="account-header">
      <div class="title">
        <h3>Witaj {{ user['username'] }}!</h3>
      </div>
      <div class="rest">
        <button type="button" class="logout" @click.prevent="logoutUser">Wyloguj się</button>
      </div>
    </div>
    <div class="account-details">
      <div class="title">
        <h3>Szczegóły konta</h3>
      </div>
      <div class="rest">
        <div class="info">
          <span style="font-weight: bold">Imię i nazwisko</span>
          <span>{{ user['name'] }}</span>
        </div>
        <div class="info">
          <span style="font-weight: bold">Adres email</span>
          <span>{{ user['email'] }}</span>
        </div>
        <div class="info">
          <span style="font-weight: bold">Długość stażu</span>
          <span>{{ user['experience'] }} lat</span>
        </div>
        <div class="info">
          <span style="font-weight: bold">Specjalność</span>
          <span>{{ user['specialty'] }}</span>
        </div>
      </div>
    </div>
  </div>
  <div class="account-user-courses">
    <h2>Utworzone kursy</h2>
    <div class="courses" v-if="!_.isEmpty(courses)">
      <div class="course" v-for="(courseItem, i) in courses" :key="i">
        <div class="course-header">
          <h4 class="course-title">{{ courseItem.title }}</h4>
          <div class="course-actions">
            <button @click.prevent="updateCourse(courseItem)" class="submit-btn">Edytuj</button>
            <button @click.prevent="deleteCourse(courseItem.id)" class="reset-btn">Usuń</button>
            <button @click.prevent="router.push('/courses/' + courseItem.id)" class="info-btn">Pokaż szczegóły</button>
          </div>
        </div>
        <p class="course-subject"><strong>Przedmiot:</strong> {{ courseItem.subject }}</p>
        <p class="course-description" v-if="courseItem.description"><strong>Opis:</strong> {{ courseItem.description }}</p>
        <p class="course-description" v-else>Brak opisu kursu!</p>
        <div class="course-details">
          <p class="course-level"><strong>Poziom:</strong> {{ courseItem.level }}</p>
          <p class="course-duration"><strong>Czas:</strong> {{ courseItem.duration }}h</p>
          <p class="course-price"><strong>Cena:</strong> {{ courseItem.price }} zł</p>
          <p class="course-score"><strong>Ocena:</strong> {{ courseItem.score }}/5</p>
          <p class="course-score"><strong>Ilość zapisów:</strong> {{ (_.find(num_bought_courses, ['course_id', courseItem.id]) || { count: 0 }).count }} </p>
        </div>
      </div>
    </div>
    <p v-else><b>Na ten moment nie stworzyłeś/aś żadnego kursu!</b></p>
    <UpdateCourse
        v-if="show_update_course"
        v-model:courses="courses"
        v-model:update_course="update_course"
        v-model:user="user"
        v-model:show_update_course="show_update_course"
    ></UpdateCourse>
    <AddCourse
        v-if="show_course"
        v-model:courses="courses"
        v-model:user="user"
        v-model:show_course="show_course"
    ></AddCourse>
    <button type="button" class="link" @click="show_course = true">Dodaj kurs</button>
  </div>
  <div class="meetings">
    <h2>Twoje spotkania</h2>
    <div class="meetings" v-if="!_.isEmpty(meetings)">
      <div class="course" v-for="course in meetings" :key="course"></div>
    </div>
    <p v-else><b>Na ten moment nie masz żadnego spotkania!</b></p>
    <button type="button" class="link" @click="show_meeting = true">Dodaj spotkanie</button>
  </div>
</template>

<style scoped>
.course-description {
  color: #6b7280;
  margin-bottom: 1rem;
  line-height: 1.4;
}

.course-details {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.course-details span {
  padding: 0.25rem 0.5rem;
  background-color: #e5e7eb;
  border-radius: 0.375rem;
  font-size: 0.8rem;
  font-weight: 500;
  color: #374151;
}

.course-actions {
  width: 80%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.account-first-section {
  width: 100%;
  max-width: 1000px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 2rem;
}

.account-header, .account-details {
  flex: 1;
  min-width: 300px;
  background-color: #ffffff;
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.account-header h3 {
  font-size: 1.5rem;
  color: #1f2937;
}

.logout {
  background-color: #ef4444;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.logout:hover {
  background-color: #dc2626;
}

.account-details .info {
  display: flex;
  flex-direction: column;
  margin-bottom: 0.5rem;
  font-size: 1rem;
  color: #374151;
}

.account-user-courses h2, .meetings h2 {
  color: #111827;
  font-size: 1.5rem;
}

.account-user-courses, .meetings {
  width: 90%;
  background-color: #ffffff;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
  display: flex;
  flex-direction: column;
  gap: 1rem;
  align-items: flex-start;
}

.courses {
  width: 100%;
  max-height: 300px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.course {
  background-color: #ecfdf5;
  border-left: 4px solid #10b981;
  padding: 1rem;
  border-radius: 0.5rem;
  color: #065f46;
}

.submit-btn, .reset-btn, .info-btn {
  width: 30%;
}
</style>