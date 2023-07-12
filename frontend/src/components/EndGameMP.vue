<template>
    <div class="endGame">
        <div class="flex justify-center">
            <div 
                v-if="textPart >= 0 && textPart <= 4 || textPart == 6 || textPart == 8"  
                class="mainTextBox flex justify-center items-center bg-white text-black font-medium text-center mt-20" 
                :class="((textPart != 8 && textPart != 6) ? 'robotPause' : '')">
                    <p v-if="textPart == 0" class="lg">
                        Hello {{ name }}! My name is Snappy.
                    </p>
                    <p v-if="textPart == 1" class="sm">
                        I am an AI assistant built to determine the overall 
                        strength of an NFL team based on its players.
                    </p>
                    <p v-if="textPart == 2" class="sm">
                        My record calculations are made using a machine learning model 
                        trained with over 50,000 NFL statistics.
                    </p>
                    <p v-if="textPart == 3" class="md">
                        In other words, I should be a pretty good predictor of how good your teams are!
                    </p>
                    <p v-if="textPart == 4" class="lg">
                        Enough about me, let's see the teams everyone put together!
                    </p>
                    <p v-if="textPart == 6" class="lg">
                        Those are the teams!<br>Now, for the rankings...
                    </p>
                    <p v-if="textPart == 8" class="lg">
                        That's all for this BlitzDraft! Thank you all for playing!
                    </p>
            </div>
            <div v-if="textPart == 5 || textPart == 7" class="sideTextBox flex justify-center items-center bg-white 
                text-black font-medium text-center absolute mt-12 ml-44">
                <p v-if="textPart == 5 && showOrder[0] && teamPart == 0" class="sm">
                    Introducing... the team selected by {{ showOrder[0][1] }}!
                </p>
                <p v-if="textPart == 5 && showOrder[1] && teamPart == 1" class="sm">
                    Next up... the team selected by {{ showOrder[1][1] }}!
                </p>
                <p v-if="textPart == 5 && showOrder[2] && teamPart == 2" class="sm">
                    Now... the team selected by {{ showOrder[2][1] }}!
                </p>
                <p v-if="textPart == 5 && showOrder[3] && teamPart == 3" class="sm">
                    Last but not least... the team selected by {{ showOrder[3][1] }}!
                </p>

                <p v-if="textPart == 7 && rankings[3] && rankPart == 0" class="sm">
                    The fourth best team assembled is... <span class="robotPause">{{ rankings[3][1] }}!</span>
                </p>
                <p v-if="textPart == 7 && rankings[2] && rankPart == 1" class="sm">
                    The third best team assembled is... <span class="robotPause">{{ rankings[2][1] }}!</span>
                </p>
                <p v-if="textPart == 7 && rankings[1] && rankPart == 2" class="sm">
                    The second best team assembled is... <span class="robotPause">{{ rankings[1][1] }}!</span>
                </p>
                <p v-if="textPart == 7 && rankings[0] && rankPart == 3" class="sm">
                    And the best team assembled is... <span class="robotPause">{{ rankings[0][1] }}!</span>
                </p>
            </div>
        </div>
        <div class="flex justify-center">
            <div v-if="textPart >= 0 && textPart <= 4 || textPart == 6 || textPart == 8" class="mainTriangle"
                :class="((textPart != 8 && textPart != 6) ? 'robotPause' : '')"></div>
            <div v-if="textPart == 5 || textPart == 7" class="sideTriangle absolute mr-48 mt-32"></div>
        </div>
        <div class="flex justify-center mt-6">
            <img :style="{display:textPart==0?'block':'none'}" class="robot robotGreet" src="../assets/robot.png" />
            <img :style="{display:textPart==1?'block':'none'}" class="robot" src="../assets/robot1.png" />
            <img :style="{display:textPart==2?'block':'none'}" class="robot" src="../assets/robot3.png" />
            <img :style="{display:textPart==3?'block':'none'}" class="robot robotHop" src="../assets/robot2.png" />
            <img :style="{display:textPart==4?'block':'none'}" class="robot" src="../assets/robot.png" />
            <img :style="{display:textPart==5?'block':'none'}" class="robotSmall" src="../assets/robot.png" />
            <img :style="{display:textPart==6?'block':'none'}" class="robot" src="../assets/robot2.png" />
            <img :style="{display:textPart==7?'block':'none'}" class="robotSmall" src="../assets/robot3.png" />
            <img :style="{display:textPart==8?'block':'none'}" class="robot robotWave" src="../assets/robot.png" />
        </div>
        <div v-if="textPart == 7" class="mt-6">
            <div v-if="rankPart >= 3 && rankings[0]" class="robotPause">
                <RankHolder rank="#1" :player="rankings[0][1]" :team="rankings[0][4]" bgColor="#AB9520" />
            </div>
            <div v-if="rankPart >= 2 && rankings[1]" class="robotPause">
                <RankHolder rank="#2" :player="rankings[1][1]" :team="rankings[1][4]" bgColor="#848484" />
            </div>
            <div v-if="rankPart >= 1 && rankings[2]" class="robotPause">
                <RankHolder rank="#3" :player="rankings[2][1]" :team="rankings[2][4]" bgColor="#A26F3D" />
            </div>
            <div v-if="rankPart >= 0 && rankings[3]" class="robotPause">
                <RankHolder rank="#4" :player="rankings[3][1]" :team="rankings[3][4]" bgColor="#7B1A1A" />
            </div>
        </div>
        <div v-if="textPart == 5">
            <MyRosterBox 
                v-if="rankings[0] && teamPart == 0"
                :MP_Players="rankings[0][4]"
                class="mt-8 playersPause" 
                width="550px" 
            />
            <MyRosterBox 
                v-if="rankings[1] && teamPart == 1"
                :MP_Players="rankings[1][4]"
                class="mt-8 playersPause" 
                width="550px" 
            />
            <MyRosterBox 
                v-if="rankings[2] && teamPart == 2"
                :MP_Players="rankings[2][4]"
                class="mt-8 playersPause" 
                width="550px" 
            />
            <MyRosterBox 
                v-if="rankings[3] && teamPart == 3"
                :MP_Players="rankings[3][4]"
                class="mt-8 playersPause" 
                width="550px" 
            />
        </div>
    </div>
