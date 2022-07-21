<script lang="ts">
import { defineComponent } from "vue";
import BaseCheckboxVue from "@/components/form-components/BaseCheckbox.vue";
import BaseInputVue from "@/components/form-components/BaseInput.vue";

export default defineComponent({
  components: {
    baseinput: BaseInputVue,
    basecheckbox: BaseCheckboxVue,
  },
  data() {
    return {
      data: {
        id: 0,
        description: '',
        str: ''
      },
    };
  },
  methods: {
    sendForm() {
      console.log("sendForm");
    },
  },
});
</script>

<template>
  <form @submit.prevent="sendForm">
    <baseinput
      v-model="data"
      label="Title"
      type="password"
      error="This input has an error!"
    />
  </form>
</template>
