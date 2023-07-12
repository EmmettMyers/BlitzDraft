<template>
  <div class="flex justify-center w-screen">
    <div class="navbar flex justify-between z-10">
      <img class="bd-logo mt-1 ml-1" src="../assets/longLogo1.png" />
      <div v-on:click="leave" class="btn flex justify-center items-center font-semibold mt-3 mr-4">Leave Game</div>
    </div>
  </div>
</template>

<script lang="ts">
import { leaveRoom, room } from '@/services/roomHandler';
import { defineComponent } from 'vue';

export default defineComponent({
  props: ['setPage'],
  methods: {
    leave(): void {
      if (room.value != ''){
        leaveRoom();
      }
      this.setPage('home');
    }
  }
});
</script>

<style lang="scss" scoped>
  @import "../styles/colors.scss";
  .navbar {
    width: 600px;
    height: 50px;
    background: $darkGray;
    border-radius: 0 0 13px 13px;
    .bd-logo {
      height: 40px;
    }
    .btn {
      border-radius: 13px;
      background: $softRed;
      height: 30px;
      width: 140px;
      font-size: 15px;
      &:hover {
        transition: 0.2s;
        filter: brightness(90%);
        cursor: pointer;
      }
    }
  }
</style>
