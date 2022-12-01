from django.contrib import admin
from .models import Profile
from .models import AllowedEmail
from .models import Config

admin.site.register(Profile)
admin.site.register(AllowedEmail)
admin.site.register(Config)
