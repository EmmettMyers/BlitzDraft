<template>
    <div class="bg-white holder">
        <Bar
            id="my-chart-id"
            :options="chartOptions"
            :data="data"
            class="chart p-2"
            style="height: 200px;"
        />
    </div>
</template>

<script lang="ts">
    import { Bar } from 'vue-chartjs'
    import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
    import { allRecords } from '@/services/statistics'

    ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

    export default {
        name: 'BarChart',
        props: ['records'],
        components: { Bar },
        data() {
            return {
                data: {
                    labels: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'],
                    datasets: [
                        {
                            backgroundColor: '#00349F',
                            data: this.records
                        }
                    ]
                },
                chartOptions: {
                    responsive: true,
                    plugins: {
                        legend: {
                            display: false
                        },
                    },
                    scales: {
                        x: {
                            display: true,
                            title: {
                                display: true,
                                text: "Win Total",
                            },
                        },
                        y: {
                            display: true,
                            title: {
                                display: true,
                                text: "Singleplayer Games",
                            },
                        },
                    }
                }
            }
        }
    }
</script>

<style lang="scss" scoped>
    .holder {
        border-radius: 13px;
        width: 410px;
    }
</style>