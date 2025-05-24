<script setup>

import TeacherInfo from "@/components/TeacherInfo.vue";
import AboutUs from "@/components/AboutUs.vue";
import OpinionInfo from "@/components/OpinionInfo.vue";
import CourseInfo from "@/components/CourseInfo.vue";
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
  display: flex;
  flex-direction: column;
}
</style>