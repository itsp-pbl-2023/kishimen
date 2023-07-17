<template>
  <div :class="$style.container">
    <div :class="$style.content">
      <div :class="$style.middile_container">
        <div :class="$style.video_container">
          <div :class="$style.video_box" :style="{ width: image_width }">
            <captured-video
              @capture="(newImageBase64: string) => {
                doEmptionEstimate(newImageBase64)
              }"
            >
            </captured-video>
          </div>
          <div
            v-for="(img_str, i) in image_list"
            :key="i"
            :class="$style.video_box"
            :style="{ width: image_width }"
          >
            <img :style="{ width: w }" :src="img_str" alt="" />
          </div>
        </div>

        <div v-if="user_store.get_is_host" :class="$style.emotion_bar">
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
      <div :class="$style.under_stick">
        <p :class="$style.content_text">音楽名:</p>
        <div :class="$style.bbs_container">
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
        </div>

        <img
          v-if="user_store.get_is_host"
          :class="$style.bottun_play"
          :src="`/bottun_${bottunState}.png`"
          alt="再生ボタン"
          @click="clickBottun"
        />
        <span
          v-if="user_store.get_is_host"
          :class="$style.meeting_key"
          @click="copyToClipboard"
          @mouseover="showPopup = true"
          @mouseleave="leavePopup"
          @mousemove="updatePopupPosition"
          >{{ user_store.get_meeting_key }}</span
        >
        <div
          v-if="showPopup"
          :class="$style.popup"
          :style="{ top: popupTop + 'px', left: popupLeft + 'px' }"
        >
          {{ copy_text }}
        </div>
        <audio
          v-if="user_store.get_is_host"
          id="myAudio"
          ref="music"
          :src="`../../public/music/${musicURL}`"
          controls
          hidden
          loop
          autoplay
        ></audio>
        <span :class="$style.space_padding"></span>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import CapturedVideo from '/@/components/CapturedVideo.vue'
import type { Emotion } from '/@/api/index'
import { musics } from '/@/assets/musics'

import { onUpdated, ref } from 'vue'
import { uploadImageToAPI, getEmotion, getFaceImage } from '/@/api/index'
import { useMusicStore, useUserStore } from '/@/store/index'

const showPopup = ref(false)
const popupTop = ref(0)
const popupLeft = ref(0)
let copy_text = ref<string>('コピー')
const image_list = ref<string[]>([])
let image_width = ref<string>('100%')
let w = ref('100%')

const store = useMusicStore()
const user_store = useUserStore()

let imageBase64 = ref<string>("")
let musicURL = ref<string>("")

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
  (Object.keys(obj) as (keyof Emotion)[]).forEach(key => {
    if (key === 'angry') weight = angry_weight.value
    else if (key === 'disgust') weight = disgust_weight.value
    else if (key === 'fear') weight = fear_weight.value
    else if (key === 'happy') weight = happy_weight.value
    else if (key === 'sad') weight = sad_weight.value
    else if (key === 'surprise') weight = surprise_weight.value
    else weight = neutral_weight.value

    obj[key] = obj[key] * weight
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

async function doEmptionEstimate(newImageBase64: string) {
  imageBase64.value = newImageBase64
  uploadImage(newImageBase64)
  getAllEmotion()
  if (user_store.get_is_host) {
    let images = []
    const res = await getFaceImage(user_store.get_meeting_key)
    for (const img of res) {
      let temp = 'data:image/png;base64,' + img
      images.push(temp)
    }
    image_list.value = images
    image_width.value =
      (100 / Math.min(1 + image_list.value.length, 3)).toString() + '%'
  }
}

async function uploadImage(newImageBase64: string) {
  const emotion = await uploadImageToAPI(newImageBase64)
}

async function getAllEmotion() {
  if (user_store.get_is_host) {
    const paused = music.value?.paused
    const emotion = await getEmotion(user_store.meeting_key)
    if (emotion) {
      musicURL.value = selectMusic(emotion)

      if (!paused) music.value?.play()
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

const copyToClipboard = () => {
  copy_text.value = 'コピーしました'
  navigator.clipboard.writeText(user_store.get_meeting_key).catch(err => {
    throw err
  })
}

const updatePopupPosition = (event: MouseEvent) => {
  popupTop.value = event.clientY - 100 // カーソルの縦位置に応じて調整
  popupLeft.value = event.clientX - 10 // カーソルの横位置に応じて調整
}

const leavePopup = () => {
  copy_text.value = 'コピー'
  showPopup.value = false
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
  width: 100%;
  height: 100%;
}
.under_stick {
  background-color: orange;
  color: white;
  height: 10%;
  // display: flex;
  // justify-content: center;
  // align-items: center;
  width: 100%;
  position: relative;
  bottom: 0;
}
.content_text {
  display: inline-block;
  font-size: 2.5em;
  margin: 0 0 0 1em;
  // margin-left: -50px;
  // width: 10%;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
  position: absolute;
  top: 50%;
  left: 5%;
  transform: translate(0, -50%);
}
.bottun_play {
  display: inline-block;
  height: 65%;
  margin: 0 auto;
  margin-left: 45px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.space_padding {
  margin: 0 1em 0 0;
  width: 350px;
}
.bbs_container {
  display: inline-block;
  position: absolute;
  width: 40%;
  top: 55%;
  left: 18%;
  transform: translate(0, -50%);
}
.bbs {
  display: flex;
  align-items: center;
  height: 40px;
  width: 60%;
  line-height: 40px;
  overflow: hidden;
  white-space: nowrap;
  // margin-left: -70px;
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

.emotion_bar {
  margin-left: 20px;
  padding: 10px;
  flex-direction: column;
  text-align: center;
  border: 1px solid #333333;
  border-radius: 10px;
  background-color: white;
}
.middile_container {
  display: flex;
  align-items: center;
  width: 95%;
  height: 78%;
  margin: auto;
  background-color: white;
}
.video_container {
  height: 100%;
  flex-grow: 1;
  display: flex;
  align-content: space-around;
  flex-wrap: wrap;
  justify-content: space-between;
}
.member_image {
  object-fit: contain;
  // width: auto;
}
.video_box {
  // width: 100px;
  // height: 100%;
  // flex-grow: 1;
  background-color: white;
  // border: solid black 1px;
  // object-fit: contain;
}
.meeting_key {
  display: inline-block;
  // margin-top: 15%;
  width: 20%;
  // height: 20%;
  font-size: 30px;
  box-shadow: none;
  border-style: solid;
  border-radius: 30px;
  border-color: white;
  transition: 0.5s;
  text-align: center;
  cursor: default;
  position: absolute;
  top: 50%;
  left: 70%;
  transform: translate(0, -50%);
  // width: 100%;
}
.meeting_key:hover {
  background-color: rgba($color: #999, $alpha: 0.5);
}
.popup {
  position: absolute;
  background-color: white;
  padding: 10px;
  border: 1px solid black;
  font-size: 14px;
}
</style>
