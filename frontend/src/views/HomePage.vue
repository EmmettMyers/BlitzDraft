<template>
    <div class="w-screen h-screen flex justify-center items-center">
        <div :style="waitForImage" class="home mb-5">
            <MultiplayerModal v-if="modalOpen" :closeModal="closeModal" :setPage="setPage" />
            <img @load="imageLoaded" src="../assets/bdLong4.png" />
            <p class="play text-regular mt-8">Play</p>
            <div class="flex justify-center">
                <div 
                    v-on:click="setPage('game')" 
                    class="spBtn font-semibold flex justify-center items-center">
                        Singleplayer
                </div>
                <div 
                    v-on:click="openModal" 
                    class="mpBtn font-semibold flex justify-center items-center">
                        Multiplayer
                </div>
            </div>
            <p class="data text-regular mt-2">Data</p>
            <div class="flex justify-center">
                <div 
                    v-on:click="setPage('teams')" 
                    class="teamsBtn font-semibold flex justify-center items-center">
                        Saved Teams
                </div>
                <div 
                    v-on:click="setPage('stats')" 
                    class="statsBtn font-semibold flex justify-center items-center">
                        Statistics
                </div>
            </div>
            <p v-on:click="logout" class="logout float-right font-medium">Log Out</p>
        </div>
    </div>
</template>

<script lang="ts">
    import { defineComponent } from 'vue';
    import MultiplayerModal from '../components/MultiplayerModal.vue';
    import { logOut } from '@/services/firebase';
    import { emptyMyPlayers, playersFilled } from '@/utils/myPlayers';
    import { projectedRecord, totalScore } from '@/services/modelFetch';
    import { myRank, roomTeamRankings, scoresReady } from '@/services/roomHandler';
    import { pickNumber } from '@/services/statistics';
    import { resetMetrics } from '@/utils/reset';

    export default defineComponent({
        props: ['setPage'],
        components: { MultiplayerModal },
        data() {
            return {
                waitForImage: "display: none",
                modalOpen: false
            }
        },
        methods: {
            imageLoaded(): void {
                this.waitForImage = "display: block"
            },
            openModal(): void {
                this.modalOpen = true;
            },
            closeModal(): void {
                this.modalOpen = false;
            },
            logout(): void {
                logOut();
                this.setPage('login');
            }
        },
        mounted() {
            resetMetrics();
        }
    });
</script>

<style lang="scss" scoped>
    .home {
        width: 600px;
        .play  {
            font-size: 30px;
        }
        .logout {
            color: #807e7e;
            font-size: 20px;
            &:hover {
                cursor: pointer;
                transition: .2s;
                filter: brightness(120%);
            }
        }
        .teamsBtn, .statsBtn, .spBtn, .mpBtn {
            &:hover {
                cursor: pointer;
                transition: .2s;
                filter: brightness(120%);
            }
        }
        .spBtn, .mpBtn {
            width: 300px;
            height: 150px;
            font-size: 40px;
            padding-bottom: 10px;
        }
        .spBtn {
            border-radius: 13px 0 0 13px;
            background: #B50000;
        }
        .mpBtn {
            border-radius: 0 13px 13px 0;
            background: #00349F;
        }
        .data  {
            font-size: 22px;
        }
        .teamsBtn, .statsBtn {
            width: 300px;
            height: 80px;
            font-size: 30px;
            padding-bottom: 5px;
        }
        .teamsBtn {
            border-radius: 13px 0 0 13px;
            background: #B05A0B;
        }
        .statsBtn {
            border-radius: 0 13px 13px 0;
            background: #7C3E05;
        }
    }
</style>