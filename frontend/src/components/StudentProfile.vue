<script setup>
import {onMounted, reactive, ref} from "vue";
import _ from "lodash";
import {useRouter} from "vue-router";
import axios from "axios";

const router = useRouter()

const user = reactive(JSON.parse(localStorage.getItem('user')))
const courses = ref(JSON.parse(localStorage.getItem('user_courses')))
const meetings = ref(JSON.parse(localStorage.getItem('user_meetings')))

const logoutUser = async () => {
  localStorage.clear()
  await router.push('/')
}

// ścieżka do backendu
const getCoursesForUser = async () => {
  try {
    const response = await axios.get('http://localhost:5000/students/' + user['id'] + '/courses')
    localStorage.setItem('user_courses', JSON.stringify(response.data))
    courses.value = response.data
  } catch (e) {
    console.log(e)
  }
}

// ścieżka do backendu
const getMeetingsForUser = async () => {
  try {
    const response = await axios.get('http://localhost:5000/students/' + user['id'] + '/meetings')
    localStorage.setItem('user_meetings', JSON.stringify(response.data))
    meetings.value = response.data
  } catch (e) {
    console.log(e)
  }
}

onMounted(async () => {
  await getCoursesForUser()
  await getMeetingsForUser()
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
          <span style="font-weight: bold">Poziom edukacji</span>
          <span>{{ user['level'] }}</span>
        </div>
      </div>
    </div>
  </div>
  <div class="account-user-courses">
    <h2>Twoje kursy</h2>
    <div class="courses" v-if="!_.isEmpty(courses)">
      <div class="course" v-for="course in courses" :key="course.id">
        <h3 class="course-title">{{ course.title }}</h3>
        <p><strong>Przedmiot:</strong> {{ course.subject }}</p>
        <p><strong>Opis:</strong> {{ course.description }}</p>
        <p><strong>Poziom:</strong> {{ course.level }}</p>
        <p><strong>Czas trwania:</strong> {{ course.duration }}h</p>
        <p><strong>Cena:</strong> {{ course.price }} zł</p>
        <p><strong>Ocena:</strong> {{ course.score }}/5</p>
      </div>
    </div>
    <p v-else><b>Na ten moment nie zapisałeś/aś się na żaden kurs!</b></p>
  </div>
  <div class="meetings">
    <h2>Twoje spotkania</h2>
    <div class="meetings" v-if="!_.isEmpty(meetings)">
      <div class="course" v-for="course in meetings" :key="course"></div>
    </div>
    <p v-else><b>Na ten moment nie masz żadnego spotkania!</b></p>
  </div>
</template>

<style scoped>
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

.account-user-courses h2 {
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

.account-user-courses h2 {
  color: #111827;
  font-size: 1.5rem;
}

.courses {
  width: 100%;
  max-height: 300px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.course {
  width: 80%;
  background-color: #ecfdf5;
  border-left: 4px solid #10b981;
  padding: 1rem;
  border-radius: 0.5rem;
  color: #065f46;
}
</style>