<template>
    <div 
        v-on:click="handleClose"
        class="shadow bg-black w-screen h-screen z-20 absolute left-0 top-0 opacity-90">
    </div>
    <div :class="join ? 'mt-20' : 'mt-32'" class="multiplayerModal absolute z-30 pb-10">
        <p 
            v-on:click="handleClose" 
            class="exit text-black font-normal absolute right-5 top-0">
                x
        </p>
        <p class="txt text-regular mt-6 ml-8 text-black">Select an option:</p>
        <div class="flex justify-center mt-1">
            <div 
                v-on:click="createRoom" 
                class="create font-semibold flex justify-center items-center">
                    Create Room
            </div>
            <div 
                v-on:click="setJoin(true)" 
                class="join font-semibold flex justify-center items-center">
                    Join Room
            </div>
        </div>
        <div v-if="join">
            <p class="txt text-regular mt-6 ml-8 text-black">Enter room code:</p>
            <div class="flex justify-center mt-1">
                <input 
                    v-model="roomCode"
                    class="input font-normal text-black flex justify-center items-center pl-4">
                <div 
                    v-on:click="joinRoom"
                    class="submit font-semibold flex justify-center items-center">
                        Join
                </div>
            </div>
        </div>
        <p v-if="error" class="font-medium error text-center text-red-700 mt-3">
            That room does not exist. Please try again.
        </p>
    </div>
</template>
  
<script lang="ts">
    import { defineComponent } from 'vue';
    import { createRoom, joinRoom, roomError } from '../services/roomHandler';

    export default defineComponent({
        props: ['closeModal', 'setPage'],
        data() {
            return {
                join: false,
                roomCode: '',
                error: roomError
            };
        },
        methods: {
            handleClose(): void {
                roomError.value = false;
                this.closeModal();
            },
            setJoin(val: boolean): void {
                this.join = val;
            },
            async createRoom(): Promise<void> {
                await createRoom();
                this.setPage('room');
            },
            async joinRoom(): Promise<void> {
                await joinRoom(this.roomCode);
                setTimeout(() => {
                    if (!roomError.value){
                        this.setPage('room');
                    }
                }, 500);
            }
        }
    });
</script>

<style lang="scss" scoped>
    @import "../styles/colors.scss";
    .multiplayerModal {
        width: 600px;
        background: #D9D9D9;
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
        .error {
            font-size: 25px;
        }
        .txt  {
            font-size: 30px;
        }
        .create, .join {
            width: 270px;
            height: 90px;
            font-size: 30px;
            padding-bottom: 8px;
            &:hover {
                cursor: pointer;
                transition: .2s;
                filter: brightness(120%);
            }
        }
        .create {
            border-radius: 13px 0 0 13px;
            background: #174FBF;
        }
        .join {
            border-radius: 0 13px 13px 0;
            background: #072A71;
        }
        .input {
            border-radius: 13px 0 0 13px;
            background: #A7A7A7;
            width: 420px;
            height: 50px;
            font-size: 25px;
        }
        .submit {
            border-radius: 0 13px 13px 0;
            background: #077712;
            width: 120px;
            height: 50px;
            font-size: 25px;
            padding-bottom: 3px;
            &:hover {
                cursor: pointer;
                transition: .2s;
                filter: brightness(120%);
            }
        }
    }
</style>
  