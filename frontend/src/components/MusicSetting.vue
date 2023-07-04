<template>
  <div
    v-for="(content, key) in emotionList"
    :key="key"
    :class="$style.under_stick"
  >
    <div :class="$style.left">
      <p :class="$style.content_text">{{ content }}</p>
    </div>
    <div :class="$style.right">
      <select :class="$style.pulldown" @change="change_handler(key)">
        <option v-for="music in musicList" :key="music.url" :value="music.url">
          {{ music.name }}
        </option>
      </select>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useMusicStore } from '/@/store/index'
import { musics } from '/@/assets/musics'

const store = useMusicStore()

const musicList = Object.entries(musics).map(([url, { name }]) => ({
  url,
  name
}))
const emotionList = {
  angry: 'Angry',
  disgust: 'Disgust',
  fear: 'Fear',
  happy: 'Happy',
  sad: 'Sad',
  surprise: 'Surprise',
  neutral: 'Neutral'
}

const change_handler = (key: keyof typeof emotionList) => {
  return (event: Event) => {
    if (!event.target || !(event.target instanceof HTMLSelectElement)) return

    switch (key) {
      case 'angry':
        store.change_music_angry(event.target.value)
        break
      case 'disgust':
        store.change_music_disgust(event.target.value)
        break
      case 'fear':
        store.change_music_fear(event.target.value)
        break
      case 'happy':
        store.change_music_happy(event.target.value)
        break
      case 'sad':
        store.change_music_sad(event.target.value)
        break
      case 'surprise':
        store.change_music_surprise(event.target.value)
        break
      case 'neutral':
        store.change_music_neutral(event.target.value)
        break
    }
  }
}
</script>

<style lang="scss" module>
.under_stick {
  height: 70px;
  align-items: center;
  display: flex;
  justify-content: center;
}
.content_text {
  font-size: 2.5em;
  padding: 0 50px;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
  margin: 0;
}

.pulldown {
  height: 65%;
  width: 200px;
  margin: 0;
  font-size: 1.3em;
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
</style>
