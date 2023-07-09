<template>
  <GameEngine />
</template>

<script lang="ts">
  import GameEngine from './views/GameEngine.vue';

  export default {
    components: {
      GameEngine,
    }
  };
</script>

<style lang="scss">
  body {
    background: black;
    color: white;
    user-select: none;
  }
</style>
