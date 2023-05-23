<template>
  <div :class="$style.app">
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
</style>
