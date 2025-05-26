<script setup>
import {ref} from "vue";

const username = ref('')

const logIn = () => {

}
</script>

<template>
  <div class="account">
    <form @submit.prevent="logIn">
      <label for="usernamae">

        <input type="text" name="username" v-model="username">
      </label>
    </form>
  </div>
<!--  <RouterLink to="/" class="link">-->
<!--    Wróć-->
<!--  </RouterLink>-->
</template>

<style scoped>

</style>