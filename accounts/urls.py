from django.urls import path
from . import views


# /accounts/...
urlpatterns = [
    path('register/', views.register, name='register'),
    path('confirm_email/<str:uuid>/', views.confirm_email, name='confirm_email'),
]
