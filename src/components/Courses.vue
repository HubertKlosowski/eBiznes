<script setup>
import {onMounted, reactive, ref, watch} from "vue";
import _ from "lodash";
import FormInputText from "@/components/FormInputText.vue";
import Header from "@/components/Header.vue";
import FormInputSelect from "@/components/FormInputSelect.vue";
import { useRoute, useRouter } from 'vue-router';
import FormButton from "@/components/FormButton.vue";

const router = useRouter()
const route = useRoute()
const courses = ref(null)
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

// ścieżka do backendu
const getCourses = () => {
  courses.value = [// MATEMATYKA
  {
    subject: 'Matematyka',
    title: 'Algebra od podstaw',
    desc: 'Naucz się działań na wyrażeniach algebraicznych, równaniach i układach równań.',
    level: 'liceum',
    duration: 20,
    price: 199,
    score: 3
  },
  {
    subject: 'Matematyka',
    title: 'Analiza matematyczna I',
    desc: 'Granice, ciągłość, pochodne i całki funkcji jednej zmiennej.',
    level: 'studia',
    duration: 30,
    price: 249,
    score: 1
  },
  {
    subject: 'Matematyka',
    title: 'Geometria analityczna',
    desc: 'Proste, okręgi i krzywe w układzie współrzędnych.',
    level: 'liceum',
    duration: 18,
    price: 189,
    score: 5
  },
  {
    subject: 'Matematyka',
    title: 'Kurs z kombinatoryki i rachunku prawdopodobieństwa',
    desc: 'Wprowadzenie do permutacji, kombinacji i pojęć prawdopodobieństwa.',
    level: 'studia',
    duration: 22,
    price: 229,
    score: 1
  },
  {
    subject: 'Matematyka',
    title: 'Matematyka dla maturzystów',
    desc: 'Powtórka całego materiału z matematyki do matury.',
    level: 'technikum',
    duration: 40,
    price: 299,
    score: 4
  },

  // FIZYKA
  {
    subject: 'Fizyka',
    title: 'Mechanika klasyczna',
    desc: 'Kinematyka, dynamika, energia i pęd – od podstaw.',
    level: 'liceum',
    duration: 25,
    price: 219,
    score: 2
  },
  {
    subject: 'Fizyka',
    title: 'Elektryczność i magnetyzm',
    desc: 'Pola elektryczne, napięcie, prąd i zjawiska magnetyczne.',
    level: 'studia',
    duration: 28,
    price: 239,
    score: 5
  },
  {
    subject: 'Fizyka',
    title: 'Fizyka kwantowa w pigułce',
    desc: 'Podstawy mechaniki kwantowej dla uczniów i studentów.',
    level: 'technikum',
    duration: 30,
    price: 299,
    score: 1
  },
  {
    subject: 'Fizyka',
    title: 'Fizyka do matury',
    desc: 'Intensywny kurs przygotowawczy z teorii i zadań maturalnych.',
    level: 'technikum',
    duration: 35,
    price: 269,
    score: 3
  },
  {
    subject: 'Fizyka',
    title: 'Termodynamika i fale',
    desc: 'Zrozumienie ciepła, pracy, fali dźwiękowych i ich zastosowań.',
    level: 'studia',
    duration: 24,
    price: 229,
    score: 1
  },

  // CHEMIA
  {
    subject: 'Chemia',
    title: 'Chemia ogólna',
    desc: 'Atomy, związki chemiczne, reakcje i prawa chemiczne.',
    level: 'liceum',
    duration: 20,
    price: 199,
    score: 1
  },
  {
    subject: 'Chemia',
    title: 'Chemia organiczna',
    desc: 'Związki węgla, grupy funkcyjne i reakcje organiczne.',
    level: 'studia',
    duration: 30,
    price: 249,
    score: 2
  },
  {
    subject: 'Chemia',
    title: 'Chemia analityczna',
    desc: 'Metody oznaczania składu chemicznego substancji.',
    level: 'technikum',
    duration: 28,
    price: 259,
    score: 3
  },
  {
    subject: 'Chemia',
    title: 'Chemia do matury',
    desc: 'Przygotowanie do egzaminu maturalnego z chemii.',
    level: 'technikum',
    duration: 32,
    price: 279,
    score: 5
  },
  {
    subject: 'Chemia',
    title: 'Chemia fizyczna',
    desc: 'Termochemia, kinetyka chemiczna, równowaga i elektrochemia.',
    level: 'studia',
    duration: 26,
    price: 239,
    score: 4
  },

  // BIOLOGIA
  {
    subject: 'Biologia',
    title: 'Biologia komórki',
    desc: 'Budowa i funkcje komórek prokariotycznych i eukariotycznych.',
    level: 'liceum',
    duration: 20,
    price: 189,
    score: 4
  },
  {
    subject: 'Biologia',
    title: 'Genetyka',
    desc: 'Dziedziczenie cech, DNA, RNA i inżynieria genetyczna.',
    level: 'studia',
    duration: 25,
    price: 239,
    score: 3.5
  },
  {
    subject: 'Biologia',
    title: 'Biologia człowieka',
    desc: 'Układy narządów, homeostaza, fizjologia człowieka.',
    level: 'studia',
    duration: 24,
    price: 229,
    score: 1.7
  },
  {
    subject: 'Biologia',
    title: 'Ekologia i ewolucja',
    desc: 'Zasady ekologii, dobór naturalny, mechanizmy ewolucyjne.',
    level: 'liceum',
    duration: 22,
    price: 219,
    score: 2.5
  },
  {
    subject: 'Biologia',
    title: 'Biologia do matury',
    desc: 'Powtórzenie materiału z biologii do egzaminu maturalnego.',
    level: 'technikum',
    duration: 35,
    price: 279,
    score: 4.5
  }
]
  render_courses.value = courses.value
  subjects.value = _.uniq(_.map(courses.value, 'subject'))
  localStorage.setItem('courses', JSON.stringify(courses.value))
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
  getCourses()
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

          <FormButton :reset="false">
            <template v-slot:green>
              Zastosuj
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
          <div @click="goToCourse(i)" class="link">
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

.submit-btn {
  margin-bottom: 1rem;
}

.form-row {
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