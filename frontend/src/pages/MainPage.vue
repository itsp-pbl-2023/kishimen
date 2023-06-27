<template>
  <div :class="$style.container">
    <div :class="$style.content">
      <div :class="$style.video_box">
        <img :src="`data:image/png;base64,${imageBase64}`" />
        <captured-video
          @capture="(newImageBase64: string) => {
            imageBase64 = newImageBase64
            apiResponse = uploadImageToAPI(newImageBase64)
            }"
        >
        </captured-video>
      </div>
      <div :class="$style.under_stick">
        <p :class="$style.content_text">音楽名 情熱大陸aaaaaaaaaaaaaa</p>
        <img
          :class="$style.bottun_play"
          :src="`/bottun_${bottunState}.png`"
          alt="再生ボタン"
          @click="clickBottun"
        />
        <audio
          ref="music"
          :src="`../../public/music/${musicURL}`"
          controls
          hidden
        ></audio>
        <span :class="$style.space_padding"></span>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import CapturedVideo from '/@/components/CapturedVideo.vue'
import { uploadImageToAPI } from '/@/api/index'

import { ref } from 'vue'
const bottunState = ref('play')
const music = ref<HTMLAudioElement>()
type Emotion = {
  angry: number
  disgust: number
  fear: number
  happy: number
  sad: number
  surprise: number
  neutral: number
}
const emotion = {
  angry: 0.18,
  disgust: 0.0,
  fear: 0.07,
  happy: 0.09,
  sad: 0.66,
  surprise: 1.0,
  neutral: 0.01
} as Emotion
let musicURL = selectMusic(emotion)
function clickBottun() {
  if (bottunState.value === 'play') {
    bottunState.value = 'stop'
    music.value?.play()
  } else {
    bottunState.value = 'play'
    music.value?.pause()
  }
}
function selectMusic(obj: Emotion) {
  let max = -1
  let emotion = 'angry' as keyof Emotion
  ;(Object.keys(obj) as (keyof Emotion)[]).forEach(key => {
    if (obj[key] > max) {
      max = obj[key]
      emotion = key
    }
  })
  switch (emotion) {
    case 'angry':
      return 'seishishitauchu.mp3'
    case 'disgust':
      return 'yume.mp3'
    case 'fear':
      return 'seishishitauchu.mp3'
    case 'happy':
      return 'yume.mp3'
    case 'sad':
      return 'seishishitauchu.mp3'
    case 'surprise':
      return 'yume.mp3'
    case 'neutral':
      return 'seishishitauchu.mp3'
  }
}

let imageBase64 = ref<string>()
let apiResponse = ref<object>()
</script>
<style lang="scss" module>
.container {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.content {
  width: 80%;
  height: 90%;
}
.under_stick {
  background-color: orange;
  height: 70px;
  align-items: center;
  display: flex;
  justify-content: center;
}
.video_box {
  width: auto;
  height: auto;
}
.content_text {
  font-size: 2.5em;
  margin: 0 0 0 1em;
  width: 350px;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
}
.bottun_play {
  height: 65%;
  margin: 0 auto;
}
.space_padding {
  margin: 0 1em 0 0;
  width: 350px;
}
</style>
