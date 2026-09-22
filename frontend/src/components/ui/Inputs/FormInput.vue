<script setup lang="ts">
interface Props {
  label: string
  type: string
  id: string
}
defineProps<Props>()

const model = defineModel<string>()
</script>

<template>
  <div class="flex flex-col min-h-20">
    <label :for="id">{{ label }}</label>
    <input
      v-model="model"
      :type="type"
      :id="id"
      class="border rounded-sm border-gray-400 py-2 px-2"
    />
  </div>
</template>
