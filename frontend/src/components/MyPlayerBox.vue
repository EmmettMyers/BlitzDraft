<template>
    <div class="playerHolder mt-1 flex justify-center">
        <div class="pos flex justify-center items-center font-bold text-black">
            <p>{{player.pos}}</p>
        </div>
        <div :style="{background: primaryColor}" class="name flex justify-between items-center pl-6 font-medium">
            <p>{{player.name}}</p>
            <img class="mr-3" :src="image"/>
        </div>
    </div>
</template>
  
<script lang="ts">
    import { teamColors } from '@/styles/team_colors';
    import { teamNames } from '@/utils/teamNames';
    import { defineComponent } from 'vue';

    interface DataProps {
        team: string;
        primaryColor: string;
        secondaryColor: string;
        image: string;
    }

    export default defineComponent({
        props: ['player'],
        data(): DataProps {
            return {
                team: "",
                primaryColor: "",
                secondaryColor: "",
                image: "",
            };
        },
        methods: {
            setColors(): void {
                if (this.team != ""){
                    const fullTeam: string[] = this.team.split(' ');
                    var mascot = "";
                    if (this.team == "San Francisco 49ers"){
                        mascot = "fortyniners";
                    } else {
                        mascot = fullTeam[fullTeam.length - 1].toLowerCase();
                    }
                    this.primaryColor = teamColors[mascot].primaryColor;
                    this.secondaryColor = teamColors[mascot].secondaryColor;   
                } else {
                    this.primaryColor = "#414141";
                    this.secondaryColor = "#414141";  
                }
            },
            setImage(): void {
                const abbreviation = teamNames[this.team];
                this.image = `https://static.www.nfl.com/t_person_squared_mobile_2x/f_auto/league/api/clubs/logos/${abbreviation}`
            },
        },
        mounted() {
            this.team = this.player.team;
            this.setColors();
            if (this.team){
                this.setImage();
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
  