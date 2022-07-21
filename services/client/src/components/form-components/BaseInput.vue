<template>
  <label v-if="label">{{ label }}</label>
  <input
    v-bind="$attrs"
    :placeholder="label"
    v-model="theModel.str"
    class="field"
  />
    <input
    v-bind="$attrs"
    :placeholder="label"
    v-model="theModel.id"
    class="field"
  />
    <input
    v-bind="$attrs"
    :placeholder="label"
    v-model="theModel.description"
    class="field"
  />
  <p>theModel.str</p>
</template>

<script lang="ts">
import { computed, defineComponent, type PropType } from "vue";

interface OurModelType {
  str: string;
  id: number;
  description: string
}

export default defineComponent({
  emits: ["update:modelValue"],
  props: {
    modelValue: {
      type: Object as PropType<OurModelType>, // Type Annotation
      default: () => ({}),
    },
    label: {
      type: String,
      default: "",
    },
  },
  setup(props, { emit }) {
    const theModel = computed({
      get: () => props.modelValue,
      set: (value) => emit("update:modelValue", value),
    });
    return { theModel };
  },
});
</script>
