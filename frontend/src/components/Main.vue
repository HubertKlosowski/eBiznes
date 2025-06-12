<script setup>

import TeacherInfo from "@/components/TeacherInfo.vue";
import AboutUs from "@/components/AboutUs.vue";
import OpinionInfo from "@/components/OpinionInfo.vue";
import CourseInfo from "@/components/CourseInfo.vue";
import axios from "axios";
import {onMounted} from "vue";

const getCourses = async () => {
  try {
    const response = await axios.get('http://localhost:5000/courses')
    localStorage.setItem('courses', JSON.stringify(response.data))
  } catch (e) {
    console.error('Błąd podczas pobierania kursów:', e)
  }
}

onMounted(async () => {
  await getCourses()
})
</script>

<template>
  <div class="main">
    <AboutUs></AboutUs>
    <CourseInfo></CourseInfo>
    <TeacherInfo></TeacherInfo>
    <OpinionInfo></OpinionInfo>
  </div>
</template>

<style scoped>
.main {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
}
</style>