<script setup>
import FormInputSelect from "@/components/FormInputSelect.vue";
import FormButton from "@/components/FormButton.vue";
import Header from "@/components/Header.vue";
import _ from "lodash";
import {onMounted, reactive, ref} from "vue";
import { useRouter } from 'vue-router';
import axios from "axios";


const router = useRouter()
const teachers = ref(null)
const render_teachers = ref(null)
const specialties = ref(null)
const filters = reactive({
  specialty: '',
  name: '',
  selected: ''
})

const resetFilters = () => {
  Object.assign(filters, {
    specialty: '',
    name: '',
    selected: ''
  })
}

const filterCourses = () => {
  render_teachers.value = teachers.value
  if (filters.specialty !== '') {
    render_teachers.value = _.filter(render_teachers.value, function (c) { return c.specialty === filters.specialty })
  }

  if (filters.selected === 'Długość stażu: od najkrótszego') {
    render_teachers.value = _.orderBy(render_teachers.value, ['experience'], ['asc'])
  } else if (filters.selected === 'Długość stażu: od najdłuższego') {
    render_teachers.value = _.orderBy(render_teachers.value, ['experience'], ['desc'])
  }
}

const getTeachers = async () => {
  try {
    const response = await axios.get('http://localhost:5000/teachers')
    teachers.value = response.data
  } catch (e) {
    console.error('Błąd podczas pobierania nauczycieli: ', e)
  }
  render_teachers.value = teachers.value
  specialties.value = _.uniq(_.map(teachers.value, 'specialty'))
  localStorage.setItem('teachers', JSON.stringify(teachers.value))
}

const goToTeacher = (i) => {
  router.push(`/teachers/${i}`)
}

onMounted(async () => {
  await getTeachers()
  console.log(teachers.value)
})
</script>

<template>
  <div class="teachers">
    <Header></Header>
    <div class="teachers-main">
      <div class="teachers-filters">
        <form @submit.prevent="filterCourses">
          <h2>Filtry</h2>
          <h4>Specjalność</h4>
          <div class="form-row">
            <label :for="sub" v-for="(sub, i) in specialties" :key="sub">
              <input type="radio" :id="sub" :value="sub" v-model="filters.specialty">{{ sub }}
            </label>
          </div>

          <FormInputSelect
              :select_values="['Długość stażu: od najwyższego', 'Długość stażu: od najniższego']"
              v-model:input_value="filters.selected"
          >
            <h4>Sortuj</h4>
          </FormInputSelect>

          <FormButton :reset="true" @redEvent="() => { resetFilters() }">
            <template v-slot:green>
              Zastosuj
            </template>
            <template v-slot:red>
              Wyczyść
            </template>
          </FormButton>
        </form>
        <div class="applied-filters">
          <span
              v-if="filters.specialty !== ''"
              @click="filters.specialty = ''"
          ><font-awesome-icon :icon="['fas', 'circle-xmark']" /> {{ filters.specialty }}</span>
          <span
              v-if="filters.selected !== ''"
              @click="filters.selected = ''"
          ><font-awesome-icon :icon="['fas', 'circle-xmark']" /> {{ filters.selected }}</span>
        </div>
      </div>
      <div class="teachers-list">
        <div class="teacher" v-for="(teacher, i) in render_teachers" :key="i">
          <div class="important_info">
            <h3>{{ teacher.name }}</h3>
            <span>Adres mail: {{ teacher.email }}</span>
            <span>Specjalność: {{ teacher.specialty }}</span>
            <span>Długość stażu: {{ teacher.experience }}</span>
          </div>
          <div @click="goToTeacher(teacher.id)" class="link">
            Pokaż szczegóły
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.important_info {
  display: flex;
  flex-direction: column;
  padding: 1rem;
}

.applied-filters {
  display: flex;
  flex-direction: column;
}

.applied-filters > span {
  cursor: pointer;
  border: 2px solid black;
  padding: 0.5rem;
  border-radius: 0.5rem;
}

.form-row:not(:last-child) {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.teacher {
  width: 80%;
  min-height: 25%;
  margin-top: 1rem;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  border: 2px solid black;
}

.teacher > h3 {
  text-align: center;
}

.teachers-list {
  width: 80%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: center;
  overflow-y: scroll;
}

.teachers-filters {
  width: 20%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  border-right: 2px solid #10b981;
  overflow-y: auto;
  padding: 0 1rem 0 1rem;
}

.teachers {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background: #f9fafb;
}

.teachers-main {
  height: 80%;
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
</style>