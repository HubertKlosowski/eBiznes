<script setup>

import Header from "@/components/Header.vue";
import {computed, onBeforeUnmount, onMounted, ref, watch} from "vue";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";

const today = ref(new Date())
const month = ref(new Date().getMonth() + 1)
const day_names = ref([
  "Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"
])
const month_names = ref([
  "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec",
  "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"
])
let timer = null

const changeDate = (param) => {
  const current = today.value
  const newMonth = current.getMonth() + param
  today.value = new Date(current.getFullYear(), newMonth, 1)
}

const daysInMonth = computed(() => {
  return new Date(today.value.getFullYear(), today.value.getMonth() + 1, 0).getDate()
})

const startOffset = computed(() => {
  const first = new Date(today.value.getFullYear(), today.value.getMonth(), 1).getDay()
  return first === 0 ? 6 : first - 1
})

const calendarDays = computed(() => {
  const total = startOffset.value + daysInMonth.value
  const arr = []
  for (let i = 0; i < total; i++) {
    if (i < startOffset.value) {
      arr.push(null)
    } else {
      arr.push(i - startOffset.value + 1)
    }
  }
  return arr
})

const monthName = computed(() => month_names.value[today.value.getMonth()])
const year = computed(() => today.value.getFullYear())

onMounted(() => {
  timer = setInterval(() => {
    today.value = new Date()
  }, 1000)
})

watch(today, () => {
  const now = new Date()
  if (today.value.getMonth() !== now.getMonth()) {
    clearInterval(timer)
    timer = null
  } else if (!timer) {
    today.value = new Date()
    timer = setInterval(() => {
      today.value = new Date()
    }, 1000)
  }
})

onBeforeUnmount(() => {
  if (timer) clearInterval(timer)
})
</script>

<template>
  <div class="calendar">
    <Header></Header>
    <div class="info">
      <h2>Twój kalendarz</h2>
    </div>
    <div class="arrows">
      <div class="link" @click="changeDate(-1)">
        <font-awesome-icon :icon="['fas', 'arrow-left']" />
      </div>
      <div class="today" v-if="month === new Date().getMonth() + 1">
        <h2>
          {{ String(today.getDate()).padStart(2, '0') }}.
          {{ String(today.getMonth() + 1).padStart(2, '0') }}.
          {{ String(today.getFullYear()).padStart(2, '0') }}
        </h2>
        <h2>
          {{ String(today.getHours()).padStart(2, '0') }}:
          {{ String(today.getMinutes()).padStart(2, '0') }}:
          {{ String(today.getSeconds()).padStart(2, '0') }}
        </h2>
      </div>
      <div class="today" v-else>
        <h2>{{ monthName }} {{ year }}</h2>
      </div>
      <div class="link" @click="changeDate(1)">
        <font-awesome-icon :icon="['fas', 'arrow-right']" />
      </div>
    </div>
    <div class="month">
      <div class="week" style="border: none">
        <div class="day" v-for="i in 7" :key="i">
          {{ day_names[i - 1] }}
        </div>
      </div>
      <div class="week" v-for="(week, i) in 6" :key="i">
        <div class="day" v-for="j in 7" :key="j" :style="{
          backgroundColor: j === 7 ? '#fef2f2' : '#ffffff'
        }">
          <div class="num" :style="{
            color: j === 7 ? '#b91c1c' : '#1f2937',
            fontWeight: '500',
            fontSize: '2vw'
          }">
            {{ calendarDays[(i * 7) + j - 1] || '' }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.num {
  font-weight: bold;
}

.day {
  width: calc(100% / 7);
  height: 100%;
  background-color: white;
  border-top: 2px solid black;
  border-right: 2px solid black;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.week {
  height: 15%;
  background-color: red;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.day:first-of-type {
  border-left: 2px solid black;
}

.week:last-of-type {
  border-bottom: 2px solid black;
}

.month {
  width: 90%;
  height: 50%;
  display: flex;
  flex-direction: column;
  padding: 1rem;
  margin: 1rem;
}

.arrows {
  width: 100%;
  height: 7%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.info {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 10%;
}

.today {
  width: 30%;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
}

.calendar {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-items: center;
  background: #f9fafb;
}
</style>