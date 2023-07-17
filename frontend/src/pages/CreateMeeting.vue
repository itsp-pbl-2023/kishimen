<template>
  <div :class="$style.container">
    <div :class="$style['create-container']">
      <music-setting />
      <button
        :class="$style.btn"
        :style="{ backgroundColor: btn_color, color: text_color }"
        @mouseover="btnOver"
        @mouseleave="btnLeave"
        @click="goMainpage"
      >
        ミーティングを作成
      </button>
      <div :class="$style['top-container']">
        <span
          :class="$style['top-page']"
          :style="{ color: top_page_color }"
          @click="goTopPage"
          @mouseover="top_page_color = colors.black"
          @mouseleave="top_page_color = colors.gray"
        >
          Top page
        </span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '/@/store/index'
import MusicSetting from '/@/components/MusicSetting.vue'

const colors = {
  team_color: '#ff971d',
  white: '#ffffff',
  black: '#000000',
  gray: 'gray'
}

let btn_color = ref<string>(colors.white)
let text_color = ref<string>(colors.black)
let meeting_id = ref<string>()
let top_page_color = ref(colors.gray)
let meeting_key = ref<string>('')
let copy_text = ref<string>('コピー')

const showPopup = ref(false)
const popupTop = ref(0)
const popupLeft = ref(0)

const router = useRouter()
const user_store = useUserStore()

onMounted(() => {
  meeting_key.value = user_store.get_meeting_key
})

const btnOver = () => {
  btn_color.value = colors.team_color
  text_color.value = colors.white
}
const btnLeave = () => {
  btn_color.value = colors.white
  text_color.value = colors.black
}
const goMainpage = () => {
  router.push('main')
}
const goTopPage = () => {
  router.push('start-page')
}
</script>

<style lang="scss" module>
input {
  all: unset;
}
.container {
  width: 100vw;
  height: 100vh;
}

.flex-container {
  display: flex;
  justify-content: space-around;
  width: 100%;
  height: 100%;
}

.create-container {
  margin: auto;
  padding: 2% 0 2% 0;
  width: 45%;
}
.right-side {
  padding: 5% 0 5% 0;
  width: 45%;
  height: 90%;
}

.discription {
  width: 100%;
  height: 50%;
  background-color: white;
}
.image {
  margin-right: 20px;
  margin-top: 100px;
  width: 100%;
  height: 50%;
}
.id-input {
  margin-top: 15%;
  width: 100%;
  height: 20%;
  font-size: 50px;
  box-shadow: none;
  border-style: solid;
  border-radius: 30px;
  border-color: black;
  transition: 0.5s;
  text-align: center;
}
.meeting-key {
  position: relative;
  margin-top: 15%;
  width: 100%;
  height: 20%;
  font-size: 50px;
  box-shadow: none;
  border-style: solid;
  border-radius: 30px;
  border-color: black;
  transition: 0.5s;
  text-align: center;
  cursor: default;
}
.meeting-key:hover {
  background-color: rgba($color: #fff, $alpha: 0.8);
}
.meeting-key span {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
}
.target-element {
  width: 100%;
  height: 100%;
  background-color: lightblue;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  cursor: pointer;
}

.popup {
  position: absolute;
  background-color: white;
  padding: 10px;
  border: 1px solid black;
  font-size: 14px;
}
.btn {
  margin-top: 2%;
  width: 100%;
  height: 20%;
  font-size: 50px;
  box-shadow: none;
  border-style: solid;
  border-radius: 30px;
  border-color: #ff971d;
  transition: 0.5s;
  // background-color: v-bind(btn_color);
  // color: v-bind(text_color);
}
.top-container {
  margin-top: 10px;
}
.top-page {
  margin-top: 5%;
  width: 100%;
  font-size: 30px;
  transition: 0.1s;
  // color: v-bind(top_page_color);
  cursor: default;
}
</style>
