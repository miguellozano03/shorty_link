import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import { Analytics, DashboardLayout, Home, Links, Settings, Subscriptions } from '@/views/Dashboard'
import { CreateLink, EditLink } from '@/views/Dashboard/Links'
import { LoginView, RegisterView } from '@/views/Auth'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: DashboardLayout,
    meta: { title: 'ShortyLink | Dashboard' },
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
    meta: { title: 'Welcome back!' },
  },
  {
    path: '/register',
    component: RegisterView,
    name: 'Register',
    meta: { title: 'Create a new account' },
  },
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
