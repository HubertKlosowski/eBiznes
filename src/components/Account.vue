<script setup>
import {useRouter} from "vue-router";
import {inject, ref} from "vue";
import Header from "@/components/Header.vue";

const router = useRouter()
const $cookies = inject('$cookies')

const user = ref(JSON.parse(localStorage.getItem('user')))

const logoutUser = async () => {
  localStorage.clear()
  await router.push('/')
}
</script>

<template>
  <div class="account">
    <Header></Header>
    <div class="header" style="border: none">
      <div class="title">
        <h3>Witaj {{ user['username'] }}!</h3>
      </div>
      <div class="rest">
        <button type="button" class="logout" @click.prevent="logoutUser">Wyloguj się</button>
      </div>
    </div>
    <div class="details">
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
    <div class="user_courses">

    </div>
    <div class="buttons">
      <RouterLink to="/update" class="update">Zmień dane</RouterLink>
      <RouterLink to="/delete" class="delete">Usuń konto</RouterLink>
    </div>
  </div>
</template>

<style scoped>
.account {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-items: center;
  align-items: center;
  background: #f9fafb;
}
</style>