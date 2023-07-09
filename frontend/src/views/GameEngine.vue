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
    import io from 'socket.io-client';

    export default defineComponent({
        components: {
            NavBar,
            TeamPickBox,
            MyRosterBox
        },
        methods: {
            /*joinRoom() {
                var socket = io("localhost:5001/");
                socket.on("connect", (data: any) => {
                    alert(data);
                });
            },
            exitRoom() {
                var socket = io("localhost:5001/");
                socket.on("disconnect", (data: any) => {
                    alert(data);
                });
            },*/
        }
    });
</script>

<style lang="scss" scoped>
</style>
  