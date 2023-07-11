<template>
    <div class="w-screen h-screen">
        <NavBar />
        <GameCountdown v-if="!fullTeam && !countDone" :countdownComplete="countdownComplete" />
        <TeamPickBox v-if="!fullTeam && countDone" />
        <MyRosterBox v-if="!fullTeam && countDone" showTxt="true" width="600px" />
        <EndGame v-if="fullTeam" />
        <div class="imgContainer absolute top-0 left-0">
            <img class="absolute" src="../assets/lucasOil.jpg" />
        </div>
    </div>
</template>

<script lang="ts">
    import { defineComponent } from 'vue';
    import NavBar from '../components/NavBar.vue';
    import TeamPickBox from '../components/TeamPickBox.vue';
    import MyRosterBox from '../components/MyRosterBox.vue';
    import GameCountdown from '../components/GameCountdown.vue';
    import EndGame from '../components/EndGame.vue';
    import { playersFilled } from '@/utils/myPlayers';

    export default defineComponent({
        components: {
            NavBar,
            TeamPickBox,
            MyRosterBox,
            EndGame,
            GameCountdown
        },
        data() {
            return {
                fullTeam: playersFilled,
                countDone: false
            }
        },
        methods: {
            countdownComplete(){
                this.countDone = true;
            }
        }
    });
</script>

<style lang="scss" scoped>
    .imgContainer {
        overflow: hidden;
        width: 600px;
        height: 100%;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: -10;
        img {
            object-fit: cover;
            height: 100vh;
            opacity: .15;
        }
    }
</style>
  