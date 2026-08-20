from django.urls import path
from . import views

app_name = 'linguistics'

urlpatterns = [
    path('', views.index, name='index'),
]