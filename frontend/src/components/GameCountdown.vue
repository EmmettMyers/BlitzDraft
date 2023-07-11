<template>
    <div class="countdown flex justify-center items-center">
        <p class="font-black text-center">{{ num }}</p>
    </div>
</template>

<script lang="ts">
    import { defineComponent } from 'vue';

    export default defineComponent({
        props: ['countdownComplete'],
        data() {
            return {
                num: 3
            };
        },
        mounted() {
            setTimeout(() => {
                this.num--;
                setTimeout(() => {
                    this.num--;
                    setTimeout(() => {
                        this.countdownComplete();
                    }, 1000);
                }, 1000);
            }, 1000);
        }
    });
</script>

<style lang="scss" scoped>
    @import "../styles/colors.scss";
    .countdown {
        height: 75vh;
        p {
            font-size: 200px;
        }
    }

</style>
  