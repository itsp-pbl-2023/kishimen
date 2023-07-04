<template>
  <div :class="$style.container">
    <div :class="$style.content">
      <div
        style="
          padding: 10px;
          margin-left: 210px;
          margin-bottom: 10px;
          width: 60%;
          border: 1px solid #333333;
          border-radius: 10px;
        "
      >
        <div :class="$style.under_stick">
          <div :class="$style.left">
            <p :class="$style.content_text">Angry</p>
          </div>
          <div :class="$style.right">
            <select
              v-model="select_angry"
              :class="$style.pulldown"
              @change="change_angry"
            >
              <option
                v-for="music in musics_angry"
                :key="music.value"
                :value="music.text"
              >
                {{ music.text }}
              </option>
            </select>
          </div>
        </div>

        <div :class="$style.under_stick">
          <div :class="$style.left">
            <p :class="$style.content_text">Disgust</p>
          </div>
          <div :class="$style.right">
            <select
              v-model="select_disgust"
              :class="$style.pulldown"
              @change="change_disgust"
            >
              <option
                v-for="music in musics_disgust"
                :key="music.value"
                :value="music.value"
              >
                {{ music.text }}
              </option>
            </select>
          </div>
        </div>

        <div :class="$style.under_stick">
          <div :class="$style.left">
            <p :class="$style.content_text">Fear</p>
          </div>
          <div :class="$style.right">
            <select
              v-model="select_fear"
              :class="$style.pulldown"
              @change="change_fear"
            >
              <option
                v-for="music in musics_fear"
                :key="music.value"
                :value="music.value"
              >
                {{ music.text }}
              </option>
            </select>
          </div>
        </div>

        <div :class="$style.under_stick">
          <div :class="$style.left">
            <p :class="$style.content_text">happy</p>
          </div>
          <div :class="$style.right">
            <select
              v-model="select_happy"
              :class="$style.pulldown"
              @change="change_happy"
            >
              <option
                v-for="music in musics_happy"
                :key="music.value"
                :value="music.value"
              >
                {{ music.text }}
              </option>
            </select>
          </div>
        </div>

        <div :class="$style.under_stick">
          <div :class="$style.left">
            <p :class="$style.content_text">Sad</p>
          </div>
          <div :class="$style.right">
            <select
              v-model="select_sad"
              :class="$style.pulldown"
              @change="change_sad"
            >
              <option
                v-for="music in musics_sad"
                :key="music.value"
                :value="music.value"
              >
                {{ music.text }}
              </option>
            </select>
          </div>
        </div>

        <div :class="$style.under_stick">
          <div :class="$style.left">
            <p :class="$style.content_text">Surprise</p>
          </div>
          <div :class="$style.right">
            <select
              v-model="select_surprise"
              :class="$style.pulldown"
              @change="change_surprise"
            >
              <option
                v-for="music in musics_surprise"
                :key="music.value"
                :value="music.value"
              >
                {{ music.text }}
              </option>
            </select>
          </div>
        </div>

        <div :class="$style.under_stick">
          <div :class="$style.left">
            <p :class="$style.content_text">Neutral</p>
          </div>
          <div :class="$style.right">
            <select
              v-model="select_neutral"
              :class="$style.pulldown"
              @change="change_neutral"
            >
              <option
                v-for="music in musics_neutral"
                :key="music.value"
                :value="music.value"
              >
                {{ music.text }}
              </option>
            </select>
          </div>
        </div>
        <button
          :class="$style['back-button']"
          @mouseover="btnOver"
          @mouseleave="btnLeave"
          @click="goMainpage"
        >
          Back to Main
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
// import { storeToRefs } from 'pinia'
import { useMusicStore } from '/@/store/index'

const store = useMusicStore()

const select_angry = ref('')
const select_happy = ref('')
const select_fear = ref('')
const select_sad = ref('')
const select_surprise = ref('')
const select_disgust = ref('')
const select_neutral = ref('')

const musics_angry = ref([
  { text: 'Disturbance.mp3', value: 'Disturbance.mp3' },
  { text: 'Red_moon.mp3', value: 'Red_moon.mp3' },
  { text: 'Running_To_The_Way.mp3', value: 'Running_To_The_Way.mp3' },
  { text: 'seishishitauchu.mp3', value: 'seishishitauchu.mp3' },
  { text: 'The_PEAK.mp3', value: 'The_PEAK.mp3' },
  { text: 'yume.mp3', value: 'yume.mp3' }
])

const musics_disgust = ref([
  { text: 'Disturbance.mp3', value: 'Disturbance.mp3' },
  { text: 'Red_moon.mp3', value: 'Red_moon.mp3' },
  { text: 'Running_To_The_Way.mp3', value: 'Running_To_The_Way.mp3' },
  { text: 'seishishitauchu.mp3', value: 'seishishitauchu.mp3' },
  { text: 'The_PEAK.mp3', value: 'The_PEAK.mp3' },
  { text: 'yume.mp3', value: 'yume.mp3' }
])

