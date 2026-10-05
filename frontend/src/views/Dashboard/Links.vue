<script setup lang="ts">
import { onMounted, ref } from 'vue'
import Link from '@/components/ui/Utils/Link.vue'
import Button from '@/components/ui/Buttons/Button.vue'
import { shortenerService } from '@/services/shortenerService'
import type { Url } from '@/types/shortener'

const links = ref<Url[]>([])

const handleDeleted = (code: string) => {
  links.value = links.value.filter((link) => link.code !== code)
}

onMounted(async () => {
  links.value = await shortenerService.get()
})
</script>
<template>
  <div class="flex h-screen w-full flex-col overflow-hidden bg-slate-50 py-12 pl-20 pr-24">
    <header class="flex flex-col gap-8">
      <div class="flex items-center justify-between">
        <h1 class="text-2xl font-bold text-slate-900">Shorty Links</h1>
        <RouterLink to="links/new">
          <Button text="New link" class="!w-auto shrink-0" />
        </RouterLink>
      </div>
      <div class="border border-slate-200"></div>
    </header>

    <div
      class="min-h-0 flex-1 overflow-y-auto pt-12 pr-2 scrollbar-none [&::-webkit-scrollbar]:hidden"
    >
      <div class="grid grid-cols-1 gap-4 pb-4">
        <Link
          v-for="link in links"
          :key="link.id"
          :title="link.title"
          :long-url="link.long_url"
          :short-url="link.short_url"
          :code="link.code"
          :created-at="new Date(link.created_at).toLocaleDateString()"
          @deleted="handleDeleted"
        />
      </div>
    </div>
  </div>
</template>
