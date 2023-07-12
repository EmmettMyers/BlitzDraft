<template>
    <div class="flex justify-center">
        <div class="waitingMP mt-2">
            <p class="complete text-black font-bold text-center mt-10">
                Your draft<br>is <span class="font-black text-green-700">complete</span>.
            </p>
            <p class="waiting text-black font-medium text-center mt-6 italic">
                Waiting for other players...
            </p>
        </div>
    </div>
    <MyRosterBox showTxt="true" width="600px" />
</template>

<script lang="ts">
    import { defineComponent } from 'vue';
    import MyRosterBox from '../components/MyRosterBox.vue';

    export default defineComponent({
        components: { MyRosterBox },
        data() {
            return {
                doneWidth: 1,
                notDoneWidth: 209
            }
        }
    });
</script>

<style lang="scss" scoped>
    @import "../styles/colors.scss";
    .waitingMP {
        width: 600px;
        height: 300px;
        background: $lightGray;
        border-radius: 13px;
        .complete {
            font-size: 65px;
            line-height: 70px;
        }
        .waiting {
            font-size: 30px;
        }
    }
</style>