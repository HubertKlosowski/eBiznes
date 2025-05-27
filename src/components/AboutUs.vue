<script setup>
import {ref} from "vue";

const numbers = ref([
  {
    category: 'Liczba uczniów',
    num: '1000+'
  },
  {
    category: 'Liczba nauczycieli',
    num: '100+'
  },
  {
    category: 'Liczba zakupionych kursów',
    num: '200+'
  },
  {
    category: 'Średnia ocena kursów',
    num: '5.1/5'
  },
])
</script>

<template>
  <div class="about_us">
    <div class="content">
      <h2>O nas</h2>
      <p class="intro">
        EduLeaf to nowoczesna platforma edukacyjna oferująca korepetycje i kursy online dla uczniów szkół podstawowych i średnich.<br>
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
      <h2>Osiągnięcia</h2>
      <div class="numbers">
        <div class="cat" v-for="el in numbers" :key="el">
          <h3>{{ el.category }}</h3>
          <span v-if="el.category !== 'Średnia ocena kursów'">{{ el.num }}</span>
          <div class="stars" v-if="el.category === 'Średnia ocena kursów'">
            {{ el.num }}<font-awesome-icon :icon="['fas', 'star']" v-for="i in 5"/>
          </div>
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
  margin: 2rem;
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
  padding-top: 1rem;
  border-top: 2px solid #10b981;
  border-bottom: 2px solid #10b981;
  transition: all 0.3s ease;
  font-size: 1.25vw;
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