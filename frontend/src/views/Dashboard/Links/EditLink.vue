<script setup lang="ts">
import { onMounted, reactive } from 'vue'
import { useRoute } from 'vue-router'
import FormInput from '@/components/ui/Inputs/FormInput.vue'
import Button from '@/components/ui/Buttons/Button.vue'

import { shortenerService } from '@/services/shortenerService'
import router from '@/router'

const route = useRoute()
const code = String(route.params.code)

const editLinkData = reactive({
  long_url: '',
  title: '',
})

onMounted(async () => {
  try {
    const links = await shortenerService.get()
    const link = links.find((item) => item.code === code)

    if (!link) {
      router.push({ name: 'links' })
      return
    }

    editLinkData.long_url = link.long_url
    editLinkData.title = link.title
  } catch (error) {
    alert("We couldn't load this link")
    router.push({ name: 'links' })
  }
})

const handleSubmit = async () => {
  try {
    await shortenerService.edit(code, {
      title: editLinkData.title,
      long_url: editLinkData.long_url,
    })

    router.push({ name: 'links' })
  } catch (error) {
    alert("We couldn't update the link")
  }
}
</script>
<template>
  <div class="flex h-screen w-full flex-col bg-slate-50 py-12 px-64 gap-6">
    <header class="flex flex-col gap-8">
      <div>
        <h1 class="text-2xl font-bold text-slate-900">Edit short link</h1>
        <p class="mt-2 text-slate-600">Update the destination or title of your link.</p>
      </div>
    </header>
    <form
      @submit.prevent="handleSubmit"
      class="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm sm:p-8"
    >
      <div class="mb-7">
        <h2 class="text-lg font-semibold text-slate-900">Link details</h2>
        <p class="mt-1 text-sm text-slate-500">
          Change the destination URL or memorable title.
        </p>
      </div>
      <div class="flex flex-col gap-5">
        <FormInput
          v-model.trim="editLinkData.long_url"
          type="url"
          label="Destination URL"
          id="destination-url"
        />
        <FormInput
          v-model.trim="editLinkData.title"
          type="text"
          label="Title (optional)"
          id="title"
        />
      </div>
      <div class="mt-8 flex justify-between border-t border-slate-100 pt-6">
        <RouterLink to="/links">
          <button
            type="button"
            class="rounded-sm border border-gray-400 hover:bg-slate-50 text-slate-800 px-4 py-2 font-bold cursor-pointer"
          >
            Cancel
          </button>
        </RouterLink>
        <Button type="submit" text="Save changes" />
      </div>
    </form>
  </div>
</template>
