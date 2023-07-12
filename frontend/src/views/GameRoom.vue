<template>
    <div class="w-screen h-screen flex justify-center items-center">
        <div :style="waitForImage" class="gameRoom">
            <div class="flex justify-center">
                <img @load="imageLoaded" src="../assets/bdRoom.png" />
            </div>
            <p class="codeTitle text-regular mt-6">Room Code</p>
            <div class="code font-black flex justify-center items-center">{{ roomId }}</div>
            <div   
                v-on:click="leaveRoom"
                class="leave font-semibold flex justify-center items-center mt-2">
                    Leave Room
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
    import { leaveRoom, room, roomError, roomPlayers } from '@/services/roomHandler';
    import { defineComponent } from 'vue';

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
            leaveRoom(): void {
                leaveRoom();
                this.setPage('home');
            },
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
            height: 120px;
            font-size: 60px;
            padding-bottom: 5px;
            border-radius: 13px;
            background: #00349F;
        }
        .leave {
            height: 40px;
            font-size: 20px;
            padding-bottom: 5px;
            border-radius: 13px;
            background: #A82323;
            &:hover {
                cursor: pointer;
                transition: .2s;
                filter: brightness(120%);
            }
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