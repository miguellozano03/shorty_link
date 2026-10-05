<script setup lang="ts">
import NavItem from '@/components/ui/Navbar/NavItem.vue'
import { House, Link, ChartColumn, Settings, CreditCard, LogOut } from '@lucide/vue'
import type { Component } from 'vue'
import { useRouter } from 'vue-router'
import { authService } from '@/services/authService'

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

const router = useRouter()

async function logout() {
  const refreshToken = localStorage.getItem('refresh_token')

  await authService.logout(refreshToken).catch(() => undefined)
  await router.push('/login')
}
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
        <button
          class="relative flex w-full items-center justify-start gap-2 py-2 pl-3 pr-2 text-left text-sm font-bold text-gray-900 hover:bg-gray-100"
          type="button"
          @click="logout"
        >
          <LogOut class="h-5 w-5 shrink-0" />
          <span>Logout</span>
        </button>
      </div>
    </div>
  </aside>
</template>
