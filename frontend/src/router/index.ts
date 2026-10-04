import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import { Analytics, DashboardLayout, Home, Links, Settings, Subscriptions } from '@/views/Dashboard'
import { CreateLink, EditLink } from '@/views/Dashboard/Links'
import { LoginView, RegisterView } from '@/views/Auth'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: DashboardLayout,
    meta: { title: 'ShortyLink | Dashboard', requiresAuth: true },
    children: [
      {
        path: '',
        name: 'home',
        component: Home,
      },
      {
        path: 'links',
        name: 'links',
        component: Links,

        meta: { title: 'ShortyLink | Links' },
      },
      {
        path: 'links/new',
        name: 'newLink',
        component: CreateLink,

        meta: { title: 'ShortyLink | Links' },
      },
      {
        path: 'links/:code/edit',
        name: 'editLink',
        component: EditLink,
        meta: { title: 'Edit link | ShortyLink' },
      },
      {
        path: 'analytics',
        name: 'analytics',
        component: Analytics,
      },
      {
        path: 'subscriptions',
        name: 'subscriptions',
        component: Subscriptions,
      },
      {
        path: 'settings',
        name: 'settings',
        component: Settings,
      },
    ],
  },
  {
    path: '/login',
    component: LoginView,
    name: 'Login',
    meta: { title: 'Welcome back!', guestOnly: true },
  },
  {
    path: '/register',
    component: RegisterView,
    name: 'Register',
    meta: { title: 'Create a new account', guestOnly: true },
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

const defaultTitle = 'Shorty Link'

router.beforeEach((to) => {
  document.title = (to.meta.title as string) || defaultTitle

  const token = localStorage.getItem('access_token')

  if (to.meta.requiresAuth && !token) {
    return '/login'
  }

  if (to.meta.guestOnly && token) {
    return '/'
  }
})

export default router
