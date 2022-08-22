<template>
  <label v-if="chart">{{ chart.name }}</label>
  <apexchart
    v-if="options"
    :options="options"
    :series="chart.generateSerie()"
    @dataPointSelection="dataPointSelection"
    :key="chart.id"
    width=100%
    height=100%
  >
  </apexchart>
</template>

<script lang="ts">
import type { changeData, Chart, DataChart } from "@/generated";
import { defineComponent } from "vue";
import VueApexCharts from "vue3-apexcharts";

export default defineComponent({
  emits: ["hideData"],
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
          animations: {
            dynamicAnimation: {
              speed: 550, //уменьшу скорость анимации 350 => 550
            },
          },
        },
        labels: this.chart.generateCategories(),
        legend: {
          fontSize: '16px',
          labels: {
            colors: [document.documentElement.style.getPropertyValue('--color-text')]
          },
          onItemClick: {
            toggleDataSeries: true, //эта штука вкрубает нажатие на легенду
          },
        },
        noData: {
          text: "Loading...",
          align: "center",
          verticalAlign: "middle",
          offsetX: 0,
          offsetY: 0,
          style: {
            color: '#929292',
            fontSize: "14px",
            fontFamily: undefined,
          },
        },
      },
    };
  },
  methods: {
    dataPointSelection(event: any, chartContext: any, config: any) {
      // console.log("dataPointSelection", config.dataPointIndex);
      const dataPoint: changeData = {
        id_chart: this.chart.id,
        changeSerieIndex: config.dataPointIndex,
      };
      this.$emit("hideData", dataPoint);
    },
  },
});
</script>
