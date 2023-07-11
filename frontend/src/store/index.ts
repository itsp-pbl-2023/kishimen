import { defineStore } from 'pinia'

export const useStore = defineStore('pinia', {
  state: () => ({
    count: 0
  }),
  getters: {
    countString(state) {
      if (state.count === 0) return 'zero'
      if (state.count === 1) return 'once'
      return `${state.count} times`
    }
  },
  actions: {
    increment() {
      this.count++
    }
  }
})

export const useMusicStore = defineStore('musics', {
  state: () => {
    return {
      music_angry: 'ikarinotettui.mp3',
      music_fear: 'akumasyoukan.mp3',
      music_surprise: 'Hey_Bob_Lets_Dance.mp3',
      music_happy: 'Resilient_Sailors.mp3',
      music_sad: 'kataomoi.mp3',
      music_neutral: 'reijounohimitu.mp3',
      music_disgust: 'iyanayokan.mp3'
    }
  },

  getters: {
    get_music_angry(state) {
      return state.music_angry
    },
    get_music_sad(state) {
      return state.music_sad
    },
    get_music_fear(state) {
      return state.music_fear
    },
    get_music_disgust(state) {
      return state.music_disgust
    },
    get_music_surprise(state) {
      return state.music_surprise
    },
    get_music_happy(state) {
      return state.music_happy
    },
    get_music_neutral(state) {
      return state.music_neutral
    }
  },

  actions: {
    change_music_angry(name: string) {
      this.music_angry = name
    },
    change_music_sad(name: string) {
      this.music_sad = name
    },
    change_music_fear(name: string) {
      this.music_fear = name
    },
    change_music_disgust(name: string) {
      this.music_disgust = name
    },
    change_music_surprise(name: string) {
      this.music_surprise = name
    },
    change_music_happy(name: string) {
      this.music_happy = name
    },
    change_music_neutral(name: string) {
      this.music_neutral = name
    }
  }
})

export const useUserStore = defineStore('user', {
  state: () => {
    return {
      meeting_key: '',
      is_host: false
    }
  },
  getters: {
    get_meeting_key(state) {
      return state.meeting_key
    },
    get_is_host(state) {
      return state.is_host
    }
  },
  actions: {
    set_meeting(key: string) {
      this.meeting_key = key
    },
    set_host() {
      this.is_host = true
    }
  }
})
