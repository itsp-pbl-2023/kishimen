<template>
  <div class="d-flex min-vh-100">
    <main class="p-3 min-vh-100">
      <router-view />
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'

const width = ref(window.innerWidth)
const handleResize = () => {
  width.value = window.innerWidth
}
onMounted(() => {
  window.addEventListener('resize', handleResize)
})
onBeforeUnmount(() => {
  window.removeEventListener('resize', handleResize)
})
</script>
