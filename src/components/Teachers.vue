<script setup>

import FormInputSelect from "@/components/FormInputSelect.vue";
import FormButton from "@/components/FormButton.vue";
import Header from "@/components/Header.vue";
import _ from "lodash";
import {onMounted, reactive, ref} from "vue";
import { useRouter } from 'vue-router';


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

  if (filters.selected === 'Długość stażu: od najniższego') {
    render_teachers.value = _.orderBy(render_teachers.value, ['price'], ['asc'])
  } else if (filters.selected === 'Długość stażu: od najwyższego') {
    render_teachers.value = _.orderBy(render_teachers.value, ['price'], ['desc'])
  }
}

// ścieżka do backendu
const getTeachers = () => {
  teachers.value = [
    {
      "teacher_id": "f1a1a1a1-1111-4eaa-aaaa-1111aaaa1111",
      "avatar": "avatar1.jpg",
      "name": "Anna Kowalska",
      "username": "akowalska",
      "email": "anna.kowalska@eduleaf.pl",
      "password": "hashed_password1",
      "specialty": "Matematyka",
      "desc": "Doświadczona nauczycielka matematyki z pasją do nauczania logicznego myślenia.",
      "experience": 8
    },
    {
      "teacher_id": "f2b2b2b2-2222-4ebb-bbbb-2222bbbb2222",
      "avatar": "avatar2.jpg",
      "name": "Krzysztof Nowak",
      "username": "knowak",
      "email": "krzysztof.nowak@eduleaf.pl",
      "password": "hashed_password2",
      "specialty": "Fizyka",
      "desc": "Pasjonat fizyki z ponad 10-letnim doświadczeniem w przygotowaniu do matury rozszerzonej.",
      "experience": 10
    },
    {
      "teacher_id": "f3c3c3c3-3333-4ecc-cccc-3333cccc3333",
      "avatar": "avatar3.jpg",
      "name": "Julia Mazur",
      "username": "jmazur",
      "email": "julia.mazur@eduleaf.pl",
      "password": "hashed_password3",
      "specialty": "Chemia",
      "desc": "Chemiczka z praktycznym podejściem do nauki i wieloletnim doświadczeniem laboratoryjnym.",
      "experience": 7
    },
    {
      "teacher_id": "f4d4d4d4-4444-4edd-dddd-4444dddd4444",
      "avatar": "avatar4.jpg",
      "name": "Łukasz Wilk",
      "username": "lwilk",
      "email": "lukasz.wilk@eduleaf.pl",
      "password": "hashed_password4",
      "specialty": "Język niemiecki",
      "desc": "Germanista i egzaminator TELC, uczy poprzez dialog i autentyczne materiały.",
      "experience": 12
    },
    {
      "teacher_id": "f5e5e5e5-5555-4eee-eeee-5555eeee5555",
      "avatar": "avatar5.jpg",
      "name": "Walentyna Dąbrowska",
      "username": "wdabrowska",
      "email": "walentyna.dabrowska@eduleaf.pl",
      "password": "hashed_password5",
      "specialty": "Matematyka",
      "desc": "Matematyczka z Politechniki Wrocławskiej, ceniona za cierpliwość i skuteczne tłumaczenie.",
      "experience": 9
    },
    {
      "teacher_id": "f6f6f6f6-6666-4eff-ffff-6666ffff6666",
      "avatar": "avatar6.jpg",
      "name": "Marcin Zieliński",
      "username": "mzielinski",
      "email": "marcin.zielinski@eduleaf.pl",
      "password": "hashed_password6",
      "specialty": "Język angielski",
      "desc": "Lektor języka angielskiego, specjalizuje się w konwersacjach i przygotowaniach do FCE/CAE.",
      "experience": 6
    },
    {
      "teacher_id": "f7g7g7g7-7777-4eaa-aaaa-7777aaaa7777",
      "avatar": "avatar7.jpg",
      "name": "Agnieszka Wiśniewska",
      "username": "awisniewska",
      "email": "agnieszka.wisniewska@eduleaf.pl",
      "password": "hashed_password7",
      "specialty": "Język polski",
      "desc": "Filolożka polska z 5-letnim doświadczeniem w pracy z młodzieżą licealną.",
      "experience": 5
    },
    {
      "teacher_id": "f8h8h8h8-8888-4ebb-bbbb-8888bbbb8888",
      "avatar": "avatar8.jpg",
      "name": "Mateusz Baran",
      "username": "mbaran",
      "email": "mateusz.baran@eduleaf.pl",
      "password": "hashed_password8",
      "specialty": "Informatyka",
      "desc": "Programista i nauczyciel informatyki, specjalizuje się w nauce Pythona i algorytmiki.",
      "experience": 4
    },
    {
      "teacher_id": "f9i9i9i9-9999-4ecc-cccc-9999cccc9999",
      "avatar": "avatar9.jpg",
      "name": "Zofia Król",
      "username": "zkrol",
      "email": "zofia.krol@eduleaf.pl",
      "password": "hashed_password9",
      "specialty": "Biologia",
      "desc": "Biolożka z doświadczeniem w pracy laboratoryjnej i pasją do nauczania poprzez eksperymenty.",
      "experience": 6
    },
    {
      "teacher_id": "fa0j0j0j-0000-4edd-dddd-0000dddd0000",
      "avatar": "avatar10.jpg",
      "name": "Tomasz Sienkiewicz",
      "username": "tsienkiewicz",
      "email": "tomasz.sienkiewicz@eduleaf.pl",
      "password": "hashed_password10",
      "specialty": "Historia",
      "desc": "Historyk z powołania, prowadzi interaktywne lekcje z wykorzystaniem źródeł i multimediów.",
      "experience": 11
    }
  ]
  render_teachers.value = teachers.value
  specialties.value = _.uniq(_.map(teachers.value, 'specialty'))
  localStorage.setItem('teachers', JSON.stringify(teachers.value))
}

const goToTeacher = (i) => {
  router.push(`/teachers/${i}`)
}

onMounted(() => {
  getTeachers()
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
        <div class="teacher" v-for="(teacher, i) in render_teachers" :key="teacher">
          <div class="important_info">
            <h3>{{ teacher.name }}</h3>
            <span>Adres mail: {{ teacher.email }}</span>
            <span>Specjalność: {{ teacher.specialty }}</span>
            <span>Długość stażu: {{ teacher.experience }}</span>
          </div>
          <div @click="goToTeacher(i)" class="link">
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