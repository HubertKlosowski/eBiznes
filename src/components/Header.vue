<script setup>
import {ref} from "vue";

const links = ref([
  {
    route: '/login',
    name: 'Konto',
    icon: ['fas', 'user']
  },
  {
    route: '/calendar',
    name: 'Kalendarz',
    icon: ['fas', 'calendar']
  },
  {
    route: '/courses',
    name: 'Kursy',
    icon: ['fas', 'building-columns']
  },
  {
    route: '/contact',
    name: 'Kontakt',
    icon: ['fas', 'address-book']
  },
])
const show_info = ref(-1)
</script>

<template>
  <div class="header">
    <div class="company">
      <RouterLink to="/">
        <img src="/src/assets/eduleaf.jpg" alt="logo EduLeaf">
      </RouterLink>
    </div>
    <div class="links">
      <RouterLink
          :to="link.route"
          class="link"
          v-for="(link, i) in links"
          :key="link"
          @mouseenter="show_info = i"
          @mouseleave="show_info = -1"
      >
        <font-awesome-icon :icon="link.icon"/>
        <span v-show="show_info === i">{{ link.name }}</span>
      </RouterLink>
    </div>
  </div>
</template>

<style scoped>
.links {
  font-size: 1.25rem;
  text-align: center;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.header {
  width: 100%;
  height: 20vh;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-evenly;
  margin: 0 auto;
  background-color: #ffffff;
  border-top: 2px solid #10b981;
  border-bottom: 2px solid #10b981;
  transition: all 0.3s ease;
}

.company {
  max-width: 5%;
  height: auto;
}

.company img {
  width: 100%;
  height: auto;
  object-fit: contain;
  display: block;
  border-radius: 2.5rem;
  border: 0.25rem solid #10b981;
}
</style>