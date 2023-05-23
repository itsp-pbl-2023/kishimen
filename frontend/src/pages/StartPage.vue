<template>
  <routes />
  <div class="container">
    <div class="left-side">
      <div class="discription"></div>
      <div class="start-botan"></div>
    </div>
    <div class="right-side">
      <div class="image"></div>
    </div>
  </div>
</template>

<script lang="ts">
import Routes from '/@/components/Routes.vue'
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'StartPage',
  components: {
    Routes
  }
})
</script>

<style>
.container {
  display: flex;
  width: 100vw;
  height: 100vh;
  background-color: red;
}
.left-side {
  width: 50%;
  height: 100%;
  /* background-color: black; */
}
.right-side {
  width: 50%;
  height: 50%;
  /* background-color: green; */
}

.discription {
  width: 40%;
  height: 50%;
  background-color: blue;
}
.image {
  width: 60%;
  height: 60%;
  background-color: black;
}
.start-botan {
  width: 40%;
  height: 50%;
  background-color: pink;
}
</style>
