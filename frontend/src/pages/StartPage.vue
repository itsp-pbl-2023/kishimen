<template>
  <div class="container">
    <div class="flex-container">
      <div class="left-side">
        <div class="discription"></div>
        <button class="start-button">Lets start!</button>
      </div>
      <div class="right-side">
        <div class="image"></div>
      </div>
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
  width: 100vw;
  height: 100vh;
  /* background-color: red; */
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
  color: pink;
  /* background-color: black; */
}
.right-side {
  padding: 5% 0 5% 0;
  width: 45%;
  height: 90%;
  /* background-color: green; */
}

.discription {
  width: 100%;
  height: 50%;
  background-color: blue;
}
.image {
  width: 100%;
  height: 100%;
  background-color: black;
}
.start-button {
  margin-top: 15%;
  width: 100%;
  height: 20%;
  font-size: 50px;
  border-radius: 30px;
  border-color: #ff971d;
  /* background-color: pink; */
}
</style>
