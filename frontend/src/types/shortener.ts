export interface Url {
  id: number
  title: string
  long_url: string
  code: string
  short_url: string
  created_at: string
}

export interface UrlCreate {
  title: string
  long_url: string
}

export interface UrlUpdate {
  title?: string
  long_url?: string
}