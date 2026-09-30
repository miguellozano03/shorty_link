<script setup lang="ts">
import { Sidebar } from '@/components/layout/Dashboard'
</script>
<template>
  <div class="flex min-h-screen w-full">
    <Sidebar />

    <main class="flex-1">
      <RouterView />
    </main>
  </div>
</template>
