# 📁 tourism/urls.py

from django.urls import path
from . import views

app_name = 'tourism'  # <--- Вот эта строка создаёт namespace!

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.tour_detail, name='tour_detail'),
]