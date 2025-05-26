import {createRouter, createWebHistory} from "vue-router";

import MainPage from "@/components/MainPage.vue";
import LogIn from "@/components/LogIn.vue";
import Courses from "@/components/Courses.vue";
import Contact from "@/components/Contact.vue";
import Account from "@/components/Account.vue";
import ForgotPassword from "@/components/ForgotPassword.vue";
import Calendar from "@/components/Calendar.vue";

const routes = [
  {
    path: '/', component: MainPage
  },
  {
    path: '/login', component: LogIn
  },
  {
    path: '/account', component: Account
  },
  {
    path: '/forgot_passwd', component: ForgotPassword
  },
  {
    path: '/courses', component: Courses
  },
  {
    path: '/contact', component: Contact
  },
  {
    path: '/calendar', component: Calendar
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from) => {

})

export default router