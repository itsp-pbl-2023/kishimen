<template>
  <div :class="$style.container">
    <div :class="$style.content">
      <div :class="$style.video_box">
        <captured-video
          @capture="(newImageBase64: string) => {
            imageBase64 = newImageBase64;
            uploadImage(newImageBase64)
          }"
        >
        </captured-video>
      </div>
      <div :class="$style.under_stick">
        <p :class="$style.content_text">音楽名:</p>

        <div :class="$style.bbs">
          <ul>
            <li>{{ musics[musicURL]?.name ?? musicURL }}</li>
            <li></li>
            <li>{{ musics[musicURL]?.name ?? musicURL }}</li>
            <li></li>
            <li>{{ musics[musicURL]?.name ?? musicURL }}</li>
            <li></li>
            <li>{{ musics[musicURL]?.name ?? musicURL }}</li>
            <li></li>
            <li>{{ musics[musicURL]?.name ?? musicURL }}</li>
          </ul>

          <ul>
            <li>{{ musics[musicURL]?.name ?? musicURL }}</li>
            <li></li>
            <li>{{ musics[musicURL]?.name ?? musicURL }}</li>
            <li></li>
            <li>{{ musics[musicURL]?.name ?? musicURL }}</li>
            <li></li>
            <li>{{ musics[musicURL]?.name ?? musicURL }}</li>
            <li></li>
            <li>{{ musics[musicURL]?.name ?? musicURL }}</li>
          </ul>

          <ul>
            <li>{{ musics[musicURL]?.name ?? musicURL }}</li>
            <li></li>
            <li>{{ musics[musicURL]?.name ?? musicURL }}</li>
            <li></li>
            <li>{{ musics[musicURL]?.name ?? musicURL }}</li>
            <li></li>
            <li>{{ musics[musicURL]?.name ?? musicURL }}</li>
            <li></li>
            <li>{{ musics[musicURL]?.name ?? musicURL }}</li>
          </ul>
        </div>

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
          autoplay
          loop
        ></audio>
        <span :class="$style.space_padding"></span>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import CapturedVideo from '/@/components/CapturedVideo.vue'
import type { Emotion } from '/@/api/index'
import { uploadImageToAPI } from '/@/api/index'
import { musics } from '/@/assets/musics'

import { ref } from 'vue'
import { useMusicStore } from '/@/store/index'

const store = useMusicStore()

let imageBase64 = ref<string>()
let musicURL = ref<string>('seishishitauchu.mp3')

const bottunState = ref('stop')
const music = ref<HTMLAudioElement>()
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
      return store.get_music_angry
    case 'disgust':
      return store.get_music_disgust
    case 'fear':
      return store.get_music_fear
    case 'happy':
      return store.get_music_happy
    case 'sad':
      return store.get_music_sad
    case 'surprise':
      return store.get_music_surprise
    case 'neutral':
      return store.get_music_neutral
  }
}

async function uploadImage(newImageBase64: string) {
  const emotion = await uploadImageToAPI(newImageBase64)
  if (emotion) {
    musicURL.value = selectMusic(emotion)
  }
}
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
  margin-left: -50px;
  width: 300px;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
}
.bottun_play {
  height: 65%;
  margin: 0 auto;
  margin-left: 45px;
}
.space_padding {
  margin: 0 1em 0 0;
  width: 350px;
}

.bbs {
  align-items: center;
  display: flex;
  height: 40px;
  line-height: 40px;
  overflow: hidden;
  width: 300px;
  white-space: nowrap;
  margin-left: -70px;
  z-index: 1;
}
.bbs ul {
  animation: flowing 40s linear infinite;
  font-size: 30px;
  transform: translateX(100%);
  margin: 0;
  padding: 0;
}
.bbs ul li {
  display: inline-block;
  padding-right: 10px;
}
@keyframes flowing {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-100%);
  }
}
</style>
