<template>
  <div :class="$style.app">
    <div :class="$style.upperbar">
      <h1 :class="$style.kishimen">KISHIMEN</h1>
    </div>
    <router-view />
  </div>
</template>

<style lang="scss" module>
.app {
  position: fixed;
  top: 0;
  right: 0;
  width: 100%;
  height: 100%;
  padding-bottom: env(safe-area-inset-bottom);
}
.upperbar {
  width: 100%;
  height: 100px;
  background-color: orange;
  display: flex;
  justify-content: center;
  align-items: center;
}

.kishimen {
  font-size: 4em;
  color: rgb(255, 255, 255);
}
</style>
