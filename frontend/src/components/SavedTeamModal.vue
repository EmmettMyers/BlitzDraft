<template>
    <div 
        v-on:click="handleClose"
        class="shadow bg-black w-screen h-screen z-20 absolute left-0 top-0 opacity-90">
    </div>
    <div class="savedTeamModal absolute z-30 pb-6 top-32">
        <p 
            v-on:click="handleClose" 
            class="exit text-black font-normal absolute right-5 top-0">
                x
        </p>
        <p class="title font-bold mt-6 ml-8 text-black">
            {{ teamInfo.teamName }}
        </p>
        <p class="desc italic font-light mt-1 ml-8 text-black">
            Drafted {{ teamInfo.date }} by {{ teamInfo.username }}
        </p>
        <p v-if="teamInfo.record != ''" class="desc italic font-light ml-8 text-black">
            Projected Record: <span class="font-medium">{{ teamInfo.record }}</span>
        </p>
        <div class="flex justify-center mt-4">
            <div class="holder bg-black flex justify-center">
                <MyRosterBox 
                    :MP_Players="teamInfo.team"
                    width="430px" 
                />
            </div>
        </div>
    </div>
</template>
  
<script lang="ts">
    import { defineComponent } from 'vue';
    import MyRosterBox from './/MyRosterBox.vue';

    export default defineComponent({
        components: { MyRosterBox },
        props: ['teamInfo', 'closeModal', 'setPage'],
        methods: {
            handleClose(): void {
                this.closeModal();
            },
        }
    });
</script>

<style lang="scss" scoped>
    @import "../styles/colors.scss";
    .savedTeamModal {
        width: 500px;
        background: #D9D9D9;
        border-radius: 13px;
        .exit {
            line-height: 50px;
            font-size: 50px;
            &:hover {
                cursor: pointer;
                color: #5c5c5c;
                transition: .2s;
            }
        }
        .title {
            font-size: 30px;
            line-height: 30px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            width: 400px;
            height: 35px
        }
        .desc {
            font-size: 20px;
            line-height: 25px;
        }
        .holder {
            width: 450px;
            border-radius: 13px;
            padding-top: 5px;
        }
    }
</style>
  