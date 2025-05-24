<script setup>
import {ref} from "vue";

const show_span = ref(-1)
const courses = ref(['Matematyka', 'Język angielski', 'Język niemiecki', 'Język polski', 'Fizyka', 'Chemia'])
const desc = ref([
    'Kursy od podstawówki po maturę. Zrozumienie zasad, praktyka, egzaminy.',
    'Gramatyka, słownictwo, konwersacje, certyfikaty językowe.',
    'Lekcje z native speakerami. Mówienie, pisanie, czytanie.',
    'Przygotowanie do egzaminów, wypracowania, lektury.',
    'Zrozumiałe wyjaśnienia zjawisk, teoria i zadania.',
    'Reakcje, równania, przygotowanie do egzaminów.'
])
</script>

<template>
  <section class="courses">
    <h2>Nasze kursy</h2>
    <p class="intro">
      Oferujemy szeroki wybór kursów online dostosowanych do różnych poziomów nauczania. Nasi doświadczeni nauczyciele pomagają uczniom zrozumieć trudne zagadnienia, przygotować się do sprawdzianów i egzaminów oraz rozwijać pasję do nauki.
    </p>

    <div class="course-list">
      <div class="course" @mouseover="show_span = i" @mouseleave="show_span = -1" v-for="(el, i) in courses" :key="el">
        <h3>{{ courses[i] }}</h3>
        <div class="desc" v-if="show_span === i">{{ desc[i] }}</div>
        <RouterLink to="/courses" class="link" v-if="show_span === i">
          <font-awesome-icon :icon="['fas', 'arrow-circle-right']" />
        </RouterLink>
      </div>
    </div>
  </section>
</template>

<style scoped>
.link {
  font-size: 2.5vw;
  text-align: center;
  align-content: center;
}

.courses {
  width: auto;
  min-height: 30%;
  margin: 0 auto;
  padding: 3rem 1.5rem;
  background-color: #ffffff;
  border-top: 2px solid #10b981;
  border-bottom: 2px solid #10b981;
  transition: all 0.3s ease;
}

h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #065f46;
  text-align: center;
}

.intro {
  font-size: 1.1rem;
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
  height: 70%;
  display: grid;
  column-gap: 5rem;
  grid-template-columns: 1fr 1fr 1fr;
  justify-content: center;
  justify-items: center;
  align-content: space-evenly;
  padding: 0;
  color: #1f2937;
}

.course-list .course {
  padding: 0.75rem 1rem;
  background-color: #ecfdf5;
  border-left: 4px solid #10b981;
  border-radius: 6px;
  transition: background-color 0.2s ease;
}

.course-list .course:hover {
  background-color: #d1fae5;
  cursor: pointer;
}
</style>
