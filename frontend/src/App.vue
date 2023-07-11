<template>
  <HomePage v-if="page == 'home'" :setPage="setPage" />
  <GameEngine v-if="page == 'game'" :setPage="setPage" />
  <GameOver v-if="page == 'gameOver'" :setPage="setPage" />
</template>

<script lang="ts">
  import HomePage from './views/HomePage.vue';
  import GameEngine from './views/GameEngine.vue';
  import GameOver from './views/GameOver.vue';
  import { defineComponent } from 'vue';

  export default defineComponent({
    components: {
      HomePage, GameEngine, GameOver
    },
    data() {
      return {
        page: "home"
      }
    },
    methods: {
      setPage(page: string): void {
        this.page = page;
      }
    }
  });
</script>

<style lang="scss">
  body {
    background: black;
    color: white;
    user-select: none;
  }
</style>