const musics_fear = ref([
  { text: 'Disturbance.mp3', value: 'Disturbance.mp3' },
  { text: 'Red_moon.mp3', value: 'Red_moon.mp3' },
  { text: 'Running_To_The_Way.mp3', value: 'Running_To_The_Way.mp3' },
  { text: 'seishishitauchu.mp3', value: 'seishishitauchu.mp3' },
  { text: 'The_PEAK.mp3', value: 'The_PEAK.mp3' },
  { text: 'yume.mp3', value: 'yume.mp3' }
])

const musics_happy = ref([
  { text: 'Disturbance.mp3', value: 'Disturbance.mp3' },
  { text: 'Red_moon.mp3', value: 'Red_moon.mp3' },
  { text: 'Running_To_The_Way.mp3', value: 'Running_To_The_Way.mp3' },
  { text: 'seishishitauchu.mp3', value: 'seishishitauchu.mp3' },
  { text: 'The_PEAK.mp3', value: 'The_PEAK.mp3' },
  { text: 'yume.mp3', value: 'yume.mp3' }
])

const musics_sad = ref([
  { text: 'Disturbance.mp3', value: 'Disturbance.mp3' },
  { text: 'Red_moon.mp3', value: 'Red_moon.mp3' },
  { text: 'Running_To_The_Way.mp3', value: 'Running_To_The_Way.mp3' },
  { text: 'seishishitauchu.mp3', value: 'seishishitauchu.mp3' },
  { text: 'The_PEAK.mp3', value: 'The_PEAK.mp3' },
  { text: 'yume.mp3', value: 'yume.mp3' }
])

const musics_surprise = ref([
  { text: 'Disturbance.mp3', value: 'Disturbance.mp3' },
  { text: 'Red_moon.mp3', value: 'Red_moon.mp3' },
  { text: 'Running_To_The_Way.mp3', value: 'Running_To_The_Way.mp3' },
  { text: 'seishishitauchu.mp3', value: 'seishishitauchu.mp3' },
  { text: 'The_PEAK.mp3', value: 'The_PEAK.mp3' },
  { text: 'yume.mp3', value: 'yume.mp3' }
])

const musics_neutral = ref([
  { text: 'Disturbance.mp3', value: 'Disturbance.mp3' },
  { text: 'Red_moon.mp3', value: 'Red_moon.mp3' },
  { text: 'Running_To_The_Way.mp3', value: 'Running_To_The_Way.mp3' },
  { text: 'seishishitauchu.mp3', value: 'seishishitauchu.mp3' },
  { text: 'The_PEAK.mp3', value: 'The_PEAK.mp3' },
  { text: 'yume.mp3', value: 'yume.mp3' }
])

const colors = {
  team_color: '#ff971d',
  white: '#ffffff',
  black: '#000000'
}

const change_angry = (event: any) => {
  store.change_music_angry(event.target.value)
}
const change_happy = (event: any) => {
  store.change_music_happy(event.target.value)
}
const change_disgust = (event: any) => {
  store.change_music_disgust(event.target.value)
}
const change_surprise = (event: any) => {
  store.change_music_surprise(event.target.value)
}
const change_neutral = (event: any) => {
  store.change_music_neutral(event.target.value)
}
const change_sad = (event: any) => {
  store.change_music_sad(event.target.value)
}
const change_fear = (event: any) => {
  store.change_music_fear(event.target.value)
}

const router = useRouter()
const btn_color = ref(colors.white)
const btn_txt_color = ref(colors.black)

const btnOver = () => {
  btn_color.value = colors.team_color
  btn_txt_color.value = colors.white
}

const btnLeave = () => {
  btn_color.value = colors.white
  btn_txt_color.value = colors.black
}

const goMainpage = () => {
  router.push('main')
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
  padding: 0 50px;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
  margin: 0;
}
.bottun_play {
  height: 65%;
  margin: 0 auto;
}

.pulldown {
  height: 65%;
  width: 200px;
  margin: 0;
  font-size: 1.3em;
}
.space_padding {
  margin: 0 1em 0 0;
  width: 350px;
}
.left {
  width: 50%;
  display: flex;
  align-items: center;
  justify-content: right;
}
.right {
  width: 50%;
  display: flex;
  align-items: center;
  justify-content: left;
}
.back-button {
  margin-top: 15%;
  width: 50%;
  height: 20%;
  font-size: 50px;
  box-shadow: none;
  border-style: solid;
  border-radius: 10px;
  border-color: #ff971d;
  transition: 0.5s;
  background-color: v-bind(btn_color);
  color: v-bind(btn_txt_color);
}
</style>
