<template>
  <LoginPage v-if="!loggedIn && page == 'login'" :setPage="setPage" />
  <HomePage v-if="(loggedIn && page == 'login') || page == 'home'" :setPage="setPage" />
  <SavedTeams v-if="page == 'teams'" :setPage="setPage" />
  <StatsPage v-if="page == 'stats'" :setPage="setPage" />
  <GameRoom v-if="page == 'room'" :setPage="setPage" />
  <GameEngine v-if="page == 'game'" :setPage="setPage" />
  <GameOver v-if="page == 'gameOver'" :setPage="setPage" />
</template>

<script lang="ts">
  import LoginPage from './views/LoginPage.vue';
  import HomePage from './views/HomePage.vue';
  import SavedTeams from './views/SavedTeams.vue';
  import StatsPage from './views/StatsPage.vue';
  import GameRoom from './views/GameRoom.vue';
  import GameEngine from './views/GameEngine.vue';
  import GameOver from './views/GameOver.vue';
  import { defineComponent } from 'vue';
  import { loggedIn } from './services/firebase';

  export default defineComponent({
    components: {
      LoginPage, 
      HomePage, 
      SavedTeams, 
      StatsPage,
      GameRoom, 
      GameEngine, 
      GameOver
    },
    data() {
      return {
        page: "login",
        loggedIn: loggedIn
      }
    },
    methods: {
      setPage(page: string): void {
        this.page = page;
      }
    },
    mounted() {
      if (localStorage.getItem("username") != null && localStorage.getItem("username") != ""){
        this.setPage('home');
      }
    }
  });
</script>

<style lang="scss">
  body {
    background: black;
    color: white;
    user-select: none;
    input:focus,
    select:focus,
    textarea:focus,
    button:focus {
        outline: none;
    }
  }
</style>
