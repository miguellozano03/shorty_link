<script setup lang="ts">
import { ref } from 'vue'
const emit = defineEmits(['login'])
const movies: string[] = ['The Predator', 'Kickboxer', 'Scream', 'Terminator 2']

const userName = ref('Miguel')

const login = () => {
  emit('login', userName.value)
}

const myValue = ref('Some value')
</script>
<template>
  <h1>Learning vueee</h1>
  <p>I'm making a side project, and I dunno view, this page is my sandbox :3</p>

  <div>
    <ul>
      <li v-for="movie in movies" v-bind:key="movie">
        {{ movie }}
      </li>
    </ul>
  </div>

  <div>
    <input type="text" v-model="myValue" class="border border-gray-500 rounded-sm" />
    <p>{{ myValue }}</p>
  </div>


  <div>
    <h2>This is a child component...</h2>
    <p>Username: {{ userName }}</p>

    <button @click="login">Login</button>

  </div>
</template>
