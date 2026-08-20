# 📁 main/views.py

# --- Импортируем всё нужное ---
from django.shortcuts import render
from tourism.models import Tour
from cases.models import Case      


def home(request):
    # Берём популярные и активные туры для карусели
    popular_tours = Tour.objects.filter(is_popular=True, is_active=True)[:8]
    featured_cases = Case.objects.filter(is_featured=True, is_active=True)[:3]
    context = {
        'popular_tours': popular_tours,
        'featured_cases': featured_cases,
    }
    return render(request, 'main/home.html', context)