<script setup lang="ts">
import { reactive } from 'vue'
import { AuthButton, SocialLoginButton } from '@/components/ui/Buttons'
import { FormInput } from '@/components/ui/Inputs'
import { GoogleIcon, GithubIcon, DiscordIcon } from '@/assets/icons'

import { authService } from '@/services/authService'

interface socialItem {
  name: string
  icon: string
}

const socialNetworks: socialItem[] = [
  {
    name: 'Google',
    icon: GoogleIcon,
  },
  {
    name: 'Github',
    icon: GithubIcon,
  },
  {
    name: 'Discord',
    icon: DiscordIcon,
  },
]

const loginData = reactive({
  email: '',
  password: '',
})

const handleSubmit = async () => {
  console.log('Datos enviados', loginData)

  try {
    const result = await authService.login(loginData)

    console.log('Respuesta:', result)
  } catch (error) {
    console.error('Error:', error)
  }
}
</script>

<template>
  <div class="grid grid-cols-1 lg:grid-cols-2 min-h-screen">
    <!-- Left Column: Login Form (Mobile & Desktop) -->
    <div class="flex flex-col p-6 gap-5 lg:p-12 lg:justify-center lg:max-w-md lg:mx-auto lg:w-full">
      <div>
        <h1 class="text-2xl text-orange-600 font-bold">Shorty Link</h1>
      </div>

      <div class="flex flex-col gap-10 pt-5">
        <div>
          <h2 class="text-2xl font-bold">Log in and start sharing</h2>
          <p>
            Don't you have an account?
            <RouterLink to="/register" class="text-blue-700 underline">Sign up</RouterLink>
          </p>
        </div>

        <form @submit.prevent="handleSubmit" class="flex flex-col gap-2">
          <FormInput v-model.trim="loginData.email" label="Email" type="email" id="email_login" />

          <FormInput
            v-model.trim="loginData.password"
            label="Password"
            type="password"
            id="password_login"
          />

          <div class="flex justify-end pt-2">
            <p class="text-blue-700 underline">Forgot your password?</p>
          </div>
          <div class="flex justify-center pt-10">
            <AuthButton text="Log in" />
          </div>
        </form>
      </div>
      <div class="flex items-center gap-3 pt-5">
        <div class="h-px flex-1 bg-gray-300"></div>
        <span class="text-sm text-gray-500">OR</span>
        <div class="h-px flex-1 bg-gray-300"></div>
      </div>

      <div class="flex flex-col gap-3 pt-5">
        <SocialLoginButton
          v-for="social in socialNetworks"
          :key="social.name"
          :text="`Continue with ${social.name}`"
          :icon-path="social.icon"
        />
      </div>
    </div>

    <!-- Right Column: Image/Background (Desktop Only) -->
    <div
      class="hidden lg:flex items-center justify-center bg-gradient-to-br from-olive-100 to-olive-200 p-8"
    >
      <div class="text-center">
        <h2 class="text-3xl font-bold text-gray-800 mb-4">Share Links Easily</h2>
        <p class="text-gray-600 text-lg max-w-sm">
          Create short, memorable links and share them with anyone, anywhere.
        </p>
      </div>
    </div>
  </div>
</template>
