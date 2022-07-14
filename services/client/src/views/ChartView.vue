<template>
  <div class="app">
    <apexcharts width="550" type="bar" :options="chartOptions" :series="series"></apexcharts>
  </div>
</template>

<script lang="ts">
import VueApexCharts from 'vue3-apexcharts'

export default {
  name: 'Chart',
  components: {
    apexcharts: VueApexCharts,
  },
  data: function () {
    return {
      chartOptions: {
        chart: {
          type: 'bar',
          id: 'vuechart-example',
          events: {
            click: function(event: any) {
              console.log(event.target)
            }
          }
        },
        xaxis: {
          categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998],
        },
      },
      series: [{
        name: 'series-1',
        data: [30, 40, 45, 50, 49, 60, 70, 81]
      }]
    }
  }
}
</script>
<style scoped>
button {
  background: #26E6A4;
  border: 0;
  font-size: 16px;
  color: '#fff';
  padding: 10px;
  margin-left: 28px;
}
</style>

