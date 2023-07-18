<template>
    <div class="w-screen h-screen flex justify-center items-center">
        <div :style="waitForImage" class="stats mb-3">
            <div class="flex justify-between items-center">
                <img @load="imageLoaded" src="../assets/bdStats.png" />
                <div 
                    v-on:click="setPage('home')"
                    class="exit flex justify-center items-center font-medium">
                        Exit
                </div>
            </div>
            <div class="flex justify-center items-center">
                <div v-if="!waitForStats" class="lds-ring mt-2">
                    <div></div><div></div><div></div><div></div></div>
            </div>
            <div v-if="waitForStats">
                <div class="flex justify-between mt-3">
                    <div>
                        <p class="recordTxt font-normal">Avg. Record</p>
                        <div 
                            style="background: #174FBF"
                            class="recordBox flex justify-center items-center font-bold">
                                {{avgRecord}}
                        </div>
                        <p class="recordTxt font-normal">Highest Record</p>
                        <div 
                            style="background: #077712"
                            class="recordBox flex justify-center items-center font-bold">
                                {{highRecord}}
                        </div>
                        <p class="recordTxt font-normal">Lowest Record</p>
                        <div 
                            style="background: #A82323"
                            class="recordBox flex justify-center items-center font-bold">
                                {{lowRecord}}
                        </div>
                    </div>
                    <div>
                        <p class="recordTxt font-normal">Record Distribution</p>
                        <RecordChart :records="allRecords" />
                    </div>
                </div>
                <div class="flex justify-between mt-2">
                    <div>
                        <p class="draftTxt font-normal">Most Drafted Players</p>
                        <div v-for="player in highPlayers" :key="player">
                            <StatPlayerBox :name="player[0]" :team="player[1][0]" height="35px" />
                        </div>
                    </div>
                    <div>
                        <p class="recordTxt font-normal mt-1">ADP by Player Position</p>
                        <ADPChart :values="positionADP" />
                    </div>
                </div>
                <div class="flex justify-between mt-2">
                    <div>
                        <p class="teamTxt font-normal">Most Rolled Teams</p>
                        <StatPlayerBox :name="highTeams[0]" :team="highTeams[0]" height="38px" />
                        <StatPlayerBox :name="highTeams[1]" :team="highTeams[1]" height="38px" />
                    </div>
                    <div>
                        <p class="teamTxt font-normal mt-1">Least Rolled Teams</p>
                        <StatPlayerBox :name="lowTeams[0]" :team="lowTeams[0]" height="38px" />
                        <StatPlayerBox :name="lowTeams[1]" :team="lowTeams[1]" height="38px" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
    import {
        allRanks,
        allRecords,
        avgRank,
        avgRecord,
        getStats,
        highRecord,
        leastRolledTeams,
        lowRecord,
        mostDraftedPlayers,
        mostRolledTeams,
        positionADP,
    } from '@/services/statistics';
    import StatPlayerBox from '../components/StatPlayerBox.vue';
    import RecordChart from '../components/RecordChart.vue';
    import ADPChart from '../components/ADPChart.vue';
    import { defineComponent } from 'vue';

    export default defineComponent({
        props: ["setPage"],
        components: { StatPlayerBox, RecordChart, ADPChart },
        data() {
            return {
                waitForImage: "display: none",
                waitForStats: false,
                avgRecord: avgRecord,
                highRecord: highRecord,
                lowRecord: lowRecord,
                avgRank: avgRank,
                highPlayers: mostDraftedPlayers,
                highTeams: mostRolledTeams,
                lowTeams: leastRolledTeams,
                positionADP: positionADP,
                allRecords: allRecords,
                allRanks: allRanks
            };
        },
        methods: {
            imageLoaded(): void {
                this.waitForImage = "display: block";
            },
            formatRecords(): void {
                if (this.avgRecord != "N/A"){
                    this.avgRecord = this.avgRecord + "-" + (17 - Number(this.avgRecord));
                    this.highRecord = this.highRecord + "-" + (17 - Number(this.highRecord));
                    this.lowRecord = this.lowRecord + "-" + (17 - Number(this.lowRecord));
                }
            }
        },
        async mounted() {
            await getStats();
            this.formatRecords();
            this.waitForStats = true;
        },
    });
</script>

<style lang="scss" scoped>
    .stats {
        width: 600px;
        img {
            width: 250px;
        }
        .teamTxt {
            font-size: 16px;
        }
        .adpBox {
            width: 600px;
            height: 120px;
            background: white;
            border-radius: 13px;
        }
        .recordTxt {
            font-size: 16px;
        }
        .recordBox {
            width: 180px;
            height: 50px;
            border-radius: 13px;
            font-size: 30px;
            padding-bottom: 3px;
        }
        .exit {
            width: 100px;
            height: 40px;
            background: #A82323;
            border-radius: 13px;
            font-size: 20px;
            padding-bottom: 2px;
            &:hover {
                cursor: pointer;
                transition: .2s;
                filter: brightness(120%);
            }
        }
        .lds-ring {
            width: 80px;
            height: 600px;
            padding-top: 200px;
        }
        .lds-ring div {
            box-sizing: border-box;
            display: block;
            position: absolute;
            width: 100px;
            height: 100px;
            margin: 8px;
            border: 10px solid #fff;
            border-radius: 50%;
            animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
            border-color: white transparent transparent transparent;
        }
        .lds-ring div:nth-child(1) {
            animation-delay: -0.45s;
        }
        .lds-ring div:nth-child(2) {
            animation-delay: -0.3s;
        }
        .lds-ring div:nth-child(3) {
            animation-delay: -0.15s;
        }
        @keyframes lds-ring {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    }
</style>