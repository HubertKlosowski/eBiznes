<script setup>
import {useRouter} from "vue-router";
import {inject, onMounted, ref} from "vue";
import Header from "@/components/Header.vue";

const router = useRouter()

const user = ref(JSON.parse(localStorage.getItem('user')))
const courses = ref(['xdxdxd'])
const meetings = ref(['xdxdxd'])

const logoutUser = async () => {
  localStorage.clear()
  await router.push('/')
}

// ścieżka do backendu
const getCoursesForUser = () => {
  localStorage.setItem('courses', JSON.stringify(courses))
}

// ścieżka do backendu
const getMeetingsForUser = () => {
  localStorage.setItem('meetings', JSON.stringify(meetings))
}

onMounted(() => {
  getCoursesForUser()
  getMeetingsForUser()
})
</script>

<template>
  <div class="account">
    <Header></Header>
    <div class="account-first-section">
      <div class="account-header">
        <div class="title">
          <h3>Witaj {{ user['username'] }}!</h3>
        </div>
        <div class="rest">
          <button type="button" class="logout" @click.prevent="logoutUser">Wyloguj się</button>
        </div>
      </div>
      <div class="account-details">
        <div class="title">
          <h3>Szczegóły konta</h3>
        </div>
        <div class="rest">
          <div class="info">
            <span style="font-weight: bold">Imię i nazwisko</span>
            <span>{{ user['name'] }}</span>
          </div>
          <div class="info">
            <span style="font-weight: bold">Adres email</span>
            <span>{{ user['email'] }}</span>
          </div>
          <div class="info">
            <span style="font-weight: bold">Poziom edukacji</span>
            <span>{{ user['level'] }}</span>
          </div>
        </div>
      </div>
    </div>
    <RouterView></RouterView>
    <div class="account-buttons">
      <RouterLink to="/update" class="update">Zmień dane</RouterLink>
      <RouterLink to="/delete" class="delete">Usuń konto</RouterLink>
    </div>
  </div>
</template>

<style scoped>
.account {
  width: 100%;
  height: 100vh;
  background-color: #f9fafb;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
  box-sizing: border-box;
}

.account-first-section {
  width: 100%;
  max-width: 1000px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 2rem;
}

.account-header, .account-details {
  flex: 1;
  min-width: 300px;
  background-color: #ffffff;
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.account-header h3 {
  font-size: 1.5rem;
  color: #1f2937;
}

.logout {
  background-color: #ef4444;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.logout:hover {
  background-color: #dc2626;
}

.account-details .info {
  display: flex;
  flex-direction: column;
  margin-bottom: 0.5rem;
  font-size: 1rem;
  color: #374151;
}

.account-user-courses h2 {
  color: #111827;
  font-size: 1.5rem;
}

.account-buttons {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
}

.update, .delete {
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  font-weight: 500;
  transition: all 0.3s ease-in-out;
}

.update {
  background-color: #10b981;
  color: white;
}

.update:hover {
  background-color: #059669;
}

.delete {
  background-color: #f3f4f6;
  border: 1px solid #d1d5db;
  color: #374151;
}

.delete:hover {
  background-color: #e5e7eb;
}
</style>