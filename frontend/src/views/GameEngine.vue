<template>
    <div :style="waitForImage" class="w-screen h-screen">
        <NavBar :setPage="setPage" />
        <GameCountdown v-if="!fullTeam && !countDone" :countdownComplete="countdownComplete" />
        <TeamPickBox v-if="!fullTeam && countDone" />
        <MyRosterBox v-if="!fullTeam && countDone" showTxt="true" width="600px" />
        <WaitingMP v-if="fullTeam && room != '' && scoresReady == false" />
        <EndGame 
            v-if="room == '' && fullTeam" 
            :gameDone="gameDone" 
        />
        <EndGameMP 
            v-if="room != '' && fullTeam && scoresReady == true" 
            :gameDone="gameDone" 
        />
        <div class="imgContainer absolute top-0 left-0">
            <img @load="imageLoaded" class="absolute" src="../assets/lucasOil.jpg" />
        </div>
    </div>
</template>

<script lang="ts">
    import { defineComponent } from 'vue';
    import NavBar from '../components/NavBar.vue';
    import TeamPickBox from '../components/TeamPickBox.vue';
    import MyRosterBox from '../components/MyRosterBox.vue';
    import WaitingMP from '../components/WaitingMP.vue';
    import GameCountdown from '../components/GameCountdown.vue';
    import EndGame from '../components/EndGame.vue';
    import EndGameMP from '../components/EndGameMP.vue';
    import { emptyMyPlayers, playersFilled } from '@/utils/myPlayers';
    import { myRank, room, roomTeamRankings, scoresReady } from '@/services/roomHandler';
    import { projectedRecord, totalScore } from '@/services/modelFetch';
    import { pickNumber } from '@/services/statistics';
    import { resetMetrics } from '@/utils/reset';

    export default defineComponent({
        props: ['setPage'],
        components: {
            NavBar,
            TeamPickBox,
            MyRosterBox,
            WaitingMP,
            EndGame,
            EndGameMP,
            GameCountdown
        },
        data() {
            return {
                fullTeam: playersFilled,
                countDone: false,
                waitForImage: "display: none",
                room: room,
                scoresReady: scoresReady
            }
        },
        methods: {
            countdownComplete(){
                this.countDone = true;
            },
            imageLoaded(): void {
                this.waitForImage = "display: block"
            },
            gameDone(): void {
                this.setPage('gameOver');
            },
        },
        mounted() {
            resetMetrics();
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
  