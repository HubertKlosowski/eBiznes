import {createRouter, createWebHistory} from "vue-router";

import MainPage from "@/components/MainPage.vue";
import LogIn from "@/components/LogIn.vue";
import Courses from "@/components/Courses.vue";
import Contact from "@/components/Contact.vue";
import Account from "@/components/Account.vue";
import ForgotPassword from "@/components/ForgotPassword.vue";
import Calendar from "@/components/Calendar.vue";
import Course from "@/components/Course.vue";
import Student from "@/components/Student.vue";
import Teacher from "@/components/Teacher.vue";
import UpdateAccount from "@/components/UpdateAccount.vue";
import DeleteAccount from "@/components/DeleteAccount.vue";

const routes = [
  {
    path: '/', component: MainPage
  },
  {
    path: '/login', component: LogIn
  },
  {
    path: '/account', component: Account,
    children: [{
      path: 'student', component: Student
    }, {
      path: 'teacher', component: Teacher
    }]
  },
  {
    path: '/forgot_passwd', component: ForgotPassword
  },
  {
    path: '/courses', component: Courses
  },
  {
    path: '/courses/:id',
    component: Course,
    props: true
  },
  {
    path: '/contact', component: Contact
  },
  {
    path: '/calendar', component: Calendar
  },
  {
    path: '/update', component: UpdateAccount
  },
  {
    path: '/delete', component: DeleteAccount
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from) => {

})

export default router