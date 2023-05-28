from django.urls import path
from . import views
from .views import rate_limit_exceeded_view

urlpatterns = [
    path('', views.home, name='home'),
    path('karte/', views.karte, name='karte'),
    path('karte_bearbeiten/<int:id>', views.karte_bearbeiten, name='karte_bearbeiten'),
    path('download/<filename>', views.download, name='download'),
    path('rate-limit-exceeded/', rate_limit_exceeded_view, name='rate_limit_exceeded'),
]
