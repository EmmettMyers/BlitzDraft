<template>
    <div class="flex justify-center w-screen pb-4">
        <div class="myRosterBox" :style="{width: width}">
            <p v-if="showTxt" class="myRosterTxt pt-2 pl-2">My Roster</p>
            <div v-for="player in players" :key="player.name">
                <MyPlayerBox :player="player" />
            </div>
        </div>
    </div>
</template>
  
<script lang="ts">
    import axios from 'axios';
    import MyPlayerBox from './/MyPlayerBox.vue';
    import { defineComponent } from 'vue';
    import { myPlayers } from '@/utils/myPlayers';

    export default defineComponent({
        components: {
            MyPlayerBox,
        },
        props: ['MP_Players', 'showTxt', 'width'],
        data() {
            return {
                players: myPlayers
            };
        },
        mounted() {
            if (this.MP_Players){
                this.players = this.MP_Players;
            }
        }
    });
</script>

<style lang="scss" scoped>
    @import "../styles/colors.scss";
    .myRosterBox {
        .myRosterTxt {
            font-size: 30px;
        }
    }
</style>
  