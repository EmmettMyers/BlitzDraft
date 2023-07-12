<template>
    <div class="endGame">
        <div class="flex justify-center">
            <div v-if="textPart >= 0 && textPart <= 4 || textPart == 7"  class="mainTextBox flex justify-center items-center bg-white 
                text-black font-medium text-center mt-20" :class="(textPart != 7 ? 'robotPause' : '')">
                <p v-if="textPart == 0" class="lg robotPause">
                    Hello {{ name }}! My name is Snappy.
                </p>
                <p v-if="textPart == 1" class="sm">
                    I am an AI assistant built to predict the regular season record of 
                    an NFL team based on its players.
                </p>
                <p v-if="textPart == 2" class="sm">
                    My record calculations are made using a machine learning model 
                    trained with over 50,000 NFL statistics.
                </p>
                <p v-if="textPart == 3" class="md">
                    In other words, I should be a pretty good predictor of how good your team is!
                </p>
                <p v-if="textPart == 4" class="lg">
                    Enough about me, let's see the team you put together!
                </p>
                <p v-if="textPart == 7" class="lg">
                    That's all for this BlitzDraft! Thank you for playing!
                </p>
            </div>
            <div v-if="textPart == 5 || textPart == 6" class="sideTextBox flex justify-center items-center bg-white 
                text-black font-medium text-center absolute mt-8 ml-44">
                <p v-if="textPart == 5" class="md">
                    Here is the team you drafted!
                </p>
                <p v-if="textPart == 6" class="sm">
                    Your team's regular season record prediction is:
                </p>
            </div>
        </div>
        <div class="flex justify-center">
            <div v-if="textPart >= 0 && textPart <= 4 || textPart == 7" class="mainTriangle"
                :class="(textPart != 7 ? 'robotPause' : '')"></div>
            <div v-if="textPart == 5 || textPart == 6" class="sideTriangle absolute mr-48 mt-28"></div>
        </div>
        <div class="flex justify-center mt-6">
            <img :style="{display:textPart==0?'block':'none'}" class="robot robotGreet" src="../assets/robot.png" />
            <img :style="{display:textPart==1?'block':'none'}" class="robot" src="../assets/robot1.png" />
            <img :style="{display:textPart==2?'block':'none'}" class="robot" src="../assets/robot3.png" />
            <img :style="{display:textPart==3?'block':'none'}" class="robot robotHop" src="../assets/robot2.png" />
            <img :style="{display:textPart==4?'block':'none'}" class="robot" src="../assets/robot.png" />
            <img :style="{display:textPart==5?'block':'none'}" class="robotSmall" src="../assets/robot.png" />
            <img :style="{display:textPart==6?'block':'none'}" class="robotSmall" src="../assets/robot3.png" />
            <img :style="{display:textPart==7?'block':'none'}" class="robot robotWave" src="../assets/robot.png" />
        </div>
        <div class="flex justify-center">
            <div v-if="textPart == 6" class="recordHolder flex justify-center items-center bg-white 
            text-black font-black text-center recordPause">
                <p>{{ projectedRecord }}</p>
            </div>
        </div>
        <MyRosterBox v-if="textPart == 5 || textPart == 6" class="mt-8 playersPause" width="550px" />
    </div>
</template>

<script lang="ts">
    import { defineComponent } from 'vue';
    import MyRosterBox from './/MyRosterBox.vue';
    import { projectedRecord } from '@/services/modelFetch';

    export default defineComponent({
        props: ['gameDone'],
        components: {
            MyRosterBox
        },
        data() {
            return {
                name: "Emmett",
                textPart: 0,
                projectedRecord: projectedRecord
            };
        },
        mounted() {
            setTimeout(() => {
                this.textPart++;
                setTimeout(() => {
                    this.textPart++;
                    setTimeout(() => {
                        this.textPart++;
                        setTimeout(() => {
                            this.textPart++;
                            setTimeout(() => {
                                this.textPart++;
                                setTimeout(() => {
                                    this.textPart++;
                                    setTimeout(() => {
                                        this.textPart++;
                                        setTimeout(() => {
                                            this.gameDone();
                                        }, 4000);
                                    }, 7000);
                                }, 5000);
                            }, 2500);
                        }, 3000);
                    }, 4000);
                }, 4000);
            }, 4000);
        }
    });
</script>

<style lang="scss" scoped>
    @import "../styles/colors.scss";
    .endGame {
        .recordHolder {
            width: 225px;
            height: 80px;
            border-radius: 13px;
            background: #FFE500;
            p {
                font-size: 50px;
            }
        }
        .mainTextBox {
            width: 450px;
            height: 220px;
            border-radius: 13px;
        }
        .mainTriangle {
            width: 0;
            height: 0;
            border-left: 20px solid transparent;
            border-right: 20px solid transparent;
            border-top: 30px solid white;
        }
        .sideTriangle {
            width: 0;
            height: 0;
            border-bottom: 10px solid transparent;
            border-right: 20px solid white;
            border-top: 10px solid transparent;
        }
        .sideTextBox {
            width: 350px;
            height: 150px;
            border-radius: 13px;
        }
        .mainTextBox p, .sideTextBox p {
            margin-bottom: 5px;
        }
        .lg {
            font-size: 35px;
            padding: 40px;
            line-height: 45px;
        }
        .md {
            font-size: 32px;
            padding: 55px;
            line-height: 40px;
        }
        .sm {
            font-size: 28px;
            padding: 45px;
            line-height: 38px;
        }
        .robot {
            width: 300px;
        }
        .robotSmall {
            width: 150px;
            margin-right: 380px;
            margin-top: 45px;
        }
        .robotGreet {
            animation: rotateAndFadeIn 2s 1;
        }
        @keyframes rotateAndFadeIn {
            0% { opacity: 0; }
            33% { opacity: 0; }
            70% { transform: rotateZ(0deg); }
            80% { transform: rotateZ(10deg); }
            90% { transform: rotateZ(-10deg); }
            100% { transform: rotateZ(0deg); opacity: 1; }
        }
        .robotWave {
            animation: rotate 0.75s 1 0.25s;
        }
        @keyframes rotate {
            0% { transform: rotateZ(0deg); }
            33% { transform: rotateZ(10deg); }
            66% { transform: rotateZ(-10deg); }
            100% { transform: rotateZ(0deg); }
        }
        .robotHop {
            animation: moveUpDown 0.5s 1;
        }
        @keyframes moveUpDown {
            0% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
            100% { transform: translateY(0); }
        }
        .playersPause {
            animation: fadeIn 0.25s;
        }
        .recordPause {
            animation: slowFadeIn 2s;
        }
        .robotPause {
            animation: slowFadeIn 1s;
        }
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        @keyframes slowFadeIn {
            0% { opacity: 0; }
            66% { opacity: 0; }
            100% { opacity: 1; }
        }
    }

</style>
  @/services/modelFetch