<template>
    <div class="w-screen h-screen flex justify-center items-center">
        <div :style="waitForImage" class="loginPage mb-20">
            <img class="mainLogo" @load="imageLoaded" src="../assets/longLogo1.png" />
            <p class="motto text-center font-light mt-2">
                Pick players from random NFL teams,<br>build the best roster possible!
            </p>
            <div class="flex justify-center google mt-8">
                <img @load="imageLoaded" v-on:click="signIn" src="../assets/googleBtn.png" />
            </div>
            <img 
                class="stadium absolute left-0 top-0 w-screen h-screen object-cover" 
                src="../assets/raidersStadium.jpg" 
            />
        </div>
    </div>
</template>

<script lang="ts">
    import { defineComponent } from 'vue';
    import { googleSignIn } from '@/services/firebase';

    export default defineComponent({
        props: ['setPage'],
        data() {
            return {
                waitForImage: "display: none"
            }
        },
        methods: {
            imageLoaded(): void {
                this.waitForImage = "display: block"
            },
            signIn(): void {
                googleSignIn();
            },
        }
    });
</script>

<style lang="scss" scoped>
    .loginPage {
        width: 600px;
        .mainLogo {
            filter: drop-shadow(0px 10px 10px rgba(0, 0, 0, 0.5));
        }
        .motto {
            font-size: 30px;
            text-shadow: 0px 10px 10px rgba(0, 0, 0, 0.5);
        }
        .google img {
            width: 350px;
            &:hover {
                cursor: pointer;
                transition: .2s;
                filter: brightness(110%);
            }
        }
        .stadium {
            z-index: -1;
            opacity: .15;
            box-shadow: 0px 10px 10px rgba(0, 0, 0, 0.5);
        }
    }
</style>