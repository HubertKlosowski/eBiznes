<script setup>

import TeacherInfo from "@/components/TeacherInfo.vue";
import AboutUs from "@/components/AboutUs.vue";
import Opinions from "@/components/Opinions.vue";
import CoursesInfo from "@/components/CoursesInfo.vue";
</script>

<template>
  <div class="main">
    <AboutUs></AboutUs>
    <CoursesInfo></CoursesInfo>
    <TeacherInfo></TeacherInfo>
    <Opinions></Opinions>
  </div>
</template>

<style scoped>
.main {
  width: 100%;
  display: flex;
  flex-direction: column;
}
</style>