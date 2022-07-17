<script lang="ts">
import { defineComponent, ref } from "vue";
import VueApexCharts from "vue3-apexcharts";
import type { ApexOptions } from "apexcharts";

export default defineComponent({
  components: {
    apexchart: VueApexCharts,
  },
  setup() {
    const options = ref<ApexOptions>({
      chart: {
        type: "donut",
        id: "vuechart-example",
      },
    });
    const series = ref([30, 40, 45, 50, 49, 60, 70, 81]);

    function click(event: any, chartContext: any, config: any) {
      console.log("click", event, chartContext, config);
    }
    function legendClick(chartContext: any, seriesIndex: any, config: any) {
      console.log("legendClick", chartContext, seriesIndex, config);
    }
    function markerClick(
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
    }
    function selection(chartContext: any, { xaxis, yaxis }: any) {
      console.log("selection", chartContext, xaxis, yaxis);
    }
    function dataPointSelection(event: any, chartContext: any, config: any) {
      console.log("dataPointSelection", event, chartContext, config);
    }

    return {
      options,
      series,
      click,
      legendClick,
      markerClick,
      selection,
      dataPointSelection,
    };
  },
});
</script>

<template>
  <div>
    <apexchart
      :options="options"
      :series="series"
      @click="click"
      @legendClick="legendClick"
      @markerClick="markerClick"
      @selection="selection"
      @dataPointSelection="dataPointSelection"
    >
    </apexchart>
  </div>
</template>
