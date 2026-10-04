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

const registerData = reactive({
  name: '',
  email: '',
  password: '',
  birthdate: '',
})

const handleSubmit = async () => {
  console.log('Datos enviados', registerData)

  try {
    const result = await authService.register(registerData)

    console.log('Response', result)
  } catch (error) {
    console.error(error)
  }
}
</script>

<template>
  <div class="grid grid-cols-1 lg:grid-cols-2 min-h-screen">
    <!-- Left Column: Register Form (Mobile & Desktop) -->
    <div class="flex flex-col p-6 gap-5 lg:p-12 lg:justify-center lg:max-w-md lg:mx-auto lg:w-full">
      <div>
        <h1 class="text-2xl text-orange-600 font-bold">Shorty Link</h1>
      </div>

      <div class="flex flex-col gap-10 pt-5">
        <div>
          <h2 class="text-2xl font-bold">Create your account</h2>
          <p>
            Already have an account?
            <RouterLink to="/login" class="text-blue-700 underline">Log in</RouterLink>
          </p>
        </div>

        <form @submit.prevent="handleSubmit" class="flex flex-col gap-4">
          <div class="flex flex-col gap-4">
            <FormInput
              v-model.trim="registerData.name"
              label="Name"
              type="text"
              id="name_register"
            />

            <FormInput
              v-model.trim="registerData.email"
              label="Email"
              type="email"
              id="email_register"
            />

            <FormInput
              v-model.trim="registerData.password"
              label="Password"
              type="password"
              id="password_register"
            />

            <div>
              <label for="birthdate_register" class="block text-sm font-medium text-gray-700 mb-1">
                Date of Birth
              </label>
              <input
                v-model="registerData.birthdate"
                type="date"
                id="birthdate_register"
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
              <p class="text-xs text-gray-500 mt-1">
                You must be at least 14 years old to register
              </p>
            </div>
          </div>

          <div class="flex justify-center pt-10">
            <AuthButton text="Sign up" />
          </div>
        </form>
      </div>
      <!-- TODO: implement OAuth -->
      <!-- <div class="flex items-center gap-3 pt-5">
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
      </div> -->
    </div>

    <!-- Right Column: Image/Background (Desktop Only) -->
    <div
      class="hidden lg:flex items-center justify-center bg-gradient-to-br from-olive-100 to-olive-200 p-8"
    >
      <div class="text-center">
        <h2 class="text-3xl font-bold text-gray-800 mb-4">Join Us Today</h2>
        <p class="text-gray-600 text-lg max-w-sm">
          Create short, memorable links and share them with anyone, anywhere.
        </p>
      </div>
    </div>
  </div>
</template>
