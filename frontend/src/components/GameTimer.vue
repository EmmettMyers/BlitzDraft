<template>
    <div :style="{ background: secondaryColor }" class="timer mt-2 flex justify-center">
        <div :style="{ background: primaryColor, width: doneWidth + 'px' }" class="done"></div>
        <div :style="{ background: secondaryColor, width: notDoneWidth + 'px' }" class="not-done"></div>
    </div>
</template>

<script lang="ts">
    import { defineComponent } from 'vue';

    export default defineComponent({
        props: ['primaryColor', 'secondaryColor', 'timeDone', 'selectIndex'],
        data() {
            return {
                doneWidth: 1,
                notDoneWidth: 209
            }
        },
        mounted() {
            const intervalId = setInterval(() => {
                this.doneWidth += 0.05;
                this.notDoneWidth -= 0.05;
                if (this.notDoneWidth < 0.05){
                    clearInterval(intervalId);
                    this.timeDone(this.selectIndex);
                }
            }, 3);
        },
    });
</script>

<style lang="scss" scoped>
    @import "../styles/colors.scss";
    .timer {
        height: 20px;
        border-radius: 13px !important;
        .done, .not-done {
            box-shadow: 0 2px 2px rgba(0, 0, 0, 0.25);
        }
        .done {
            border-radius: 13px 0 0 13px !important;
        }
        .not-done {
            border-radius: 0 13px 13px 0 !important;
        }
    }
</style>
  