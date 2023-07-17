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
            <div class="flex justify-between mt-3">
                <div>
                    <p class="recordTxt font-normal">Avg. Record</p>
                    <div class="recordBox flex justify-center items-center font-bold">11-6</div>
                </div>
                <div>
                    <p class="recordTxt font-normal">Highest Record</p>
                    <div class="recordBox flex justify-center items-center font-bold">11-6</div>
                </div>
                <div>
                    <p class="recordTxt font-normal">Lowest Record</p>
                    <div class="recordBox flex justify-center items-center font-bold">11-6</div>
                </div>
                <div>
                    <p class="recordTxt font-normal">Avg. Rank</p>
                    <div class="recordBox flex justify-center items-center font-bold">2</div>
                </div>
            </div>
            <p class="recordTxt font-normal mt-1">Record Distribution</p>
            <div class="recordDist"></div>
            <div class="flex justify-between mt-1">
                <div>
                    <p class="draftTxt font-normal">Most Drafted Players</p>
                    <div class="draftBox flex justify-center items-center font-bold">Justin Jefferson</div>
                    <div class="draftBox mt-1 flex justify-center items-center font-bold">Josh Jacobs</div>
                    <div class="draftBox mt-1 flex justify-center items-center font-bold">Texans OL</div>
                    <div class="draftBox mt-1 flex justify-center items-center font-bold">Cole Kmet</div>
                    <div class="draftBox mt-1 flex justify-center items-center font-bold">Patrick Mahomes</div>
                </div>
                <div>
                    <p class="teamTxt font-normal">Most Rolled Teams</p>
                    <div class="teamBox flex justify-center items-center font-bold">Houston Texans</div>
                    <div class="teamBox mt-1 flex justify-center items-center font-bold">Minnesota Vikings</div>
                    <p class="teamTxt font-normal mt-1">Least Rolled Teams</p>
                    <div class="teamBox flex justify-center items-center font-bold">Miami Dolphins</div>
                    <div class="teamBox mt-1 flex justify-center items-center font-bold">New England Patriots</div>
                </div>
            </div>
            <p class="recordTxt font-normal mt-1">ADP by Player Position</p>
            <div class="recordDist"></div>
        </div>
    </div>
</template>

<script lang="ts">
    import { defineComponent } from 'vue';

    export default defineComponent({
        props: ['setPage'],
        data() {
            return {
                waitForImage: "display: none",
            }
        },
        methods: {
            imageLoaded(): void {
                this.waitForImage = "display: block";
            },
        }
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
        .teamBox {
            width: 295px;
            height: 38px;
            background: #174FBF;
            border-radius: 13px;
            font-size: 18px;
        }
        .draftTxt {
            font-size: 16px;
        }
        .draftBox {
            width: 295px;
            height: 35px;
            background: #174FBF;
            border-radius: 13px;
            font-size: 18px;
        }
        .recordDist {
            width: 600px;
            height: 120px;
            background: white;
            border-radius: 13px;
        }
        .recordTxt {
            font-size: 16px;
        }
        .recordBox {
            width: 140px;
            height: 50px;
            background: #174FBF;
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
    }
</style>