<script setup>
import Header from "@/components/Header.vue";

</script>

<template>
  <div class="account">
    <Header></Header>
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

.account-buttons {
  width: 90%;
  background-color: #ffffff;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
  display: flex;
  flex-direction: row;
  gap: 1rem;
  justify-content: center;
  align-items: center;
  margin-bottom: 1rem;
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