<script lang="ts">
import { defineComponent, ref } from 'vue'
import VueApexCharts from 'vue3-apexcharts'
import type { ApexOptions } from 'apexcharts'



export default defineComponent({
  components: {
    apexchart: VueApexCharts,
  },
  setup() {
    const options = ref<ApexOptions>({
      chart: {
        type: 'donut',
        id: 'vuechart-example',
        events: {
          markerClick: function(event: any, ...rest): void {
            console.log("event")
          }
        }
      },
    })
    const series = ref([30, 40, 45, 50, 49, 60, 70, 81])

    return {
      options,
      series,
    }
  }
})



</script>

<template>
  <div>
    <apexchart :options="options" :series="series" @markerClick="options.chart.events.markerClick">
    </apexchart>
  </div>
</template>
