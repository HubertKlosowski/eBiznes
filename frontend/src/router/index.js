import {createRouter, createWebHistory} from "vue-router";

import MainPage from "@/components/MainPage.vue";
import LogIn from "@/components/LogIn.vue";
import Courses from "@/components/Courses.vue";
import Contact from "@/components/Contact.vue";
import Account from "@/components/Account.vue";
import ForgotPassword from "@/components/ForgotPassword.vue";
import Calendar from "@/components/Calendar.vue";
import Course from "@/components/Course.vue";
import StudentProfile from "@/components/StudentProfile.vue";
import TeacherProfile from "@/components/TeacherProfile.vue";
import UpdateAccount from "@/components/UpdateAccount.vue";
import DeleteAccount from "@/components/DeleteAccount.vue";
import Teachers from "@/components/Teachers.vue";
import Teacher from "@/components/Teacher.vue";

const routes = [
  {
    path: '/account', component: Account,
    children: [{
      path: 'student', component: StudentProfile
    }, {
      path: 'teacher', component: TeacherProfile
    }]
  },
  { path: '/', component: MainPage },
  { path: '/login', component: LogIn },
  { path: '/forgot_passwd', component: ForgotPassword },
  { path: '/courses', component: Courses },
  { path: '/courses/:id', component: Course, props: true },
  { path: '/contact', component: Contact },
  { path: '/calendar', component: Calendar },
  { path: '/update', component: UpdateAccount },
  { path: '/delete', component: DeleteAccount },
  { path: '/teachers', component: Teachers },
  { path: '/teachers/:id', component: Teacher, props: true }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from) => {
  const user = localStorage.getItem('user')
  if ((to.path === '/account/teacher' || to.path === '/account/student') && user === null && from.path !== '/login') {
    return false
  }
})

export default router