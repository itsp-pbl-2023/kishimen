<template>
  <h1>{{ msg }}</h1>
  <button @click="increment">count: {{ count }}</button>
  <p>
    Edit <code>components/HelloWorld.vue</code> to test hot module
    <span :class="$style.re">replacement</span>.
  </p>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useStore } from '/@/store'

defineProps({
  msg: {
    type: String,
    required: true
  }
})

const store = useStore()
const count = computed(() => store.countString)
const { increment } = store
</script>

<style lang="scss" module>
.re {
  font-weight: bold;
}
</style>
