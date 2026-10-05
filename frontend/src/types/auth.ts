export interface AuthCredentials {
  email: string;
  password: string;
}

export interface RegisterSchema {
  name: string;
  email: string;
  password: string;
  birthdate: string;
}

export interface RefreshTokenRequest {
  refresh_token: string;
}

export interface LogoutAllRequest {
  user_id: number;
}

export interface AuthResponse {
  access_token: string;
  refresh_token: string;
  token_type?: string;
}