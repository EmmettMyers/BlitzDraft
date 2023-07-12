<template>
    <div class="flex justify-center w-screen">
        <PlayerPickModal 
            v-if="modalOpen" 
            :player="modalPlayer" 
            :team="team" 
            :primaryColor="primaryColor"
            :secondaryColor="secondaryColor"  
            :closeModal="closeModal"
            :startFlipper="startFlipper"
        />
        <div class="teamPickBox mt-2 flex justify-between">
            <div class="mt-2 ml-8">
                <p class="pickTxt text-black">Pick from:</p>
                <div :style="{background: primaryColor}" class="teamHolder">
                    <p :style="{color: secondaryColor}" class="font-bold text-center pt-4">
                        <template v-if="team.split(' ').length === 3">
                            {{ team.split(' ')[0] }} {{ team.split(' ')[1] }}<br>
                            {{ team.split(' ')[2] }}
                        </template>
                        <template v-else>
                            {{ team.split(' ')[0] }}<br>{{ team.split(' ')[1] }}
                        </template>
                    </p>
                    <div class="flex justify-center">
                        <img :src="image" />
                    </div>
                </div>
                <div v-if="teamFlips == 32">
                    <GameTimer
                        :primaryColor="primaryColor"
                        :secondaryColor="secondaryColor"  
                        :timeDone="timeDone"
                        :selectIndex="selectIndex"
                    />
                </div>
            </div>
            <div v-if="teamFlips == 32" class="mt-3 mr-4">
                <div v-for="player in players" :key="player.name">
                    <PickPlayerBox 
                        :player="player"
                        :primaryColor="primaryColor"
                        :secondaryColor="secondaryColor" 
                        :openModal="openModal"
                    />
                </div>
            </div>
        </div>
    </div>
</template>
  
<script lang="ts">
    import PickPlayerBox from './/PickPlayerBox.vue';
    import GameTimer from './/GameTimer.vue';
    import PlayerPickModal from './/PlayerPickModal.vue';
    import { teamColors } from '../styles/team_colors';
    import { fetchTeamPlayerData, teamPlayerData } from '../services/teamFetch';
    import { teamNames } from '../utils/teamNames';
    import { defineComponent } from 'vue';
    import axios from 'axios';
    import { Player } from '@/types/types';
    import { setImage, setColor } from '@/utils/teamSetters';
    import { myPlayers, setPlayer } from '@/utils/myPlayers';

    interface DataProps {
        selectIndex: number;
        teamIndex: number;
        flipId: number;
        teamFlips: number;
        team: string;
        finalTeam: string;
        primaryColor: string;
        secondaryColor: string;
        image: string;
        players: Player[],
        modalOpen: boolean,
        modalPlayer: Player
    }

    export default defineComponent({
        components: {
            PickPlayerBox,
            PlayerPickModal,
            GameTimer
        },
        data(): DataProps {
            return {
                selectIndex: 0,
                teamIndex: Math.floor(Math.random() * 32),
                flipId: 0,
                teamFlips: 0,
                team: "",
                finalTeam: "",
                primaryColor: "",
                secondaryColor: "",
                image: "",
                players: [{pos: "", name: "", stats: [], image: ""}],
                modalOpen: false,
                modalPlayer: {pos: "", name: "", stats: [], image: ""}
            };
        },
        methods: {
            timeDone(index: number): void {
                if (this.selectIndex == index){
                    let filled = false;
                    while (!filled){
                        const randPlayer: Player = this.players[Math.floor(Math.random() * 8)];
                        const player = myPlayers.value.find((player) => player.pos === randPlayer.pos);
                        if (!(!!player && player.name !== '')){
                            setPlayer(randPlayer.pos, randPlayer.name, this.team, randPlayer.stats);
                            filled = true;
                        }
                    }
                    this.startFlipper();
                }
            },
            openModal(player: any): void {
                this.modalPlayer = player;
                this.modalOpen = true;
            },
            closeModal(): void {
                this.modalOpen = false;
            },
            flipper(): void {
                this.team = Object.keys(teamNames)[this.teamIndex];
                this.image = setImage(this.team);
                this.primaryColor = setColor("primary", this.team);
                this.secondaryColor = setColor("secondary", this.team);
                if (this.teamIndex == 31){
                    this.teamIndex = 0;
                } else {
                    this.teamIndex += 1;
                }
                this.teamFlips += 1;
                if (this.teamFlips == 32){
                    this.team = this.finalTeam;
                    this.image = setImage(this.team);
                    this.primaryColor = setColor("primary", this.team);
                    this.secondaryColor = setColor("secondary", this.team);
                    clearInterval(this.flipId);
                }
            },
            async startFlipper() {
                this.selectIndex += 1;
                this.teamFlips = 0;
                this.finalTeam = Object.keys(teamNames)[Math.floor(Math.random() * 32)];
                await fetchTeamPlayerData(this.finalTeam);
                this.players = teamPlayerData;
                this.flipId = setInterval(this.flipper, 100);
            }
        },
        mounted() {
            this.startFlipper();
        },
    });
</script>

<style lang="scss" scoped>
    @import "../styles/colors.scss";
    .teamPickBox {
        width: 600px;
        height: 300px;
        background: $lightGray;
        border-radius: 13px;
        .pickTxt {
            font-size: 30px;
        }
        .teamHolder {
            background: white;
            width: 210px;
            height: 200px;
            border-radius: 13px;
            box-shadow: 0 2px 2px rgba(0, 0, 0, 0.25);
            p {
                font-size: 25px;
                line-height: 25px;
            }
            img {
                height: 120px;
            }
        }
    }
</style>
  