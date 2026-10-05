<script setup lang="ts">
interface Props {
  text: string
  iconPath?: string
}
defineProps<Props>()
</script>

<template>
  <button
    type="button"
    class="flex w-full justify-center items-center gap-2 rounded-sm border border-gray-300 py-2 font-medium cursor-pointer hover:bg-gray-100 transition-all duration-200"
  >
    <img :src="iconPath" alt="Svg icon" class="h-5 w-5" />
    {{ text }}
  </button>
</template>
