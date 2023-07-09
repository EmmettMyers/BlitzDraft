<template>
    <div class="flex justify-center w-screen pb-4">
        <div class="myRosterBox">
            <p class="myRosterTxt pt-2">My Roster</p>
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

    export default defineComponent({
        components: {
            MyPlayerBox,
        },
        data() {
            return {
                players: [
                        { pos: 'QB', name: '', team: '' },
                        { pos: 'RB', name: '', team: '' },
                        { pos: 'WR1', name: '', team: '' },
                        { pos: 'WR2', name: '', team: '' },
                        { pos: 'WR3', name: '', team: '' },
                        { pos: 'TE', name: '', team: '' },
                        { pos: 'OL', name: '', team: '' },
                        { pos: 'DEF', name: '', team: '' },
                    ]
            };
        },
    });
</script>

<style lang="scss" scoped>
    @import "../styles/colors.scss";
    .myRosterBox {
        width: 600px;
        .myRosterTxt {
            font-size: 30px;
        }
    }
</style>
  