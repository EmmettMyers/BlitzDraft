<template>
    <div class="playerPickModalStats flex justify-center mt-2">
        <div :style="{background: primaryColor}" class="statName flex justify-center items-center font-semibold">
            <p>{{ statName }}</p>
        </div>
        <div :style="{background: secondaryColor}" class="statNum flex justify-center items-center font-extrabold">
            <p :style="{color: primaryColor}">{{ stat }}</p>
        </div>
    </div>
</template>
  
<script lang="ts">
    import { defineComponent } from 'vue';

    export default defineComponent({
        props: ['stat', 'statName', 'primaryColor', 'secondaryColor'],
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
  