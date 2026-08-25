# 📁 cases/views.py

from django.shortcuts import get_object_or_404, render

from .models import Case


def list_view(request):
    """Список кейсов с фильтром по направлениям."""
    cases = Case.objects.filter(is_active=True)
    
    # Фильтр по направлению (категория)
    direction = request.GET.get('direction', '')
    if direction:
        cases = cases.filter(direction=direction)
    
    cases = cases.order_by('order', '-created_at')
    
    # Собираем все доступные направления для фильтра
    directions = (
        Case.objects
        .filter(is_active=True)
        .values_list('direction', flat=True)
        .distinct()
        .order_by('direction')
    )
    
    context = {
        'cases': cases,
        'selected_direction': direction,
        'directions': directions,
        'direction_labels': dict(Case.DIRECTION_CHOICES),
    }
    return render(request, 'cases/list.html', context)


def detail_view(request, slug):
    """Детальная страница кейса."""
    case = get_object_or_404(Case, slug=slug, is_active=True)
    
    # Похожие кейсы: то же направление, кроме текущего
    similar = (
        Case.objects
        .filter(is_active=True, direction=case.direction)
        .exclude(pk=case.pk)
        .order_by('order', '-created_at')[:6]
    )
    
    context = {
        'case': case,
        'similar': similar,
    }
    return render(request, 'cases/detail.html', context)