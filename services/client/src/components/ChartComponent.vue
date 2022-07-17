<template>
  <apexchart
    v-if="options && series"
    type="line"
    height="350"
    :options="options"
    :series="series"
    @click="click"
    @legendClick="legendClick"
    @markerClick="markerClick"
    @selection="selection"
    @dataPointSelection="dataPointSelection"
  >
  </apexchart>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import VueApexCharts from "vue3-apexcharts";

export default defineComponent({
  components: {
    apexchart: VueApexCharts,
  },
  data() {
    return {
      options: {
        chart: {
          id: "vuechart-example",
        },
        xaxis: {
          categories: [1991, 1992, 1993],
        },
      },
      series: [
        {
          name: "series-1",
          data: [30, 40, 45],
        },
      ],
    };
  },
  methods: {
    click(event: any, chartContext: any, config: any) {
      console.log("click", event, chartContext, config);
    },
    legendClick(chartContext: any, seriesIndex: any, config: any) {
      console.log("legendClick", chartContext, seriesIndex, config);
    },
    markerClick(
      event: any,
      chartContext: any,
      { seriesIndex, dataPointIndex, config }: any
    ) {
      console.log(
        "markerClick",
        event,
        chartContext,
        seriesIndex,
        dataPointIndex,
        config
      );
    },
    selection(chartContext: any, { xaxis, yaxis }: any) {
      console.log("selection", chartContext, xaxis, yaxis);
    },
    dataPointSelection(event: any, chartContext: any, config: any) {
      console.log("dataPointSelection", event, chartContext, config);
    },
  },
});
</script>
