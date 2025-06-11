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
</style>