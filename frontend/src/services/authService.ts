import { api } from './api'
import type {
  AuthCredentials,
  RegisterSchema,
  AuthResponse,
  RefreshTokenRequest,
  LogoutAllRequest,
} from '@/types/auth'

export const authService = {
  async register(credentials: RegisterSchema) {
    const response = await api.post<AuthResponse>('auth/register', credentials)

    localStorage.setItem('access_token', response.access_token)
    localStorage.setItem('refresh_token', response.refresh_token)

    return response
  },

  async login(credentials: AuthCredentials) {
    const response = await api.post<AuthResponse>('auth/login', credentials)

    localStorage.setItem('access_token', response.access_token)
    localStorage.setItem('refresh_token', response.refresh_token)

    return response
  },

  async refresh(refreshToken: string) {
    const response = await api.post<AuthResponse>('auth/refresh', {
      refresh_token: refreshToken,
    } satisfies RefreshTokenRequest)

    localStorage.setItem('access_token', response.access_token)
    localStorage.setItem('refresh_token', response.refresh_token)

    return response
  },

  async logout(refreshToken: string | null) {
    try {
      if (refreshToken) {
        return await api.post<void>('auth/logout', {
          refresh_token: refreshToken,
        } satisfies RefreshTokenRequest)
      }
    } finally {
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
    }
  },

  logoutAll(userId: number) {
    return api.post<void>('auth/logout_all', {
      user_id: userId,
    } satisfies LogoutAllRequest)
  },
}
