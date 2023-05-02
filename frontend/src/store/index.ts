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
