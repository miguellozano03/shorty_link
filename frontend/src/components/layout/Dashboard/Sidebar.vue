<script setup lang="ts">
import NavItem from '@/components/ui/Navbar/NavItem.vue'
import { House, Link, ChartColumn, Settings, CreditCard } from '@lucide/vue'
import type { Component } from 'vue'

interface NavLink {
  link: string
  text: string
  icon: Component
}

const mainNavItems: NavLink[] = [
  { link: '/', text: 'Home', icon: House },
  { link: '/links', text: 'Links', icon: Link },
  { link: '/analytics', text: 'Analytics', icon: ChartColumn },
]

const bottonNavItems: NavLink[] = [
  { link: '/subscriptions', text: 'Subscriptions', icon: CreditCard },
  { link: '/settings', text: 'Configuration', icon: Settings },
]
</script>
<template>
  <aside class="flex flex-col h-screen w-3xs gap-5">
    <div class="flex py-4 px-2 items-center">
      <p class="text-xl font-bold">Shorty Link</p>
    </div>

    <div class="flex flex-col gap-4 w-full">
      <nav class="flex flex-col gap-1 px-2">
        <NavItem
          v-for="item in mainNavItems"
          :key="item.text"
          :link="item.link"
          :text="item.text"
          :icon="item.icon"
        />
      </nav>

      <div class="w-11/12 self-center border-b-2 border-zinc-200"></div>

      <div class="px-2">
        <NavItem
          v-for="item in bottonNavItems"
          :key="item.text"
          :link="item.link"
          :text="item.text"
          :icon="item.icon"
        />
      </div>
    </div>
  </aside>
</template>
