<template>
  <input type="checkbox" v-model="theModel"
    class="field" />
  <label v-if="label">{{ label }}</label>
</template>


<script lang="ts">
import { defineComponent, computed } from 'vue'
import type { PropType } from 'vue'

type Booleanish = boolean | 'true' | 'false'


export default defineComponent({
  emits: ['change:modelValue'],
  props: {
    modelValue: {
      type: Object as PropType<Booleanish>, // Type Annotation
      default: () => ({}),
    },
    label: {
      type: String,
      default: ''
    },
  },
  setup(props, { emit }) {
    const theModel = computed({
      get: () => props.modelValue,
      set: (value) => emit('change:modelValue', value),
    });
    return { theModel };
  }
})
</script>
