<script setup>
import {ref} from "vue";

const numbers = ref([
  {
    category: 'Liczba uczniów',
    num: 1000
  },
  {
    category: 'Liczba nauczycieli',
    num: 100
  },
  {
    category: 'Liczba zakupionych kursów',
    num: 200
  },
  {
    category: 'Średnia ocena kursów',
    num: '5.1/5'
  },
])
</script>

<template>
  <div class="about_us">
    <h2>O nas</h2>
    <p class="intro">
      EduLeaf to nowoczesna platforma edukacyjna oferująca korepetycje i kursy online dla uczniów szkół podstawowych i średnich.
      Łączymy najlepszych nauczycieli z technologią, aby zapewnić efektywną i elastyczną naukę.
    </p>
    <div class="more">
      <div class="x">
        <h3>Profesjonalizm</h3>
      </div>
      <div class="x">
        <h3>Dokładność</h3>
      </div>
      <div class="x">
        <h3>Rzetelność</h3>
      </div>
    </div>
    <div class="numbers">
      <div class="cat" v-for="el in numbers" :key="el">
        <h3>{{ el.category }}</h3>
        <p v-if="el.category !== 'Średnia ocena kursów'">{{ el.num }}+</p>
        <div class="stars" v-if="el.category === 'Średnia ocena kursów'">
          <p>
            {{ el.num }}
            <font-awesome-icon :icon="['fas', 'star']" v-for="i in 5"/>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.stars {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-content: center;
}

.numbers {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
  padding: 1rem;
}

.cat {
  padding: 0.75rem 1rem;
  background-color: #ecfdf5;
  border-left: 4px solid #10b981;
  border-radius: 6px;
  transition: background-color 0.2s ease;
}

.cat:hover {
  background-color: #d1fae5;
  cursor: pointer;
}

.about_us {
  width: 100%;
  height: auto;
  margin: 0 auto;
  border-top: 2px solid #10b981;
  border-bottom: 2px solid #10b981;
  transition: all 0.3s ease;
  font-size: 1.5vw;
}

h2 {
  margin-bottom: 1rem;
  color: #065f46;
  text-align: center;
}

.intro {
  color: #374151;
  margin-bottom: 1.5rem;
  line-height: 1.6;
  text-align: center;
}

.more {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
  padding: 0;
  margin: 3rem 1.5rem;
  color: #1f2937;
}

.more > .x {
  width: 20%;
  text-align: center;
  font-size: 1rem;
  font-weight: bold;
  padding: 0.75rem 1rem;
  background-color: #ecfdf5;
  border: 4px solid #10b981;
  border-radius: 6px;
  margin-bottom: 0.75rem;
  transition: background-color 0.2s ease;
}

.more .x:hover {
  background-color: #d1fae5;
}
</style>