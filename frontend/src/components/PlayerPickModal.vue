<template>
    <div 
        v-on:click="closeModal" 
        class="shadow bg-black w-screen h-screen z-20 absolute left-0 top-0 opacity-90">
    </div>
    <div class="playerPickModal absolute z-30 mt-20">
        <p 
            v-on:click="closeModal" 
            class="exit text-black font-normal absolute right-5 top-0">
                x
        </p>
        <div class="ml-8">
            <p class="title text-black font-extrabold mt-4">{{ player.name }}</p>
            <p class="desc text-black font-medium">{{ player.pos }} | {{ team }}</p>
        </div>
        <div class="flex justify-between mt-4">
            <div class="imgHolder bg-white ml-8 flex justify-center relative">
                <img class="absolute bottom-0" :src="player.image"/>
            </div>
            <div class="statHolder mr-8">
                <div v-for="(stat, index) in player.stats" :key="stat">
                    <PlayerPickModalStats 
                        :stat="stat"
                        :statName="statNames[index]"
                        :primaryColor="primaryColor"
                        :secondaryColor="secondaryColor" 
                    />
                </div>
            </div>
        </div>
        <div class="flex justify-center">
            <div class="btn flex justify-center items-center font-bold mt-5">Select Player</div>
        </div>
    </div>
</template>
  
<script lang="ts">
    import { defineComponent } from 'vue';
    import PlayerPickModalStats from './/PlayerPickModalStats.vue';
    import { statNames } from '../utils/playerStatNames';

    export default defineComponent({
        components: {
            PlayerPickModalStats,
        },
        props: ['player', 'team', 'primaryColor', 'secondaryColor', 'closeModal'],
        data() {
            return {
                statNames: [""],
            };
        },
        mounted() {
            const pos: string = this.player.pos;
            this.statNames = statNames[pos].stats;
        },
    });
</script>

<style lang="scss" scoped>
    @import "../styles/colors.scss";
    .playerPickModal {
        width: 600px;
        height: 425px;
        background: $solidGray;
        border-radius: 13px;
        .exit {
            line-height: 50px;
            font-size: 50px;
            &:hover {
                cursor: pointer;
                color: #5c5c5c;
                transition: .2s;
            }
        }
        .title {
            line-height: 50px;
            font-size: 40px;
        }
        .desc {
            font-size: 22px;
        }
        .imgHolder {
            width: 250px;
            height: 205px;
            border-radius: 13px;
            box-shadow: 0 2px 2px rgba(0, 0, 0, 0.25);
            img {
                height: 190px;
            }
        }
        .btn {
            width: 535px;
            height: 50px;
            background: $solidGreen;
            border-radius: 13px;
            box-shadow: 0 2px 2px rgba(0, 0, 0, 0.25);
            font-size: 22px;
            &:hover {
                cursor: pointer;
                filter: brightness(120%);
                transition: .2s;
            }
        }
    }
</style>
  