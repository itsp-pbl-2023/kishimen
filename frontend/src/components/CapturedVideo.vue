<template>
  <video ref="video" />
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

const video = ref<HTMLVideoElement>()
onMounted(() => {
  if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices
      .getUserMedia({
        video: true,
        audio: false
      })
      .then(stream => {
        if (video.value && video.value !== null) {
          video.value.srcObject = stream
          video.value.play()
        }
      })
  }
})
</script>

<style lang="scss" module>
video {
  object-fit: contain;
  width: 100%;
  height: 100%;
}
</style>
