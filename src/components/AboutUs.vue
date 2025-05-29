<script setup>
import {onMounted, ref} from "vue";

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
    num: 4.99
  },
])

const visibleNumbers = ref([])

onMounted(() => {
  let index = 0
  const interval = setInterval(() => {
    if (index < numbers.value.length) {
      visibleNumbers.value.push(numbers.value[index])
      index++
    } else {
      clearInterval(interval)
    }
  }, 500)
})
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
        <Transition name="left" appear :duration="550">
          <div class="x">
            <h3>Profesjonalizm</h3>
          </div>
        </Transition>
        <Transition name="center" appear :duration="550">
          <div class="x">
            <h3>Dokładność</h3>
          </div>
        </Transition>
        <Transition name="right" appear :duration="550">
          <div class="x">
            <h3>Rzetelność</h3>
          </div>
        </Transition>
      </div>
      <h2>Osiągnięcia</h2>
      <div class="numbers">
        <TransitionGroup name="list" appear>
          <div class="cat" v-for="el in visibleNumbers" :key="el">
            <h3>{{ el.category }}</h3>
            <span v-if="el.category !== 'Średnia ocena kursów'">{{ el.num }}</span>
            <span class="stars" v-if="el.category === 'Średnia ocena kursów'">
              {{ el.num }}<font-awesome-icon :icon="['fas', 'star']" v-for="i in 5"/>
            </span>
          </div>
        </TransitionGroup>
      </div>
    </div>
  </div>
</template>

<style scoped>
.left-enter-from, .left-leave-to {
  transform: translateX(-60px);
  opacity: 0;
}

.right-enter-from, .right-leave-to {
  transform: translateX(60px);
  opacity: 0;
}

.center-enter-from, .center-leave-to {
  transform: translateY(-60px);
  opacity: 0;
}

.list-enter-active span,
.list-leave-active span,
.left-enter-active,
.left-leave-active,
.right-enter-active,
.right-leave-active,
.center-enter-active,
.center-leave-active {
  transition: all 0.7s ease-in-out;
}

.list-enter-from span,
.list-leave-to span {
  transform: translateX(30px);
  opacity: 0;
}

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
  background: linear-gradient(to bottom, #f0fdf4, #ffffff);
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