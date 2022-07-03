from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('karte/', views.karte, name='karte'),
    path('download/', views.download, name='download'),
]
