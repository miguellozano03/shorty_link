<script setup lang="ts">
interface Props {
  text: string
}
defineProps<Props>()
</script>

<template>
  <button type="submit" class="w-full rounded-sm border bg-blue-700 text-white py-2 font-bold cursor-pointer">
    {{ text }}
  </button>
</template>