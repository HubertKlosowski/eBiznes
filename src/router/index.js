import {createRouter, createWebHistory} from "vue-router";

import MainPage from "@/components/MainPage.vue";
import LogIn from "@/components/LogIn.vue";
import Courses from "@/components/Courses.vue";
import Contact from "@/components/Contact.vue";

const routes = [
  {
    path: '/', component: MainPage
  },
  {
    path: '/login', component: LogIn
  },
  {
    path: '/courses', component: Courses
  },
  {
    path: '/contact', component: Contact
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router