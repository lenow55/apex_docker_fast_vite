<template>
  <apexchart
    v-if="options"
    :options="options"
    :series="chart.generateSerie()"
    @dataPointSelection="dataPointSelection"
  >
  </apexchart>
</template>

<script lang="ts">
import type { Chart } from "@/generated";
import { defineComponent } from "vue";
import VueApexCharts from "vue3-apexcharts";

// type GenerateData = {
//   serie: number[];
//   categories: string[];
//   ids: number[];
// };

export default defineComponent({
  name: "Chart",
  components: {
    apexchart: VueApexCharts,
  },
  props: {
    chart: {
      type: Object as () => Chart,
      required: true,
    },
  },
  data() {
    return {
      options: {
        chart: {
          type: "donut",
          id: this.chart.id,
        },
        labels: this.chart.generateCategories(),
      },
    };
  },
  setup() {
  },
  // created() {
  //   this.generateDiagram();
  // },
  methods: {
    // generateDiagram() {
    //   console.log(this.chart.generateSerie())
    // },
    // click(event: any, chartContext: any, config: any) {
    //   console.log("click", event, chartContext, config);
    // },
    // legendClick(chartContext: any, seriesIndex: any, config: any) {
    //   console.log("legendClick", chartContext, seriesIndex, config);
    // },
    // markerClick(
    //   event: any,
    //   chartContext: any,
    //   { seriesIndex, dataPointIndex, config }: any
    // ) {
    //   console.log(
    //     "markerClick",
    //     event,
    //     chartContext,
    //     seriesIndex,
    //     dataPointIndex,
    //     config
    //   );
    // },
    // selection(chartContext: any, { xaxis, yaxis }: any) {
    //   console.log("selection", chartContext, xaxis, yaxis);
    // },
    dataPointSelection(event: any, chartContext: any, config: any) {
      console.log("dataPointSelection", event, chartContext, config);
    },
  },
});
</script>
