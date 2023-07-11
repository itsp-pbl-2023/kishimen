<template>
  <div class="container">
    <div class="flex-container">
      <div class="left-side">
        <button
          v-for="(menu, idx) in start_menus"
          :key="idx"
          class="btn new-btn"
          :style="{ backgroundColor: menu.btn_color, color: menu.text_color }"
          @mouseover="btnOver(menu)"
          @mouseleave="btnLeave(menu)"
          @click="goPage(menu.page)"
        >
          {{ menu.titel }}
        </button>
      </div>
      <div class="right-side">
        <img
          src="https://resize2-icotto.k-img.com/RQxND1N0oIB-MMWKyooFxpOYWC3F8fPGoLJVLrpjHSk/rs:fill:1400:934/plain/https://icotto.k-img.com/uploads/press_image/000/09d/87b/image/bc40397be9b6939f256e6655fe46ac64.jpeg"
          alt="きしめん"
          class="image"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { CreateMeeting } from '/@/api/index'
import { useUserStore } from '/@/store/index'

const user_store = useUserStore()

const colors = {
  team_color: '#ff971d',
  white: '#ffffff',
  black: '#000000'
}

type StartMenu = {
  titel: string
  text_color: string
  btn_color: string
  page: string
}
let start_menus = reactive<StartMenu[]>([
  {
    titel: '新規ミーティング',
    text_color: colors.black,
    btn_color: colors.white,
    page: 'create-meeting'
  },
  {
    titel: 'ミーティングに参加',
    text_color: colors.black,
    btn_color: colors.white,
    page: 'join-meeting'
  }
])

const router = useRouter()

const btnOver = (menu: StartMenu) => {
  menu.btn_color = colors.team_color
  menu.text_color = colors.white
}
const btnLeave = (menu: StartMenu) => {
  menu.btn_color = colors.white
  menu.text_color = colors.black
}
const goPage = async (page: string) => {
  if (page === 'create-meeting') {
    await CreateMeeting()
      .then(res => {
        user_store.set_meeting(res.key)
        user_store.set_host()
      })
      .catch(err => {
        throw err
      })
  }
  router.push(page)
}
</script>

<style lang="scss">
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

.left-side {
  padding: 5% 0 5% 0;
  width: 45%;
  height: 90%;
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
.btn {
  margin-top: 15%;
  width: 100%;
  height: 20%;
  font-size: 50px;
  box-shadow: none;
  border-style: solid;
  border-radius: 30px;
  border-color: #ff971d;
  transition: 0.5s;
}
</style>
