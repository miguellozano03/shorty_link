import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '@/views/DashboardView.vue'
import { LoginView, RegisterView } from '@/views/Auth'

const routes = [
  { path: '/', component: DashboardView },
  { path: '/login', component: LoginView, name: 'Login', meta: { title: 'Welcome back!' } },
  { path: '/register', component: RegisterView, name: 'Register', meta: { title: 'Create a new account' } },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

const defaultTitle = 'Shorty Link'

router.beforeEach((to, _from, next) => {
  document.title = (to.meta.title as string) || defaultTitle
  next()
})

export default router
