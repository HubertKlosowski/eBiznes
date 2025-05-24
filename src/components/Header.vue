<script setup>

</script>

<template>
  <div class="header">
    <div class="company">
      <RouterLink to="/">
        <img src="/src/assets/eduleaf.jpg" alt="logo EduLeaf">
      </RouterLink>
    </div>
    <div class="account">
      <RouterLink to="/account" class="link">
        <font-awesome-icon :icon="['fas', 'user']" />
      </RouterLink>
    </div>
    <div class="calendar">
      <RouterLink to="/calendar" class="link">
        <font-awesome-icon :icon="['fas', 'calendar']" />
      </RouterLink>
    </div>
  </div>
</template>

<style scoped>
.header {
  width: 100%;
  height: auto;
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
  max-width: 6%;
  padding: 3rem 1.5rem;
  height: auto;
}

.company img {
  width: 100%;
  height: auto;
  object-fit: contain;
  display: block;
  border-radius: 2.5rem;
  border: 0.25rem solid black;
}
</style>