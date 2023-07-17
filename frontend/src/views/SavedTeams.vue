<template>
    <div class="w-screen h-screen flex justify-center items-center">
        <div :style="waitForImage" class="savedTeams mb-10">
            <SavedTeamModal v-if="modalOpen" :teamInfo="team" :closeModal="closeModal" :setPage="setPage" />
            <img @load="imageLoaded" src="../assets/bdTeams.png" />
            <div class="flex justify-center font-medium mt-3">
                <div 
                    v-on:click="deleteTeams"
                    :class="{'bdr' : deleting}"
                    class="delete flex justify-center items-center">
                        Delete Teams
                </div>
                <div 
                    v-on:click="setPage('home')" 
                    class="exit flex justify-center items-center">
                        Exit
                </div>
            </div>
            <p v-if="deleting" class="deleteTxt italic font-light mt-3">Click a team to delete it.</p>
            <p :class="deleting ? 'mt-2' : 'mt-5'" class="teamsTxt text-regular">Saved teams</p>
            <div :style="waitForTeams" v-for="team in teams" :key="team.teamName">
                <div 
                    v-on:click="handleTeamClick(team)"
                    :class="{'redShade' : deleting}"
                    class="team font-bold flex justify-center items-center mt-2">
                        {{ team.teamName }}
                </div>
            </div>
            <div class="flex justify-center">
                <div v-if="waitForTeams == 'display: none'" class="lds-ring mt-2">
                    <div></div><div></div><div></div><div></div></div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
    import { setSavedTeams, savedTeams, deleteTeam } from '@/services/savedTeams';
    import { defineComponent } from 'vue';
    import SavedTeamModal from '../components/SavedTeamModal.vue';

    export default defineComponent({
        components: { SavedTeamModal },
        props: ['setPage'],
        data() {
            return {
                waitForImage: "display: none",
                waitForTeams: "display: none",
                teams: savedTeams,
                modalOpen: false,
                team: [],
                deleting: false
            }
        },
        methods: {
            imageLoaded(): void {
                this.waitForImage = "display: block"
            },
            teamsLoaded(): void {
                this.waitForTeams = "display: block"
            },
            handleTeamClick(team: any): void {
                if (this.deleting){
                    deleteTeam(team.teamName);
                } else {
                    this.team = team;
                    this.modalOpen = true;
                }
            },
            closeModal(): void {
                this.modalOpen = false;
            },
            deleteTeams(): void {
                this.deleting = !this.deleting;
            },
        },
        async mounted(){
            await setSavedTeams();
            this.teamsLoaded();
        }
    });
</script>

<style lang="scss" scoped>
    .savedTeams {
        width: 500px;
        .deleteTxt {
            font-size: 30px;
            color: #EE697D;
        }
        .delete, .exit {
            height: 50px;
            font-size: 25px;
            padding-bottom: 3px;
        }
        .delete {
            border-radius: 13px 0 0 13px;
            width: 375px; 
            background: #5C0A0A;
            &:hover {
                cursor: pointer;
                border: 5px solid red;
                transition: .1s;
            }
        }
        .bdr {
            border: 5px solid red;
        }
        .exit {
            border-radius: 0 13px 13px 0;
            width: 125px;
            background: #A82323;
            &:hover {
                cursor: pointer;
                filter: brightness(120%);
                transition: .1s;
            }
        }
        .teamsTxt {
            font-size: 30px;
        }
        .team {
            height: 70px;
            font-size: 30px;
            border-radius: 13px;
            padding-bottom: 3px;
            width: 500px;
            background: #174FBF;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            &:hover {
                cursor: pointer;
                filter: brightness(120%);
                transition: .2s;
            }
        }
        .redShade {
            &:hover {
                background: #A82323 !important;
            }
        }
        .lds-ring {
            width: 80px;
            height: 80px;
        }
        .lds-ring div {
            box-sizing: border-box;
            display: block;
            position: absolute;
            width: 80px;
            height: 80px;
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