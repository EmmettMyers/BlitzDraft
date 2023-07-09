<template>
    <div class="flex justify-center w-screen">
        <PlayerPickModal 
            v-if="modalOpen" 
            :player="modalPlayer" 
            :team="team" 
            :primaryColor="primaryColor"
            :secondaryColor="secondaryColor"  
            :closeModal="closeModal"
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
                <div v-if="teamFlips == 32" class="timer mt-2 flex justify-center">
                    <div :style="{background: primaryColor}" class="done"></div>
                    <div :style="{background: secondaryColor}" class="not-done"></div>
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
    import PlayerPickModal from './/PlayerPickModal.vue';
    import { teamColors } from '../styles/team_colors';
    import { fetchTeamPlayerData, teamPlayerData } from '../services/teamFetch';
    import { teamNames } from '../utils/teamNames';
    import { defineComponent } from 'vue';
    import axios from 'axios';

    export default defineComponent({
        components: {
            PickPlayerBox,
            PlayerPickModal,
        },
        data() {
            return {
                teamIndex: Math.floor(Math.random() * 32),
                flipId: 0,
                teamFlips: 0,
                team: "",
                finalTeam: "",
                primaryColor: "",
                secondaryColor: "",
                image: "",
                players: [{pos: "", name: "", stats: ""}],
                modalOpen: false,
                modalPlayer: {pos: "", name: "", stats: ""}
            };
        },
        methods: {
            openModal(player: any): void {
                this.modalPlayer = player;
                this.modalOpen = true;
            },
            closeModal(): void {
                this.modalOpen = false;
            },
            setColors(): void {
                const fullTeam: string[] = this.team.split(' ');
                var mascot = "";
                if (this.team == "San Francisco 49ers"){
                    mascot = "fortyniners";
                } else {
                    mascot = fullTeam[fullTeam.length - 1].toLowerCase();
                }
                this.primaryColor = teamColors[mascot].primaryColor;
                this.secondaryColor = teamColors[mascot].secondaryColor;
            },
            setImage(): void {
                const abbreviation = teamNames[this.team];
                this.image = `https://static.www.nfl.com/t_person_squared_mobile_2x/f_auto/league/api/clubs/logos/${abbreviation}`
            },
            flipper(): void {
                this.team = Object.keys(teamNames)[this.teamIndex];
                this.setImage();
                this.setColors();
                if (this.teamIndex == 31){
                    this.teamIndex = 0;
                } else {
                    this.teamIndex += 1;
                }
                this.teamFlips += 1;
                if (this.teamFlips == 32){
                    this.team = this.finalTeam;
                    this.setImage();
                    this.setColors();
                    clearInterval(this.flipId);
                }
            }
        },
        async mounted() {
            this.finalTeam = Object.keys(teamNames)[Math.floor(Math.random() * 32)];
            await fetchTeamPlayerData(this.finalTeam);
            this.players = teamPlayerData;
            this.flipId = setInterval(this.flipper, 100);
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
        .timer {
            height: 20px;
            .done {
                width: 90px;
                border-radius: 13px 0 0 13px;
                background: white;
                box-shadow: 0 2px 2px rgba(0, 0, 0, 0.25);
            }
            .not-done {
                width: 120px;
                border-radius: 0 13px 13px 0;
                background: white;
                box-shadow: 0 2px 2px rgba(0, 0, 0, 0.25);
            }
        }
    }
</style>
  