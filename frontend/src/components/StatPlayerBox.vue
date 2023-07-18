<template>
    <div
        :style="{background: uniqueColor, height: height}"
        class="statPlayerBox mt-1 flex justify-center items-center font-bold">
            {{ name }}
    </div>
</template>
  
<script lang="ts">
    import { defineComponent } from 'vue';
    import { setImage, setColor } from '@/utils/teamSetters';

    export default defineComponent({
        props: ['name', 'team', 'height'],
        data() {
            return {
                uniqueColor: ""
            };
        },
        mounted() {
            //alert(this.name + " " + this.team);
            this.uniqueColor = setColor("unique", this.team);
        },
    });
</script>

<style lang="scss" scoped>
    @import "../styles/colors.scss";
    .statPlayerBox {
        width: 295px;
        height: 35px;
        background: #174FBF;
        border-radius: 13px;
        font-size: 18px;
    }
    .teamBox {
        width: 295px;
        height: 38px;
        background: #174FBF;
        border-radius: 13px;
        font-size: 18px;
    }
</style>
  @/utils/styleSetters