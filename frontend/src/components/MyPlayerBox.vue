<template>
    <div class="playerHolder mt-1 flex justify-center">
        <div class="pos flex justify-center items-center font-bold text-black">
            <p>{{player.pos}}</p>
        </div>
        <div :style="{background: secondaryColor}" class="name flex justify-between items-center pl-7 font-medium">
            <p>{{player.name}}</p>
            <img :src="player.team_image"/>
        </div>
    </div>
</template>
  
<script lang="ts">
    import { teamColors } from '@/styles/team_colors';
    import { defineComponent } from 'vue';

    export default defineComponent({
        props: ['player'],
        data() {
            return {
                team: "",
                primaryColor: "",
                secondaryColor: "",
                image: "https://logos-world.net/wp-content/uploads/2020/05/Houston-Texans-logo.png",
            };
        },
        methods: {
            setColors(): void {
                if (this.team != ""){
                    const fullTeam: string[] = this.team.split(' ');
                    const mascot: string = fullTeam[fullTeam.length - 1].toLowerCase();
                    this.primaryColor = teamColors[mascot].primaryColor;
                    this.secondaryColor = teamColors[mascot].secondaryColor;   
                } else {
                    this.primaryColor = "#414141";
                    this.secondaryColor = "#414141";  
                }
            }
        },
        mounted() {
            this.setColors();
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
  