<script lang="ts">
import { defineComponent } from 'vue'
import BaseCheckboxVue from '@/components/form-components/BaseCheckbox.vue'
import BaseInputVue from '@/components/form-components/BaseInput.vue'

export default defineComponent({
  components: {
    baseinput: BaseInputVue,
    basecheckbox: BaseCheckboxVue,
  },
  methods: {
    sendForm() {
      console.log("sendForm");
    }
  }
})
</script>

<template>
  <form @submit.prevent="sendForm"></form>
</template>