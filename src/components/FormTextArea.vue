<script setup>
const input_value = defineModel('input_value')
const props = defineProps(['label_for', 'placeholder', 'label'])
</script>

<template>
  <label :for="props.label_for">{{ props.label }}</label>
  <div class="form-row">
    <textarea
        v-model="input_value"
        rows="3"
        :id="props.label_for"
        :placeholder="props.placeholder"
    ></textarea>
  </div>
</template>

<style scoped>
.form-row {
  width: 100%;
  margin-bottom: 1.5rem;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

label {
  font-size: 1.25vw;
  color: #374151;
  text-align: center;
}

textarea {
  width: 90%;
  padding: 0.75rem 1rem;
  border: 1px solid #d1d5db;
  border-radius: 0.5rem;
  font-size: 1rem;
  outline: none;
  transition: border-color 0.3s ease;
}

textarea:focus {
  border-color: #10b981;
  box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.2);
}
</style>