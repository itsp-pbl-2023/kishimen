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
        <div :id="$style.angry" :class="$style.under_stick">
          <div :class="$style.left">
            <p :class="$style.content_text">Angry</p>
          </div>
          <div :class="$style.right">
            <select :class="$style.pulldown">
              <option value="music">Distrubance.mp3</option>
              <option value="music">Red_moon.mp3</option>
              <option value="music">Running_To_The_Way.mp3</option>
              <option value="music">seishishitauchu.mp3</option>
              <option value="music">The_PEAK.mp3</option>
              <option value="music">yume.mp3</option>
            </select>
          </div>
        </div>
        <div :class="$style.under_stick">
          <div :class="$style.left">
            <p :class="$style.content_text">Disgust</p>
          </div>
          <div :class="$style.right">
            <select :class="$style.pulldown">
              <option value="music">Distrubance.mp3</option>
              <option value="music">Red_moon.mp3</option>
              <option value="music">Running_To_The_Way.mp3</option>
              <option value="music">seishishitauchu.mp3</option>
              <option value="music">The_PEAK.mp3</option>
              <option value="music">yume.mp3</option>
            </select>
          </div>
        </div>
        <div :class="$style.under_stick">
          <div :class="$style.left">
            <p :class="$style.content_text">Fear</p>
          </div>
          <div :class="$style.right">
            <select :class="$style.pulldown">
              <option value="music">Distrubance.mp3</option>
              <option value="music">Red_moon.mp3</option>
              <option value="music">Running_To_The_Way.mp3</option>
              <option value="music">seishishitauchu.mp3</option>
              <option value="music">The_PEAK.mp3</option>
              <option value="music">yume.mp3</option>
            </select>
          </div>
        </div>
        <div :class="$style.under_stick">
          <div :class="$style.left">
            <p :class="$style.content_text">happy</p>
          </div>
          <div :class="$style.right">
            <select :class="$style.pulldown">
              <option value="music">Distrubance.mp3</option>
              <option value="music">Red_moon.mp3</option>
              <option value="music">Running_To_The_Way.mp3</option>
              <option value="music">seishishitauchu.mp3</option>
              <option value="music">The_PEAK.mp3</option>
              <option value="music">yume.mp3</option>
            </select>
          </div>
        </div>
        <div :class="$style.under_stick">
          <div :class="$style.left">
            <p :class="$style.content_text">Sad</p>
          </div>
          <div :class="$style.right">
            <select :class="$style.pulldown">
              <option value="music">Distrubance.mp3</option>
              <option value="music">Red_moon.mp3</option>
              <option value="music">Running_To_The_Way.mp3</option>
              <option value="music">seishishitauchu.mp3</option>
              <option value="music">The_PEAK.mp3</option>
              <option value="music">yume.mp3</option>
            </select>
          </div>
        </div>
        <div :class="$style.under_stick">
          <div :class="$style.left">
            <p :class="$style.content_text">Surprise</p>
          </div>
          <div :class="$style.right">
            <select :class="$style.pulldown">
              <option value="music">Distrubance.mp3</option>
              <option value="music">Red_moon.mp3</option>
              <option value="music">Running_To_The_Way.mp3</option>
              <option value="music">seishishitauchu.mp3</option>
              <option value="music">The_PEAK.mp3</option>
              <option value="music">yume.mp3</option>
            </select>
          </div>
        </div>
        <div :class="$style.under_stick">
          <div :class="$style.left">
            <p :class="$style.content_text">Neutral</p>
          </div>

          <div :class="$style.right">
            <div>Selected: {{ selected }}</div>

            <select v-model="selected">
              <option disabled value="">Please select one</option>
              <option>A</option>
              <option>B</option>
              <option>C</option>
            </select>
          </div>
        </div>
        <button
          type="submit"
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
const colors = {
  team_color: '#FF971D',
  white: '#FFFFFF',
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
  if (document !== null) {
    const str = document.getElementById('angry').value
  }
  router.push('main')
}

var angry_music = document.getElementById('angry')
function clickBtn1() {
  const color1 = document.form1.color1

  // 値(数値)を取得
  const num = color1.selectedIndex
  //const num = document.form1.color1.selectedIndex;

  // 値(数値)から値(value値)を取得
  const str = color1.options[num].value
  //const str = document.form1.color1.options[num].value;

  document.getElementById('span1').textContent = str
}
</script>
<style lang="scss" module>
.angry {
  width: auto;
}
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
