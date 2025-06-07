<script setup>
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";

const input_value = defineModel('input_value')
const show_password = defineModel('show_password')
const props = defineProps(['label_for', 'placeholder', 'label', 'is_passwd'])
</script>

<template>
  <label :for="props.label_for">{{ props.label }}</label>
  <div class="form-row">
    <input
      type="text"
      v-model="input_value"
      :id="props.label_for"
      :placeholder="props.placeholder"
      v-if="props.is_passwd === false || props.is_passwd === undefined"
    />
    <input
      type="password"
      v-model="input_value"
      :id="props.label_for"
      :placeholder="props.placeholder"
      v-else
    >
    <font-awesome-icon
      :icon="['fas', 'eye']"
      class="link"
      v-if="show_password && props.is_passwd === true"
      @click="show_password = !show_password"
    />
    <font-awesome-icon
      :icon="['fas', 'eye-slash']"
      class="link"
      v-else-if="!show_password && props.is_passwd === true"
      @click="show_password = !show_password"
    />
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

input[type="password"] {
  width: 70%;
}

.link {
  width: 5%;
  margin: 0 0 0 1rem;
  padding: 1rem;
}

label {
  font-size: 1.25vw;
  color: #374151;
  text-align: center;
}

input {
  width: 90%;
  padding: 0.75rem 1rem;
  border: 1px solid #d1d5db;
  border-radius: 0.5rem;
  font-size: 1rem;
  outline: none;
  transition: border-color 0.3s ease;
}

input:focus {
  border-color: #10b981;
  box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.2);
}
</style>