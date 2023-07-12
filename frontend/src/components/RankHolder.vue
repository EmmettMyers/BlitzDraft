<template>
    <div class="rankBox flex justify-center mt-2">
        <div class="rank text-black font-black flex justify-center items-center">{{ rank }}</div>
        <div class="player" :style="{background: color}">
            <div class="name ml-4 font-bold mt-1">
                {{ player }}
            </div>
            <div class="team ml-5 font-normal pr-4">
                {{ (team as any[]).map(player => player.name).join(', ') }}
            </div>
        </div>
    </div>
</template>
  
<script lang="ts">
    import { defineComponent } from 'vue';

    export default defineComponent({
        props: ['rank', 'player', 'team', 'bgColor'],
        data() {
            return {
                color: this.bgColor
            };
        }
    });
</script>

<style lang="scss" scoped>
    @import "../styles/colors.scss";
    .rankBox {
        height: 100px;
        .rank {
            border-radius: 13px 0 0 13px;
            width: 120px;
            background: #E4E4E4;
            font-size: 50px;
        }
        .player {
            border-radius: 0 13px 13px 0;
            width: 430px;
            .name {
                font-size: 30px;
                line-height: 45px;
            }
            .team {
                font-size: 13px;
            }
        }
    }
</style>
  