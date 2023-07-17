<template>
    <div 
        :style="waitForImage" v-on:click="closeModal"
        class="shadow bg-black w-screen h-screen z-20 absolute left-0 top-0 opacity-90">
    </div>
    <div :style="waitForImage" class="playerPickModal absolute z-30 mt-20">
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
                <img @load="imageLoaded" v-if="secondaryImage == ''" class="absolute bottom-0" :src="player.image"/>
                <img @load="imageLoaded" v-else class="absolute bottom-1" :src="secondaryImage"/>
            </div>
            <div class="statHolder mr-8">
                <div v-for="(stat, index) in player.stats" :key="stat">
                    <PlayerPickModalStats 
                        :pos="player.pos"
                        :index="index"
                        :stat="stat"
                        :statName="statNames[index]"
                        :primaryColor="primaryColor"
                        :secondaryColor="secondaryColor" 
                    />
                </div>
            </div>
        </div>
        <div class="flex justify-center">
            <div 
                v-on:click="selectPlayer()" 
                class="btn flex justify-center items-center font-bold mt-5">
                    Select Player
            </div>
        </div>
    </div>
</template>
  
<script lang="ts">
    import { defineComponent } from 'vue';
    import PlayerPickModalStats from './/PlayerPickModalStats.vue';
    import { statNames } from '../utils/playerStatNames';
    import { myPlayers, setPlayer } from '@/utils/myPlayers';
    import { setImage } from '@/utils/teamSetters';
    import { postDraftPick } from '@/services/statistics';

    interface DataProps {
        statNames: string[];
        secondaryImage: string;
        waitForImage: string;
    }

    export default defineComponent({
        components: {
            PlayerPickModalStats,
        },
        props: ['player', 'team', 'primaryColor', 'secondaryColor', 'closeModal', 'startFlipper'],
        data(): DataProps {
            return {
                statNames: [""],
                secondaryImage: "",
                waitForImage: "display: none"
            };
        },
        methods: {
            selectPlayer(): void {
                this.startFlipper();
                setPlayer(this.player.pos, this.player.name, this.team, this.player.stats);
                this.closeModal();
                postDraftPick(this.player, this.team);
            },
            imageLoaded(): void {
                this.waitForImage = "display: block"
            }
        },
        mounted() {
            const pos: string = this.player.pos;
            this.statNames = statNames[pos].stats;
            if (pos == "OL" || pos == "DEF"){
                this.secondaryImage = setImage(this.team);
            }
        },
    });
</script>

<style lang="scss" scoped>
    @import "../styles/colors.scss";
    .playerPickModal {
        width: 550px;
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
            width: 450px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .desc {
            font-size: 22px;
        }
        .imgHolder {
            width: 190px;
            height: 205px;
            border-radius: 13px;
            box-shadow: 0 2px 2px rgba(0, 0, 0, 0.25);
            img {
                border-radius: 13px;
                height: 190px;
            }
        }
        .btn {
            width: 490px;
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
  @/utils/styleSetters