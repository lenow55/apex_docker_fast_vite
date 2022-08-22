<script lang="ts">
import { defineComponent, ref, defineProps } from "vue";
import VueApexCharts from "vue3-apexcharts";
import type { ApexOptions } from "apexcharts";
import { ChartGroup, type changeData } from "@/generated";
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
    const app_state = ref<AppState>({
      loading: true,
      chartsGroup: new ChartGroup(),
      chartRules: [],
      error: undefined,
    });

    async function load() {
      try {
        const chartsResp = await axios.post("/diagrams");
        // console.log(chartsResp.data);
        app_state.value.chartsGroup = new ChartGroup(chartsResp.data);
      } catch (err: any) {
        console.log(err);
      } finally {
        app_state.value.loading = false;
      }
      // console.log(app_state.value.chartsGroup.charts);
    }

    async function filter() {
      app_state.value.loading = true;
      try {
        const chartsResp = await axios.post(
          "/diagrams",
          app_state.value.chartRules
        );
        app_state.value.chartsGroup.updateCharts(chartsResp.data);
      } catch (err: any) {
        console.log(err);
      } finally {
        app_state.value.loading = false;
      }
    }

    function hideRefreshData(data: changeData) {
      app_state.value.chartsGroup.changeVisible(
        data.id_chart,
        data.changeSerieIndex
      );
      app_state.value.chartRules = app_state.value.chartsGroup.get_rules();
      filter();
    }

    return {
      app_state,
      load,
      filter,
      hideRefreshData,
    };
  },
  created() {
    this.load();
  },
});
</script>

<template>
  <div class="chart-group" v-if="app_state.chartsGroup.charts">
    <h2>{{ app_state.chartsGroup.name }}</h2>
    <p v-html="app_state.chartsGroup.description"></p>
    <div class="chart-container">
      <div
        v-for="c in app_state.chartsGroup.charts"
        :key="c.id"
        class="chart-wrapper"
      >
        <chart :chart="c" @hideData="hideRefreshData" />
      </div>
    </div>
  </div>
  <div v-else class="loader">
    <div class="inner one"></div>
    <div class="inner two"></div>
    <div class="inner three"></div>
  </div>
</template>

<style>
.loader {
  left: calc(50% - 32px);
  width: 64px;
  height: 64px;
  border-radius: 50%;
  perspective: 800px;
}

.inner {
  position: absolute;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  border-radius: 50%;
}

.inner.one {
  left: 0%;
  top: 0%;
  animation: rotate-one 1s linear infinite;
  border-bottom: 3px solid #efeffa;
}

.inner.two {
  right: 0%;
  top: 0%;
  animation: rotate-two 1s linear infinite;
  border-right: 3px solid #efeffa;
}

.inner.three {
  right: 0%;
  bottom: 0%;
  animation: rotate-three 1s linear infinite;
  border-top: 3px solid #efeffa;
}
/* 
@keyframes rotate-one {
  0% {
    transform: rotateX(35deg) rotateY(-45deg) rotateZ(0deg);
  }
  100% {
    transform: rotateX(35deg) rotateY(-45deg) rotateZ(360deg);
  }
}

@keyframes rotate-two {
  0% {
    transform: rotateX(50deg) rotateY(10deg) rotateZ(0deg);
  }
  100% {
    transform: rotateX(50deg) rotateY(10deg) rotateZ(360deg);
  }
}

@keyframes rotate-three {
  0% {
    transform: rotateX(35deg) rotateY(55deg) rotateZ(0deg);
  }
  100% {
    transform: rotateX(35deg) rotateY(55deg) rotateZ(360deg);
  }
} */

.chart-container {
  display: grid;
  gap: 20px;

  /* ! */
  grid-template-columns: 800px;
  grid-template-rows: repeat(3, 800px);
}

@media (min-width: 1224px) {
  .chart-container {
    display: grid;
    gap: 20px;

    /* ! */
    grid-template-columns: 700px 400px;
    grid-template-rows: 700px 700px;
  }
}

@media (min-width: 1920px) {
  .chart-container {
    display: grid;
    gap: 20px;

    /* ! */
    grid-template-columns: 500px 500px 800px;
    grid-template-rows: repeat(1, 500px);
  }
}
</style>
