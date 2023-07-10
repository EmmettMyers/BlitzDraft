<template>
    <div v-if="selectable" v-on:click="openModal(player)" class="playerHolder active mt-1 flex justify-center">
        <div :style="{background: primaryColor}" class="pos flex justify-center items-center font-bold">
            <p>{{player.pos}}</p>
        </div>
        <div :style="{background: secondaryColor}" class="name flex justify-center items-center font-semibold">
            <p :style="{color: primaryColor}">{{player.name}}</p>
        </div>
    </div>
    <div v-else class="playerHolder mt-1 flex justify-center">
        <div style="background: #414141" class="pos flex justify-center items-center font-bold">
            <p style="color: black">{{player.pos}}</p>
        </div>
        <div style="background: #414141" class="name flex justify-center items-center font-semibold">
            <p style="color: black">{{player.name}}</p>
        </div>
    </div>
</template>
  
<script lang="ts">
    import { myPlayers } from '@/utils/myPlayers';
    import { defineComponent } from 'vue';

    export default defineComponent({
        props: ['player', 'primaryColor', 'secondaryColor', 'openModal'],
        data() {
            return {
                selectable: true
            }
        },
        mounted() {
            const player = myPlayers.value.find((player) => player.pos === this.player.pos);
            if (!!player && player.name !== ''){
                this.selectable = false;
            }
        }
    });
</script>

<style lang="scss" scoped>
    @import "../styles/colors.scss";
    .playerHolder {
        font-size: 18px;
        height: 30px;
        .pos {
            width: 70px;
            border-radius: 13px 0 0 13px;
            box-shadow: 0 2px 2px rgba(0, 0, 0, 0.25);
        }
        .name {
            width: 250px;
            border-radius: 0 13px 13px 0;
            box-shadow: 0 2px 2px rgba(0, 0, 0, 0.25);
        }
    }
    .active {
        &:hover {
            cursor: pointer;
            filter: brightness(80%);
            transition: .2s;
        }
    }
</style>
  