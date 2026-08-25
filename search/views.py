# 📁 search/views.py

from django.db.models import Q
from django.shortcuts import render

from cases.models import Case
from tourism.models import Tour

from .site_content import search_pages

# минимальная длина запроса — чтобы поиск по одной букве не грузил всю базу
MIN_QUERY_LENGTH = 2

# по каким полям ищем (лишние/отсутствующие поля будут пропущены)
TOUR_FIELDS = (
    'title', 'short_description', 'full_description', 'direction', 'season',
    'days__title', 'days__description',
)
CASE_FIELDS = (
    'title', 'short_description', 'full_description', 'client', 'result', 'direction',
)


def _existing_lookups(model, lookups):
    """
    Оставляем только те поля, которые реально есть в модели.
    Так поиск не упадёт с FieldError, если в Case нет какого-то поля.
    """
    own = {f.name for f in model._meta.get_fields()}
    result = []
    for lookup in lookups:
        root = lookup.split('__')[0]
        if root in own:
            result.append(lookup)
    return result


def _build_query(model, lookups, query):
    """Собираем условие: поле1 содержит запрос ИЛИ поле2 содержит запрос ИЛИ ..."""
    condition = Q()
    for lookup in _existing_lookups(model, lookups):
        condition |= Q(**{f'{lookup}__icontains': query})
    return condition


def _by_relevance(items, query, title_attr='title'):
    """Сначала те, у кого совпадение в названии — это почти всегда важнее."""
    q = query.lower()

    def rank(item):
        title = (getattr(item, title_attr, '') or '').lower()
        if title.startswith(q):
            return 0
        if q in title:
            return 1
        return 2

    return sorted(items, key=rank)


def search(request):
    query = (request.GET.get('q') or '').strip()
    section = request.GET.get('section') or 'all'

    tours, cases, pages = [], [], []
    too_short = bool(query) and len(query) < MIN_QUERY_LENGTH

    if query and not too_short:
        # 🌍 ТУРЫ
        tour_condition = _build_query(Tour, TOUR_FIELDS, query)
        if tour_condition:
            tours = list(
                Tour.objects.filter(is_active=True)
                .filter(tour_condition)
                .distinct()[:30]
            )
            tours = _by_relevance(tours, query)

        # 🏆 КЕЙСЫ
        case_condition = _build_query(Case, CASE_FIELDS, query)
        if case_condition:
            case_qs = Case.objects.all()
            if any(f.name == 'is_active' for f in Case._meta.get_fields()):
                case_qs = case_qs.filter(is_active=True)
            cases = list(case_qs.filter(case_condition).distinct()[:30])
            cases = _by_relevance(cases, query)

        # 📄 СТРАНИЦЫ САЙТА
        pages = search_pages(query)

    counts = {
        'tours': len(tours),
        'cases': len(cases),
        'pages': len(pages),
    }
    counts['all'] = counts['tours'] + counts['cases'] + counts['pages']

    context = {
        'query': query,
        'section': section,
        'too_short': too_short,
        'min_length': MIN_QUERY_LENGTH,
        'tours': tours,
        'cases': cases,
        'pages': pages,
        'counts': counts,
        'has_results': counts['all'] > 0,
    }
    return render(request, 'search/results.html', context)