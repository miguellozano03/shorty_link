<script setup lang="ts">
import { shortenerService } from '@/services/shortenerService'
import { Pencil, Share2, X, CalendarDays } from '@lucide/vue'
interface Props {
  title: string
  shortUrl: string
  longUrl: string
  code: string
  createdAt: string
}
const props = defineProps<Props>()

const emit = defineEmits<{
  deleted: [code: string]
}>()

const handleDelete = async () => {
  let response = window.confirm('Do you want to remove this link')
  if (!response) {
    return
  }
  await shortenerService.delete(props.code)
  emit('deleted', props.code)
}
</script>

<template>
  <article class="overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm">
    <div class="flex items-start justify-between gap-4 px-6 py-5">
      <div class="min-w-0">
        <h3 class="font-semibold text-slate-900">{{ title }}</h3>
        <a :href="shortUrl" class="mt-2 inline-block font-semibold text-blue-800 hover:underline">
          {{ shortUrl }}
        </a>
        <p class="mt-1 break-all text-sm text-slate-500">{{ longUrl }}</p>
      </div>

      <div class="flex shrink-0 items-center gap-1">
        <button
          @click="$router.push({ name: 'editLink', params: { code } })"
          type="button"
          aria-label="Editar link"
          class="rounded-md p-2 text-slate-500 hover:bg-slate-100 hover:text-blue-800"
        >
          <Pencil class="h-4 w-4 text-blue-800" />
        </button>
        <!-- <button
          type="button"
          aria-label="Compartir link"
          class="rounded-md p-2 text-slate-500 hover:bg-slate-100 hover:text-blue-800"
        >
          <Share2 class="h-4 w-4" />
        </button> -->
        <button
          @click="handleDelete"
          type="button"
          aria-label="Eliminar link"
          class="rounded-md p-2 text-slate-500 hover:bg-red-50 hover:text-red-600"
        >
          <X class="h-4 w-4 text-red-800" />
        </button>
      </div>
    </div>

    <footer
      class="flex flex-wrap items-center justify-between gap-3 border-t border-slate-100 bg-slate-50/70 px-6 py-3"
    >
      <button type="button" class="text-sm font-medium text-blue-800 hover:underline">
        Ver datos de clics
      </button>
      <p class="flex items-center gap-1.5 text-sm text-slate-500">
        <CalendarDays class="h-4 w-4 shrink-0" aria-hidden="true" />
        Creado el <time datetime="2026-09-26">{{ createdAt }}</time>
      </p>
    </footer>
  </article>
</template>
