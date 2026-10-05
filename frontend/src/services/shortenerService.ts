import { api } from './api'
import type { Url, UrlCreate, UrlUpdate } from '@/types/shortener'

export const shortenerService = {
  async get() {
    return await api.get<Url[]>('shortener/urls')
  },

  async create(data: UrlCreate) {
    return await api.post<Url>('shortener/urls', {
      title: data.title,
      long_url: data.long_url,
    })
  },

  async edit(code: string, data: UrlUpdate) {
    return await api.patch<Url>(`shortener/urls/${code}`, {
      title: data.title,
      long_url: data.long_url,
    })
  },

  async delete(code: string) {
    return await api.delete(`shortener/urls/${code}`)
  },
}
