<template>
    <div class="">
        <NavBar />
        <TeamPickBox />
        <MyRosterBox />
    </div>
</template>

<script lang="ts">
    import { defineComponent } from 'vue';
    import NavBar from '../components/NavBar.vue';
    import TeamPickBox from '../components/TeamPickBox.vue';
    import MyRosterBox from '../components/MyRosterBox.vue';

    export default defineComponent({
        components: {
            NavBar,
            TeamPickBox,
            MyRosterBox
        },
        methods: {
        }
    });
</script>

<style lang="scss" scoped>
</style>
  