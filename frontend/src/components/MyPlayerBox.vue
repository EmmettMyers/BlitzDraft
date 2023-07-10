<template>
    <div class="playerHolder mt-1 flex justify-center">
        <div class="pos flex justify-center items-center font-bold text-black">
            <p>{{player.pos}}</p>
        </div>
        <div :style="{background: uniqueColor}" class="name flex justify-between items-center pl-6 font-medium">
            <p>{{player.name}}</p>
            <img class="mr-3" :src="image"/>
        </div>
    </div>
</template>
  
<script lang="ts">
    import { teamColors } from '@/styles/team_colors';
    import { teamNames } from '@/utils/teamNames';
    import { defineComponent } from 'vue';
    import { setImage, setColor } from '@/utils/teamSetters';

    interface DataProps {
        team: string;
        uniqueColor: string;
        image: string;
    }

    export default defineComponent({
        props: ['player'],
        data(): DataProps {
            return {
                team: "",
                uniqueColor: "",
                image: "",
            };
        },
        mounted() {
            this.team = this.player.team;
            this.uniqueColor = setColor("unique", this.team);
            if (this.team){
                this.image = setImage(this.team);
            }
        },
    });
</script>

<style lang="scss" scoped>
    @import "../styles/colors.scss";
    .playerHolder {
        font-size: 23px;
        height: 40px;
        .pos {
            width: 100px;
            border-radius: 13px 0 0 13px;
            background: $lightGray;
        }
        .name {
            width: 500px;
            border-radius: 0 13px 13px 0;
        }
        img {
            height: 35px;
        }
    }
</style>
  