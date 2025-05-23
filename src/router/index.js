import { createMemoryHistory, createRouter } from 'vue-router'

import Main from "@/components/Main.vue";
import Account from "@/components/Account.vue";
import CoursesInfo from "@/components/CoursesInfo.vue";

const routes = [
  { path: '/', component: Main },
  { path: '/account', component: Account }
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router