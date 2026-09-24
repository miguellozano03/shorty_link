<script setup lang="ts">
import type { Component } from 'vue'
import { useRoute } from 'vue-router'

interface Props {
  text: string
  link: string
  icon?: Component
}
defineProps<Props>()

const route = useRoute()
</script>

<template>
  <RouterLink
    :to="link"
    exact-active-class="bg-indigo-50 text-indigo-800"
    class="relative flex justify-start items-center gap-2 text-sm font-bold w-full py-2 pl-3 pr-2 text-gray-900 hover:bg-gray-100"
  >
    <component :is="icon" v-if="icon" class="w-5 h-5 shrink-0" />

    <span v-if="route.path === link" class="absolute left-0 h-5 w-1 rounded-r-sm bg-indigo-800" />

    <span>{{ text }}</span>
  </RouterLink>
</template>
