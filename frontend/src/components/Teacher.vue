<script setup>
import { useRoute } from 'vue-router'
import {onMounted, reactive, ref} from "vue";
import _ from "lodash";
import FormInputText from "@/components/FormInputText.vue";
import FormInputSelect from "@/components/FormInputSelect.vue";
import FormButton from "@/components/FormButton.vue";
import FormTextArea from "@/components/FormTextArea.vue";
import axios from "axios";

const route = useRoute()
const teacherId = route.params.id

const teacher = reactive(_.find(JSON.parse(localStorage.getItem('teachers')), ['id', teacherId]))
const opinions = ref(null)
const opinion = reactive({
  title: '',
  content: '',
  score: 0
})

const resetInputs = () => {
  Object.assign(opinion, {
    title: '',
    content: '',
    score: 0
  })
}
</script>
<template>
  <div class="teacher-main">
    <div class="teacher-header">
      <h2>Profil nauczyciela {{ teacher.name }}</h2>
      <RouterLink to="/teachers" class="link">
        Wróć
      </RouterLink>
    </div>
    <div class="courses-intro">
      <div class="course-scope">
        <h3>Opis nauczyciela</h3>
        <div class="content">
          <span v-for="(sentence, i) in teacher.description.split('.')" :key="i">{{ sentence }}</span>
        </div>
      </div>
      <div class="teacher-info">
        <h3>Dane ogólne</h3>
        <dl>
          <div class="info-item">
            <dt>Imię i nazwisko</dt>
            <dd>{{ teacher.name }}</dd>
          </div>
          <div class="info-item">
            <dt>Adres email</dt>
            <dd>{{ teacher.email }}</dd>
          </div>
          <div class="info-item">
            <dt>Długość stażu</dt>
            <dd>{{ teacher.experience }} lat</dd>
          </div>
          <div class="info-item">
            <dt>Specjalność</dt>
            <dd>{{ teacher.specialty }}</dd>
          </div>
        </dl>
      </div>
    </div>
  </div>
</template>

<style scoped>
.teacher-main {
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

.teacher-header {
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

.teacher-info, .course-scope {
  width: 40%;
  background-color: #f0fdf4;
  padding: 1.5rem;
  border-radius: 1rem;
  border-left: 4px solid #10b981;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
}

.teacher-info h3 {
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
</style>
