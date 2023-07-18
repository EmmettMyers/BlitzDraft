<template>
    <div class="bg-white holder">
        <Bar
            id="my-chart-id"
            :options="chartOptions"
            :data="data"
            class="chart p-2"
            style="height: 200px; width: 295px"
        />
    </div>
</template>

<script lang="ts">
    import { Bar } from 'vue-chartjs'
    import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

    ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

    export default {
        name: 'BarChart',
        props: ['values'],
        components: { Bar },
        data() {
            return {
                data: {
                    labels: ['QB', 'RB', 'WR1', 'WR2', 'WR3', 'TE', 'OL', 'DEF'],
                    datasets: [
                        {
                            backgroundColor: '#B50000',
                            data: this.values
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
                                text: "Player Position",
                            },
                        },
                        y: {
                            display: true,
                            title: {
                                display: true,
                                text: "Avg. Draft Position",
                            },
                            max: 8,
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
        width: 295px;
        height: 188px;
    }
</style>