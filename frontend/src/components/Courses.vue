<script setup>
import {onMounted, reactive, ref, watch} from "vue";
import _ from "lodash";
import FormInputText from "@/components/FormInputText.vue";
import Header from "@/components/Header.vue";
import FormInputSelect from "@/components/FormInputSelect.vue";
import { useRoute, useRouter } from 'vue-router';
import FormButton from "@/components/FormButton.vue";
import axios from "axios";

const router = useRouter()
const route = useRoute()
const courses = ref(JSON.parse(localStorage.getItem('courses')))
const render_courses = ref(null)
const subjects = ref(null)
const filters = reactive({
  subject: '',
  price_range: {
    p_min: null,
    p_max: null
  },
  selected: ''
})

const resetFilters = () => {
  Object.assign(filters, {
    subject: '',
    price_range: {
      p_min: null,
      p_max: null
    },
    selected: ''
  })
}

const filterCourses = () => {
  render_courses.value = courses.value
  if (filters.subject !== '') {
    render_courses.value = _.filter(render_courses.value, function (c) { return c.subject === filters.subject })
  }

  if (filters.price_range.p_min !== null) {
    render_courses.value = _.filter(render_courses.value, function (c) { return c.price >= filters.price_range.p_min })
  }
  if (filters.price_range.p_max !== null) {
    render_courses.value = _.filter(render_courses.value, function (c) { return c.price <= filters.price_range.p_max })
  }

  if (filters.selected === 'Ocena: od najlepszej') {
    render_courses.value = _.orderBy(render_courses.value, ['score'], ['desc'])
  } else if (filters.selected === 'Cena: od najniższej') {
    render_courses.value = _.orderBy(render_courses.value, ['price'], ['asc'])
  } else if (filters.selected === 'Cena: od najwyższej') {
    render_courses.value = _.orderBy(render_courses.value, ['price'], ['desc'])
  }
}

const goToCourse = (i) => {
  router.push(`/courses/${i}`)
}

watch(filters, () => {
  if (filters.price_range.p_min === '') {
    filters.price_range.p_min = null
  } if (filters.price_range.p_max === '') {
    filters.price_range.p_max = null
  }
})

onMounted(() => {
  courses.value = JSON.parse(localStorage.getItem('courses'))
  render_courses.value = courses.value
  subjects.value = _.uniq(_.map(courses.value, 'subject'))
  if (!_.isEmpty(route.query)) {
    filters.subject = route.query.category
    render_courses.value = _.filter(render_courses.value, function (c) { return c.subject === route.query.category })
  }
})
</script>

<template>
  <div class="courses">
    <Header></Header>
    <div class="courses-main">
      <div class="courses-filters">
        <form @submit.prevent="filterCourses">
          <h2>Filtry</h2>
          <h4>Przedmiot</h4>
          <div class="form-row">
            <label :for="sub" v-for="(sub, i) in subjects" :key="sub">
              <input type="radio" :id="sub" :value="sub" v-model="filters.subject">{{ sub }}
            </label>
          </div>
          <h4>Cena</h4>

          <FormInputText
              :label_for="'minimum'"
              :placeholder="'od zł'"
              v-model:input_value="filters.price_range.p_min"
          ></FormInputText>

          <FormInputText
              :label_for="'maximum'"
              :placeholder="'do zł'"
              v-model:input_value="filters.price_range.p_max"
          ></FormInputText>

          <FormInputSelect
              :select_values="['Ocena: od najlepszej', 'Cena: od najwyższej', 'Cena: od najniższej']"
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
              v-if="filters.subject !== ''"
              @click="filters.subject = ''"
          ><font-awesome-icon :icon="['fas', 'circle-xmark']" /> {{ filters.subject }}</span>
          <span
              v-if="filters.price_range.p_min !== null"
              @click="filters.price_range.p_min = null"
          ><font-awesome-icon :icon="['fas', 'circle-xmark']" /> {{ filters.price_range.p_min }}</span>
          <span
              v-if="filters.price_range.p_max !== null"
              @click="filters.price_range.p_max = null"
          ><font-awesome-icon :icon="['fas', 'circle-xmark']" /> {{ filters.price_range.p_max }}</span>
          <span
              v-if="filters.selected !== ''"
              @click="filters.selected = ''"
          ><font-awesome-icon :icon="['fas', 'circle-xmark']" /> {{ filters.selected }}</span>
        </div>
      </div>
      <div class="courses-list">
        <div class="course" v-for="(course, i) in render_courses" :key="course">
          <div class="important_info">
            <h3>{{ course.title }}</h3>
            <span>Cena: {{ course.price }} zł</span>
            <span>Ocena: {{ course.score }}/5</span>
          </div>
          <div @click="goToCourse(course.id)" class="link">
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

.course {
  width: 80%;
  min-height: 25%;
  margin-top: 1rem;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  border: 2px solid black;
}

.course > h3 {
  text-align: center;
}

.courses-list {
  width: 80%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: center;
  overflow-y: scroll;
}

.courses-filters {
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

.courses {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background: #f9fafb;
}

.courses-main {
  height: 80%;
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
</style>