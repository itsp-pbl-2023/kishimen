<template>
  <div :class="$style.wrapper">
    <div :class="$style.wrapper2">
      <video ref="video" />
      <canvas ref="canvas" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

const emit = defineEmits(['capture'])

const video = ref<HTMLVideoElement>()
let cameraHeight = 100
let cameraWidth = 100
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
          const trackSetting = stream.getTracks()[0]?.getSettings()
          cameraHeight = trackSetting?.height ?? 100
          cameraWidth = trackSetting?.width ?? 100
        }
      })
  }
})

const canvas = ref<HTMLCanvasElement>()
const captureVideo = () => {
  if (!video.value) return null

  if (canvas.value) {
    canvas.value.height = cameraHeight
    canvas.value.width = cameraWidth
  }
  canvas.value
    ?.getContext('2d')
    ?.drawImage(video.value, 0, 0, cameraWidth, cameraHeight)
  return canvas.value?.toDataURL('image/png').replace(/^.*,/, '')
}
setInterval(() => {
  const imageURL = captureVideo()
  if (imageURL) emit('capture', imageURL)
}, 5000)
</script>

<style lang="scss" module>
.wrapper {
  width: 100%;
  height: 100%;
  object-fit: contain;
}
.wrapper2 {
  position: relative;
  display: inline-block;
}
video {
  position: relative;
  left: 0px;
  top: 0px;
  width: 100%;
  height: 100%;
}
canvas {
  visibility: hidden;
  position: absolute;
  left: 0px;
  top: 0px;
  height: 100%;
  width: 100%;
}
</style>
