import { createMemoryHistory, createRouter } from 'vue-router'

import MainPage from "@/components/MainPage.vue";
import Account from "@/components/Account.vue";

const routes = [
  { path: '/', component: MainPage },
  { path: '/account', component: Account }
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router