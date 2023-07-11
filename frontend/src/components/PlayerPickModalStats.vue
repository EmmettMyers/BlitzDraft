<template>
    <div v-if="showStat" class="playerPickModalStats flex justify-center mt-2">
        <div :style="{background: primaryColor}" class="statName flex justify-center items-center font-semibold">
            <p>{{ statName }}</p>
        </div>
        <div class="bg-white statNum flex justify-center items-center font-extrabold">
            <p :style="{color: primaryColor}">{{ stat }}</p>
        </div>
    </div>
</template>
  
<script lang="ts">
    import { defineComponent } from 'vue';

    export default defineComponent({
        props: ['pos', 'index', 'stat', 'statName', 'primaryColor', 'secondaryColor'],
        data() {
            return {
                showStat: true
            };
        },
        mounted() {
            if (this.pos == 'QB' && this.index == 0){
                this.showStat = false;
            } else if (this.pos == 'RB' && this.index == 3){
                this.showStat = false;
            } else if (this.pos == 'DEF' && this.index == 1){
                this.showStat = false;
            }
        }
    });
</script>

<style lang="scss" scoped>
    @import "../styles/colors.scss";
    .playerPickModalStats {
        height: 55px;
        .statName {
            font-size: 20px;
            width: 145px;
            border-radius: 13px 0 0 13px;
            box-shadow: 0 2px 2px rgba(0, 0, 0, 0.25);
        }
        .statNum {
            font-size: 28px;
            width: 125px;
            border-radius: 0 13px 13px 0;
            box-shadow: 0 2px 2px rgba(0, 0, 0, 0.25);
        }
    }
</style>
  