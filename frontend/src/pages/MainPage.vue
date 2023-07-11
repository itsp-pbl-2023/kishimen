<template>
  <div :class="$style.container">
    <div :class="$style.content">
      <div :class="$style.video_box">
        <captured-video
          @capture="(newImageBase64: string) => {
            doEmptionEstimate(newImageBase64)
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
          v-if="user_store.get_is_host"
          :class="$style.bottun_play"
          :src="`/bottun_${bottunState}.png`"
          alt="再生ボタン"
          @click="clickBottun"
        />
        <audio
          id="myAudio"
          ref="music"
          :src="`../../public/music/${musicURL}`"
          controls
          hidden
          loop
        ></audio>
        <span :class="$style.space_padding"></span>
      </div>
    </div>

    <div
      style="
        display: flex;
        padding: 10px;
        flex-direction: column;
        text-align: center;
        margin-left: 30px;
        border: 1px solid #333333;
        border-radius: 10px;
      "
    >
      <h4>感情の重みづけ</h4>
      <div>
        Angry: <span id="value">{{ angry_weight }}</span>
      </div>
      <input
        type="range"
        min="0"
        max="1"
        step="0.1"
        value="1"
        @change="change_angry"
      />
      <div>
        Disgust: <span id="value">{{ disgust_weight }}</span>
      </div>
      <input
        type="range"
        min="0"
        max="1"
        step="0.1"
        value="1"
        @change="change_disgust"
      />
      <div>
        Fear: <span id="value">{{ fear_weight }}</span>
      </div>
      <input
        type="range"
        min="0"
        max="1"
        step="0.1"
        value="1"
        @change="change_fear"
      />
      <div>
        Happy: <span id="value">{{ happy_weight }}</span>
      </div>
      <input
        type="range"
        min="0"
        max="1"
        step="0.1"
        value="1"
        @change="change_happy"
      />
      <div>
        Sad: <span id="value">{{ sad_weight }}</span>
      </div>
      <input
        type="range"
        min="0"
        max="1"
        step="0.1"
        value="1"
        @change="change_sad"
      />
      <div>
        Surprise: <span id="value">{{ surprise_weight }}</span>
      </div>
      <input
        type="range"
        min="0"
        max="1"
        step="0.1"
        value="1"
        @change="change_surprise"
      />
      <div>
        Neutral: <span id="value">{{ neutral_weight }}</span>
      </div>
      <input
        type="range"
        min="0"
        max="1"
        step="0.1"
        value="1"
        @change="change_neutral"
      />
    </div>
  </div>
</template>
<script setup lang="ts">
import CapturedVideo from '/@/components/CapturedVideo.vue'
import type { Emotion } from '/@/api/index'
import { musics } from '/@/assets/musics'

import { ref } from 'vue'
import { uploadImageToAPI, getEmotion } from '/@/api/index'
import { useMusicStore, useUserStore } from '/@/store/index'
import { computed } from 'vue'

const store = useMusicStore()
const user_store = useUserStore()

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
  let weight
  let emotion = 'angry' as keyof Emotion
  ;(Object.keys(obj) as (keyof Emotion)[]).forEach(key => {
    if (key === 'angry') weight = angry_weight.value
    else if (key === 'disgust') weight = disgust_weight.value
    else if (key === 'fear') weight = fear_weight.value
    else if (key === 'happy') weight = happy_weight.value
    else if (key === 'sad') weight = sad_weight.value
    else if (key === 'surprise') weight = surprise_weight.value
    else weight = neutral_weight.value

    if (obj[key] * weight > max) {
      max = obj[key] * weight
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

async function doEmptionEstimate(newImageBase64: string) {
  imageBase64.value = newImageBase64
  uploadImage(newImageBase64)
  getAllEmotion()
}

async function uploadImage(newImageBase64: string) {
  const emotion = await uploadImageToAPI(newImageBase64)
}

async function getAllEmotion() {
  if (user_store.get_is_host) {
    const audio = document.getElementById('myAudio')
    const emotion = await getEmotion(user_store.meeting_key)
    if (emotion) {
      selectMusic(emotion)
      music.value?.play()
    }
  }
}

let angry_weight = ref<number>(1)
let disgust_weight = ref<number>(1)
let fear_weight = ref<number>(1)
let happy_weight = ref<number>(1)
let sad_weight = ref<number>(1)
let surprise_weight = ref<number>(1)
let neutral_weight = ref<number>(1)

const change_angry = (event: any) => {
  angry_weight.value = event.target.value
}

const change_disgust = (event: any) => {
  disgust_weight.value = event.target.value
}

const change_fear = (event: any) => {
  fear_weight.value = event.target.value
}

const change_happy = (event: any) => {
  happy_weight.value = event.target.value
}

const change_sad = (event: any) => {
  sad_weight.value = event.target.value
}

const change_surprise = (event: any) => {
  surprise_weight.value = event.target.value
}

const change_neutral = (event: any) => {
  neutral_weight.value = event.target.value
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

input[type='range' i] {
  appearance: auto;
  cursor: default;
  padding: initial;
  border: initial;
  margin: 2px;
  margin-bottom: 20px;
}
</style>
