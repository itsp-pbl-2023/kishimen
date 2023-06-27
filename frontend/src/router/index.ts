import { createRouter, createWebHistory } from 'vue-router'
import Index from '../pages/IndexPage.vue'
import Hello from '../pages/HelloPage.vue'
import StartPage from '../pages/StartPage.vue'
import MainPage from '../pages/MainPage.vue'
import SettingPage from '../pages/SettingPage.vue'

export const routerHistory = createWebHistory()

export default createRouter({
  history: routerHistory,
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/hello',
      name: 'hello',
      component: Hello
    },
    {
      path: '/start-page',
      name: 'start-page',
      component: StartPage,
    },
    {
      path: '/main',
      name: 'main',
      component: MainPage
    },
    {
      path: '/setting',
      name: 'setting',
      component: SettingPage
    }
  ]
})
