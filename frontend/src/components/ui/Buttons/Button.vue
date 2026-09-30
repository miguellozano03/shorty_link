<script setup lang="ts">
interface Props {
  text: string
}
defineProps<Props>()
</script>

<template>
  <button type="button" class="rounded-sm border bg-blue-700 text-white px-4 py-2 font-bold cursor-pointer">
    {{ text }}
  </button>
</template>