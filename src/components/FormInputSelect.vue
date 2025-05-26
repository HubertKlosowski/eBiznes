<script setup>
const props = defineProps(['select_values', 'title'])
const input_value = defineModel('input_value')
</script>

<template>
  <div class="form-row">
    <slot></slot>
    <select v-model="input_value">
      <option disabled value="">Wybierz jedną z opcji</option>
      <option v-for="value in props.select_values" :key="value">{{ value }}</option>
    </select>
  </div>
</template>

<style scoped>
select {
  width: 100%;
  max-width: 300px;
  padding: 0.5rem 1rem;
  border: 2px solid #10b981;
  border-radius: 0.75rem;
  background-color: #ffffff;
  color: #111827;
  font-size: 1rem;
  cursor: pointer;
  transition: border-color 0.3s, box-shadow 0.3s;
  appearance: none;
  background-image: url("data:image/svg+xml;charset=US-ASCII,%3Csvg width='10' height='7' viewBox='0 0 10 7' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M1 1L5 5L9 1' stroke='%2310b981' stroke-width='2'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 1rem center;
  background-size: 1rem;
}

select:focus {
  outline: none;
  border-color: #059669;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.3);
}

.form-row {
  width: 100%;
  margin-bottom: 1.5rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>