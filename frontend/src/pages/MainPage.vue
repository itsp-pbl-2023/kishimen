<template>
  <div :class="$style.container">
    <div :class="$style.content">
      <div :class="$style.video_box">
        <img :src="imageURL" />
        <captured-video @capture="setImage"> </captured-video>
      </div>
      <div :class="$style.under_stick">
        <p :class="$style.content_text">音楽名 情熱大陸aaaaaaaaaaaaaa</p>
        <img
          :class="$style.bottun_play"
          :src="`/bottun_${bottunState}.png`"
          alt="再生ボタン"
          @click="clickBottun"
        />
        <span :class="$style.space_padding"></span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import CapturedVideo from '/@/components/CapturedVideo.vue'
import { ref } from 'vue'
const bottunState = ref('play')

function clickBottun() {
  if (bottunState.value === 'play') {
    bottunState.value = 'stop'
  } else {
    bottunState.value = 'play'
  }
}

let imageURL = ref<string>()
const setImage = (newImageURL: string) => {
  imageURL.value = newImageURL
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
