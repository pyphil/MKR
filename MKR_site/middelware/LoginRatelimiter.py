# middlewares.py
from django.core.cache import cache
from django.shortcuts import redirect


class LoginRateLimiterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/accounts/login/':  # Adjust the login URL as per your project's setup
            ip_address = request.META.get('REMOTE_ADDR')
            cache_key = f'login_rate_limit:{ip_address}'
            rate_limit = 5 # Maximum allowed login attempts per minute
            current_attempts = cache.get(cache_key, 0)
            if current_attempts >= rate_limit:
                return redirect('rate_limit_exceeded')
            else:
                cache.set(cache_key, current_attempts + 1, 600)  # Store attempts for 1 minute
        return self.get_response(request)
