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
        <music-setting />
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
import MusicSetting from '/@/components/MusicSetting.vue'

const colors = {
  team_color: '#ff971d',
  white: '#ffffff',
  black: '#000000'
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
