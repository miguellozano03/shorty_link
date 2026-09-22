const API_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000/api/v1/";

type RequestOptions = RequestInit & {
  token?: string;
};

async function request<T>(
  endpoint: string,
  options: RequestOptions = {},
): Promise<T> {
  const { token, headers, ...requestOptions } = options;

  const response = await fetch(`${API_URL}${endpoint}`, {
    ...requestOptions,
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...headers,
    },
  });

  const contentType = response.headers.get("content-type");
  const data = contentType?.includes("application/json")
    ? await response.json()
    : await response.text();

  if (!response.ok) {
    const message =
      typeof data === "object" && data !== null && "message" in data
        ? String(data.message)
        : "Error en la petición";

    throw new Error(message);
  }

  return data as T;
}

export const api = {
  get<T>(endpoint: string, options?: RequestOptions) {
    return request<T>(endpoint, {
      ...options,
      method: "GET",
    });
  },

  post<T>(endpoint: string, body?: unknown, options?: RequestOptions) {
    return request<T>(endpoint, {
      ...options,
      method: "POST",
      body: body !== undefined ? JSON.stringify(body) : undefined,
    });
  },

  put<T>(endpoint: string, body?: unknown, options?: RequestOptions) {
    return request<T>(endpoint, {
      ...options,
      method: "PUT",
      body: body !== undefined ? JSON.stringify(body) : undefined,
    });
  },

  delete<T>(endpoint: string, options?: RequestOptions) {
    return request<T>(endpoint, {
      ...options,
      method: "DELETE",
    });
  },
};