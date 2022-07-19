<script lang="ts">
import { defineComponent, ref, defineProps } from "vue";
import VueApexCharts from "vue3-apexcharts";
import type { ApexOptions } from "apexcharts";
import { ChartGroup } from "@/generated";
import Chart from "@/components/ChartComponent.vue";
import axios from "axios";
import type { Rule4Chart } from "@/generated";

type AppState = {
  loading: boolean;
  chartsGroup: ChartGroup;
  chartRules: Rule4Chart[];
  error: unknown;
};

export default defineComponent({
  name: "Diagrams",
  components: {
    apexchart: VueApexCharts,
    chart: Chart,
  },

  setup() {
    // const options = ref<ApexOptions>({
    //   chart: {
    //     type: "donut",
    //     id: "vuechart-example",
    //   },
    // });
    // const series = ref([30, 40, 45, 50, 49, 60, 70, 81]);

    const app_state = ref<AppState>({
      loading: true,
      chartsGroup: new ChartGroup(),
      chartRules: [
        {
          id_diagram: 0,
          include_fields_id: [0],
        },
      ],
      error: undefined,
    });

    // function click(event: any, chartContext: any, config: any) {
    //   console.log("click", event, chartContext, config);
    // }
    // function legendClick(chartContext: any, seriesIndex: any, config: any) {
    //   console.log("legendClick", chartContext, seriesIndex, config);
    // }
    // function markerClick(
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
    // }
    // function selection(chartContext: any, { xaxis, yaxis }: any) {
    //   console.log("selection", chartContext, xaxis, yaxis);
    // }
    // function dataPointSelection(event: any, chartContext: any, config: any) {
    //   console.log("dataPointSelection", event, chartContext, config);
    // }

    async function load() {
      try {
        const chartsResp = await axios.post("/diagrams");
        console.log(chartsResp.data);
        app_state.value.chartsGroup = new ChartGroup(chartsResp.data);
      } catch (err: any) {
        console.log(err);
      } finally {
        app_state.value.loading = false;
      }
      console.log(app_state.value.chartsGroup.charts);
    }

    async function filter() {
      try {
        const chartsResp = await axios.post(
          "/diagrams",
          app_state.value.chartRules
        );
        console.log(chartsResp.data);
        app_state.value.chartsGroup = new ChartGroup(chartsResp.data);
      } catch (err: any) {
        console.log(err);
      } finally {
        app_state.value.loading = false;
      }
      console.log(app_state.value.chartsGroup.charts);
    }

    return {
      app_state,
      load,
      filter,
      // options,
      // series,
      // click,
      // legendClick,
      // markerClick,
      // selection,
      // dataPointSelection,
    };
  },
  created() {
    this.load();
    setTimeout(() => {
      this.filter();
    }, 3000);
  },
});
</script>

<template>
  <div class="chart-group">
    <h2>{{ app_state.chartsGroup.name }}</h2>
    <p v-html="app_state.chartsGroup.description"></p>

    <div
      v-for="c in app_state.chartsGroup.charts"
      :key="c.id"
      class="chart-wrapper"
    >
      <chart :chart="c" />
    </div>
  </div>
</template>

<style>
#app {
  display: flex;
  flex-direction: column;
}

.chart-wrapper {
  display: block;
  width: 100%;
  float: left;
  transition: width 0.2s;
  margin: 10px;
}

@media only screen and (min-width: 600px) {
  .chart-wrapper {
    width: 50%;
  }
}

@media (min-width: 1024px) {
  .chart-wrapper {
    width: 31%;
  }
}
</style>
