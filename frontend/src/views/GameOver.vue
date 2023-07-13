<template>
    <div class="w-screen h-screen flex justify-center items-center">
        <div :style="waitForImage" class="gameOver mb-8">
            <img @load="imageLoaded" src="../assets/bdLong3.png" />
            <div class="teamHolder mt-6 relative">
                <p class="user pl-7 pt-2 pb-1 font-extrabold">Emmett Myers</p>
                <p class="player font-medium pl-7" v-for="player in players" :key="player.name">
                    <span class="pos">{{ player.pos }}:</span> {{ player.name }}
                </p>
                <div class="recordHolder absolute bottom-16 right-8">
                    <p class="txt text-black text-center font-medium mt-4">{{ title }}:</p>
                    <p class="num text-black text-center font-black">{{ number }}</p>
                </div>
            </div>
            <div v-on:click="restart"
                 class="btn start w-full flex justify-center items-center font-semibold mt-8">
                Start New Game
            </div>
            <div class="btn save w-full flex justify-center items-center font-semibold mt-2">
                Save Team
            </div>
            <div v-on:click="setPage('home')"
                 class="btn exit w-full flex justify-center items-center font-semibold mt-2">
                    Exit to Menu
            </div>
        </div>
    </div>
</template>

<script lang="ts">
    import { projectedRecord, totalScore } from '@/services/modelFetch';
    import { myRank, roomTeamRankings, scoresReady } from '@/services/roomHandler';
    import { emptyMyPlayers, myPlayers, playersFilled } from '@/utils/myPlayers';
    import { defineComponent } from 'vue';

    export default defineComponent({
        props: ['setPage'],
        data() {
            return {
                waitForImage: "display: none",
                players: myPlayers,
                title: "",
                number: ""
            }
        },
        methods: {
            imageLoaded(): void {
                this.waitForImage = "display: block"
            },
            restart(): void {
                this.setPage('game');
            }
        },
        mounted(){
            if (projectedRecord.value != ""){
                this.title = "Record";
                this.number = projectedRecord.value;
            } else {
                this.title = "Ranking";
                this.number = "#" + myRank.value.toString();
            }
        }
    });
</script>

<style lang="scss" scoped>
    .gameOver {
        width: 500px;
        img {
            width: 200px;
        }
        .btn {
            height: 70px;
            border-radius: 13px;
            font-size: 30px;
            padding-bottom: 5px;
            &:hover {
                cursor: pointer;
                transition: .2s;
                filter: brightness(120%);
            }
        }
        .start { background: #077712; }
        .save { background: #B05A0B; }
        .exit { background: #A82323; }
        .teamHolder {
            width: 500px;
            height: 300px;
            background: #636363;
            border-radius: 13px;
            .user {
                font-size: 40px;
            }
            .player {
                font-size: 20px;
                line-height: 25px;
                .pos {
                    font-weight: 400 !important;
                    color: #bababa;
                }
            }
            .recordHolder {
                width: 160px;
                height: 130px;
                background: #FFE500;
                border-radius: 13px;
                box-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
                .txt {
                    font-size: 25px;
                }
                .num {
                    line-height: 50px;
                    font-size: 50px;
                }
            }
        }
    }
</style>@/services/modelFetch