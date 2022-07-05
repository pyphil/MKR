from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('karte/', views.karte, name='karte'),
    path('karte_bearbeiten/<int:id>', views.karte_bearbeiten, name='karte_bearbeiten'),
    path('download/<filename>', views.download, name='download'),
]
