import os

def frontend_urls(request):
    """Context processor to provide frontend URLs to templates"""
    return {
        'FRONTEND_LOGIN_URL': os.environ.get('FRONTEND_LOGIN_URL', 'http://localhost:5173/login'),
        'FRONTEND_REGISTER_URL': os.environ.get('FRONTEND_REGISTER_URL', 'http://localhost:5173/register'),
    }
