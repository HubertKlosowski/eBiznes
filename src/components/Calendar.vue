<script setup>

import Header from "@/components/Header.vue";
import {computed, reactive, ref, watch} from "vue";

const months = ref([
  "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec",
  "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"
])
const dayofweek = ref([
  "Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"
])

const today = ref(new Date().getDate() + ' ' + new Date().getMonth() + ' ' + new Date().getFullYear())
const num_of_days = ref(31)
const c = ref(0)
const choose = reactive({
  year: 0,
  month: 0,
  day: 0
})

const changeView = (param) => {
  if (param.unit === 'year') {
    choose.year = param.value
    c.value = 1
  } else if (param.unit === 'month') {
    choose.month = param.value
    c.value = 2
    calculateNumOfDays()
  } else if (param.unit === 'day') {
    choose.day = param.value
    c.value = 3
  }
}

const calculateNumOfDays = () => {
  if (choose.year % 4 === 0 && choose.month === 1) {
    num_of_days.value = 29
  } else if (choose.year % 4 !== 0 && choose.month === 1) {
    num_of_days.value = 28
  } else {
    num_of_days.value = 31 ? 31 : 10
  }
}

const formattedDate = computed(() => {
  const parts = []
  if (choose.day !== 0) parts.push(choose.day.toString().padStart(2, '0'))
  if (choose.month !== 0) parts.push(months.value[choose.month])
  parts.push(choose.year)
  return parts.join(' ')
})
</script>

<template>
  <div class="calendar">
    <Header></Header>
    <div class="info">
      <div class="cl" v-if="choose.year !== 0">
        <font-awesome-icon :icon="['fas', 'arrow-left']" />
      </div>
      <h2 v-if="choose.year === 0">Twój kalendarz</h2>
      <h2 v-else>
        {{ formattedDate }}
      </h2>
      <div class="cl" v-if="choose.year !== 0">
        <font-awesome-icon :icon="['fas', 'arrow-right']" />
      </div>
    </div>
    <div class="year" v-if="c === 0">
      <div class="element" v-for="rok in 12" @click="changeView({
      unit: 'year',
      value: rok + new Date().getFullYear() - 2
      })">
        <div class="t">
          {{ rok + new Date().getFullYear() - 2 }}
        </div>
        <div class="events">
          <font-awesome-icon :icon="['fas', 'circle-info']" />
          <font-awesome-icon :icon="['fas', 'circle-exclamation']" />
        </div>
      </div>
    </div>
    <div class="month" v-else-if="c === 1">
      <div class="element" v-for="mc in 12" @click="changeView({
      unit: 'month',
      value: mc - 1
      })">
        <div class="t">
          {{ months[mc - 1] }}
        </div>
        <div class="events">
          <font-awesome-icon :icon="['fas', 'circle-info']" />
          <font-awesome-icon :icon="['fas', 'circle-exclamation']" />
        </div>
      </div>
    </div>
    <div class="day" v-else-if="c === 2">
      <div class="element" v-for="d in num_of_days" @click="changeView({
      unit: 'day',
      value: d
      })">
        <div class="t">
          {{ d }}
        </div>
        <div class="events">
          <font-awesome-icon :icon="['fas', 'circle-info']" />
          <font-awesome-icon :icon="['fas', 'circle-exclamation']" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.cl {
  border: 2px solid black;
  padding: 1rem;
  border-radius: 1.5rem;
  font-size: 1.5vw;
}

.events {
  font-size: larger;
}

.element {
  width: 60%;
  height: 60%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  padding: 0.5rem;
  border-radius: 0.5rem;
  border: 2px solid black;
  font-size: 1.5vw;
  cursor: pointer;
  transition: all 0.3s ease;
}

.element:hover {
  transform: scale(1.03);
}

.year, .month, .day {
  width: 100%;
  height: 50%;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  row-gap: 0.5rem;
  column-gap: 0.5rem;
  justify-content: space-between;
  align-items: center;
  place-items: center;
}

.info {
  width: 100%;
  min-height: 15%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-evenly;
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