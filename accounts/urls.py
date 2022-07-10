from django.urls import path
from . import views


# /accounts/...
urlpatterns = [
    path('register/', views.register, name='register'),
    path('registation_email/', views.registration_email, name='registration_email'),
    path('confirm_email/<str:uuid>/', views.confirm_email, name='confirm_email'),
]
