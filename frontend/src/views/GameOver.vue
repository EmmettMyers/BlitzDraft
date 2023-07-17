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
            <div 
                v-on:click="restart"
                 class="btn start w-full flex justify-center items-center font-semibold mt-8">
                    Start New Game
            </div>
            <div v-if="saveStep == 1" class="pt-2 pb-3">
                <p class="saveTxt font-light mt-1">Enter your team's name:</p>
                <div class="flex justify-center">
                    <input 
                        v-model="teamName"
                        class="input font-normal text-black flex justify-center items-center pl-4">
                    <div 
                        v-on:click="submitSaveTeam"
                        class="submit font-semibold flex justify-center items-center">
                            Save
                    </div>
                </div>
            </div>
            <p v-if="saveStep == 2" class="savedTxt font-light mt-1">Your team has been saved.</p>
            <div 
                v-if="saveStep == 0"
                v-on:click="startSaveTeam"
                class="btn save w-full flex justify-center items-center font-semibold mt-2">
                    Save Team
            </div>
            <div 
                v-on:click="setPage('home')"
                 class="btn exit w-full flex justify-center items-center font-semibold mt-2">
                    Exit to Menu
            </div>
        </div>
    </div>
</template>

<script lang="ts">
    import { projectedRecord, totalScore } from '@/services/modelFetch';
    import { myRank, roomTeamRankings, scoresReady } from '@/services/roomHandler';
    import { saveTeam } from '@/services/savedTeams';
    import { postRank, postRecord } from '@/services/statistics';
    import { emptyMyPlayers, myPlayers, playersFilled } from '@/utils/myPlayers';
    import { resetMetrics } from '@/utils/reset';
    import { defineComponent } from 'vue';

    export default defineComponent({
        props: ['setPage'],
        data() {
            return {
                waitForImage: "display: none",
                players: myPlayers,
                title: "",
                number: "",
                saveStep: 0,
                teamName: "",
            }
        },
        methods: {
            imageLoaded(): void {
                this.waitForImage = "display: block"
            },
            restart(): void {
                resetMetrics();
                this.setPage('game');
            },
            submitSaveTeam(): void {
                saveTeam(this.teamName);
                this.saveStep = 2;
            },
            startSaveTeam(): void {
                if (this.saveStep != 2){
                    this.saveStep = 1;
                }
            },
        },
        mounted(){
            this.saveStep = 0;
            if (projectedRecord.value != ""){
                this.title = "Record";
                this.number = projectedRecord.value;
                const wins = parseInt(this.number.substring(0, this.number.indexOf("-")));
                postRecord(wins);
            } else {
                this.title = "Ranking";
                this.number = "#" + myRank.value.toString();
                postRank(myRank.value);
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
        .input {
            border-radius: 13px 0 0 13px;
            background: #A7A7A7;
            width: 420px;
            height: 40px;
            font-size: 20px;
        }
        .submit {
            border-radius: 0 13px 13px 0;
            background: #B05A0B;
            width: 120px;
            height: 40px;
            font-size: 20px;
            padding-bottom: 3px;
            &:hover {
                cursor: pointer;
                transition: .2s;
                filter: brightness(120%);
            }
        }
        .saveTxt {
            font-size: 20px;
        }
        .savedTxt {
            font-size: 20px;
            color: #e3730b;
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