<template>
    <div class="w-screen h-screen flex justify-center items-center">
        <div :style="waitForImage" class="gameRoom">
            <div class="flex justify-center">
                <img @load="imageLoaded" src="../assets/bdRoom.png" />
            </div>
            <p class="codeTitle text-regular mt-6">Room Code</p>
            <div class="code font-black flex justify-center items-center">{{ roomId }}</div>
            <div class="flex justify-center mt-2">
                <div   
                    v-on:click="startGame"
                    class="start font-semibold flex justify-center items-center">
                        Start Game
                </div>
                <div   
                    v-on:click="leaveRoom"
                    class="leave font-semibold flex justify-center items-center">
                        Exit
                </div>
            </div>
            <p class="codeTitle text-regular mt-2">Players 
                <span class="font-bold playerCount">({{ players.length }}/4)</span></p>
            <div 
                v-for="player in players" :key="player.name"
                class="player font-medium flex justify-center items-center mt-1">
                    {{ player.name }}
            </div>
        </div>
    </div>
</template>

<script lang="ts">
    import { leaveRoom, room, roomPlayers, startMPGame, startGame } from '@/services/roomHandler';
    import { defineComponent, getCurrentInstance, watch } from 'vue';

    export default defineComponent({
        props: ['setPage'],
        data() {
            return {
                waitForImage: "display: none",
                modalOpen: false,
                roomId: room,
                players: roomPlayers
            }
        },
        methods: {
            imageLoaded(): void {
                this.waitForImage = "display: block"
            },
            startGame(): void {
                startGame();
            },
            leaveRoom(): void {
                leaveRoom();
                this.setPage('home');
            },
        },
        setup() {
            const instance = getCurrentInstance();
            const setPage = (instance!.proxy as any).setPage;
            watch(startMPGame, async (newState, oldState) => {
                if (newState){
                    setPage('game');
                }
            });
        }
    });
</script>

<style lang="scss" scoped>
    .gameRoom {
        width: 400px;
        img {
            width: 400px;
        }
        .codeTitle  {
            font-size: 30px;
            .playerCount {
                color: #FFE500; 
                font-size: 25px;
            }
        }
        .code {
            letter-spacing: 10px;
            padding-left: 10px;
            height: 120px;
            font-size: 60px;
            padding-bottom: 5px;
            border-radius: 13px;
            background: #00349F;
        }
        .start, .leave {
            height: 40px;
            font-size: 20px;
            padding-bottom: 5px;
            border-radius: 13px 0 0 13px;
            background: #14721D;
            &:hover {
                cursor: pointer;
                transition: .2s;
                filter: brightness(120%);
            }
        }
        .start {
            width: 400px;
            border-radius: 13px 0 0 13px;
            background: #14721D;
        }
        .leave {
            width: 100px;
            border-radius: 0 13px 13px 0;
            background: #A82323;
        }
        .player {
            height: 60px;
            font-size: 25px;
            padding-bottom: 5px;
            border-radius: 13px;
            background: #B05A0B;
        }
    }
</style>