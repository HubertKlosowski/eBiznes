<script setup>
import { useRoute } from 'vue-router'
import {onMounted, reactive} from "vue";

const route = useRoute()
const courseId = route.params.id

const course = reactive({
  subject: '',
  title: '',
  desc: '',
  level: '',
  duration: 0,
  max_people: 0,
  price: 0,
  score: 0
})

// ścieżka do backendu
const getCourse = () => {
  Object.assign(course, {
    subject: 'Matematyka',
    title: 'Algebra od podstaw',
    desc: 'Naucz się działań na wyrażeniach algebraicznych, równaniach i układach równań.',
    level: 'beginner',
    duration: 20,
    max_people: 15,
    price: 199,
    score: 3
  })
}

onMounted(() => {
  getCourse()
})
</script>
<template>
  <div class="courses-main">
    <div class="course-header">
      {{ courseId }}
      <RouterLink to="/courses" class="link">
        Wróć
      </RouterLink>
    </div>
    <div class="courses-intro">
      <div class="course-scope">

      </div>
      <div class="course-info">

      </div>
    </div>
    <div class="course-lessons">

    </div>
    <div class="course-tests">

    </div>
    <div class="course-opinions">

    </div>
  </div>
</template>

<style scoped>
.courses-main {
  width: 100%;
  margin: 0 auto;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  background-color: #f9fafb;
  border-radius: 1rem;
  box-shadow: 0 0 12px rgba(0, 0, 0, 0.05);
}

.course-header {
  width: 100%;
  display: flex;
  justify-content: flex-start;
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
