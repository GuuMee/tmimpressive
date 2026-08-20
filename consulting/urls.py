from django.urls import path
from . import views

app_name = 'consulting'

urlpatterns = [
    path('', views.index, name='index'),
]