</template>

<script lang="ts">
    import { defineComponent } from 'vue';
    import MyRosterBox from './/MyRosterBox.vue';
    import RankHolder from './/RankHolder.vue';
    import { projectedRecord } from '@/services/modelFetch';
    import { room, roomPlayers, roomTeamRankings } from '@/services/roomHandler';

    export default defineComponent({
        props: ['gameDone'],
        components: {
            MyRosterBox, RankHolder
        },
        data() {
            return {
                name: "everyone",
                textPart: 0,
                projectedRecord: projectedRecord,
                playerCount: roomPlayers.value.length,
                rankings: roomTeamRankings,
                showOrder: roomTeamRankings,
                teamPart: 0,
                rankPart: 0
            };
        },
        mounted() {
            let showTime = 7000 * this.showOrder.length;
            let rankTime = 4000 * this.showOrder.length;
            this.showOrder = this.showOrder.sort(() => Math.random() - 0.5);
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
                                setInterval(() => {
                                    this.teamPart++;
                                }, 7000);
                                setTimeout(() => {
                                    this.textPart++;
                                    setTimeout(() => {
                                        this.textPart++;
                                        setInterval(() => {
                                            this.rankPart++;
                                        }, 4000);
                                        setTimeout(() => {
                                            this.textPart++;
                                            setTimeout(() => {
                                                this.gameDone();
                                            }, 4000);
                                        }, rankTime);
                                    }, 4000);
                                }, showTime);
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
            margin-top: 60px;
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