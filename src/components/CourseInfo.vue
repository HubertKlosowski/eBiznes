<script setup>
import {ref} from "vue";

const show_span = ref(-1)
const courses = ref([
  {
    name: 'Matematyka',
    icon: ['fas', 'calculator'],
    desc: 'Kursy od podstawówki po maturę. Zrozumienie zasad, praktyka, egzaminy.'
  },
  {
    name: 'Biologia',
    icon: ['fas', 'dna'],
    desc: 'Anatomia, genetyka, ekologia, przygotowanie do egzaminów.',
  },
  {
    name: 'Język angielski',
    icon: ['fas', 'language'],
    desc: 'Lekcje z native speakerami. Mówienie, pisanie, czytanie.',
  },
  {
    name: 'Informatyka',
    icon: ['fas', 'computer'],
    desc: 'Algorytmy, programowanie, bazy danych, praktyczne projekty.',
  },
  {
    name: 'Fizyka',
    icon: ['fas', 'rocket'],
    desc: 'Zrozumiałe wyjaśnienia zjawisk, teoria i zadania.',
  },
  {
    name: 'Chemia',
    icon: ['fas', 'flask-vial'],
    desc: 'Reakcje, równania, przygotowanie do egzaminów.'
  },
])
</script>

<template>
  <div class="courses">
    <div class="content">
      <h2>Nasze kursy</h2>
      <p class="intro">
        Oferujemy szeroki wybór kursów online dostosowanych do różnych poziomów nauczania.<br>
        Nasi doświadczeni nauczyciele pomagają uczniom zrozumieć trudne zagadnienia, przygotować się do sprawdzianów i egzaminów.
      </p>

      <div class="course-list">
        <div class="course" @mouseover="show_span = i" @mouseleave="show_span = -1" v-for="(el, i) in courses" :key="el">
          <h3>{{ el.name }}</h3>
          <div class="desc" v-if="show_span === i">{{ el.desc }}</div>
          <RouterLink to="/courses" class="link" v-if="show_span === i">
            <font-awesome-icon :icon="el.icon" />
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.content {
  width: 90%;
  height: auto;
  margin: 0 auto;
}

.link {
  width: 20%;
  height: 20%;
  padding: 0.5rem;
  font-size: 2.5vw;
  text-align: center;
  align-content: center;
  border-radius: 1.5rem;
}

.courses {
  width: 100%;
  height: auto;
  margin: 0 auto;
  background-color: #ffffff;
  border-top: 2px solid #10b981;
  border-bottom: 2px solid #10b981;
  transition: all 0.3s ease;
  font-size: 1.25vw;
  padding-top: 1rem;
}

h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #065f46;
  text-align: center;
}

.intro {
  font-size: 1.25vw;
  color: #374151;
  margin-bottom: 1.5rem;
  line-height: 1.6;
  text-align: center;
}

.course {
  width: 75%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}

.course-list {
  width: 100%;
  height: auto;
  display: grid;
  row-gap: 5rem;
  grid-template-columns: 1fr 1fr 1fr;
  justify-content: center;
  justify-items: center;
  align-content: space-evenly;
  padding: 0;
  margin-bottom: 5rem;
  color: #1f2937;
}

.course {
  padding: 0.75rem 1rem;
  background-color: #ecfdf5;
  border-left: 4px solid #10b981;
  border-radius: 6px;
  transition: background-color 0.2s ease;
}

.course:hover {
  background-color: #d1fae5;
  cursor: pointer;
}
</style>
