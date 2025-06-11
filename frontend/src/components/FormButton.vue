<script setup>
const props = defineProps(['reset'])

const emits = defineEmits(['redEvent'])
</script>

<template>
  <div class="form-row">
    <button class="submit-btn" :style="{
      width: props.reset ? '40%' : '100%'
    }" type="submit">
      <slot name="green"></slot>
    </button>
    <button
        class="reset-btn"
        @click="emits('redEvent')"
        v-if="props.reset"
        type="button">
      <slot name="red"></slot>
    </button>
  </div>
</template>

<style scoped>
.form-row {
  width: 100%;
  margin-bottom: 1.5rem;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.submit-btn {
  width: 40%;
  margin-top: 1rem;
  padding: 0.75rem 1rem;
  background-color: #10b981;
  color: #fff;
  font-weight: 600;
  font-size: 1rem;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-btn:hover {
  background-color: #059669;
}

.reset-btn {
  width: 40%;
  margin-top: 1rem;
  padding: 0.75rem 1rem;
  background-color: orangered;
  color: #fff;
  font-weight: 600;
  font-size: 1rem;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.reset-btn:hover {
  background-color: #b53300;
}
</style>