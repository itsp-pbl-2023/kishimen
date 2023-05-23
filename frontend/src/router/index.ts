import { createRouter, createWebHistory } from 'vue-router'
import Index from '../pages/IndexPage.vue'
import Hello from '../pages/HelloPage.vue'
import MainPage from '../pages/MainPage.vue'

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
      path: '/main',
      name: 'main',
      component: MainPage
    }
  ]
})
