<script setup>
import {onMounted, ref} from "vue";
import _ from "lodash";

const courses = ref(JSON.parse(localStorage.getItem('courses')))
const meetings = ref(JSON.parse(localStorage.getItem('meetings')))

// ścieżka do backendu
const getNumberofBoughtCourses = () => {

}

// ścieżka do backendu
const getStudentsForCourse = () => {

}

// ścieżka do backendu
const deleteStudentFromCourse = () => {

}

// ścieżka do backendu
const addStudentToCourse = () => {

}

// ścieżka do backendu
const updateCourse = () => {

}

// ścieżka do backendu
const createCourse = () => {

}

// ścieżka do backendu
const deleteCourse = () => {

}

// ścieżka do backendu
const updateMeeting = () => {

}

// ścieżka do backendu
const deleteMeeting = () => {

}

onMounted(() => {
  getNumberofBoughtCourses()
})
</script>

<template>
  <div class="account-user-courses">
    <h2>Utworzone kursy</h2>
    <div class="courses" v-if="!_.isEmpty(courses)">
      <div class="course" v-for="course in courses" :key="course"></div>
    </div>
    <p v-else><b>Na ten moment nie stworzyłeś/aś żadnego kursu!</b></p>
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
.account-header h3 {
  font-size: 1.5rem;
  color: #1f2937;
}

.account-user-courses {
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
  gap: 1rem;
}

.course {
  background-color: #ecfdf5;
  border-left: 4px solid #10b981;
  padding: 1rem;
  border-radius: 0.5rem;
  color: #065f46;
}
</style>