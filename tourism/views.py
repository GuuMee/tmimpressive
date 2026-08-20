# 📁 tourism/views.py
# ✅ ГОТОВЫЙ ФАЙЛ ЦЕЛИКОМ — можно просто заменить свой

from django.db.models import DecimalField, OuterRef, Subquery
from django.db.models.functions import Coalesce
from django.shortcuts import get_object_or_404, render

from .models import Tour, TourPrice


# ============================================================
# 🎨 ИКОНКИ И ВАРИАНТЫ ФИЛЬТРОВ
# ============================================================

TYPE_ICONS = {
    'cultural': 'fa-masks-theater',
    'adventure': 'fa-mountain-sun',
    'historical': 'fa-landmark',
    'mice': 'fa-briefcase',
    'individual': 'fa-user',
    'photo': 'fa-camera',
}

CATEGORY_ICONS = {
    'budget': 'fa-wallet',
    'standard': 'fa-star',
    'premium': 'fa-crown',
}

# ⏱️ Длительность: (код, название, иконка)
DURATION_CHOICES = [
    ('1', '1 день', 'fa-bolt'),
    ('2-3', '2–3 дня', 'fa-calendar-day'),
    ('4-7', '4–7 дней', 'fa-calendar-week'),
    ('8+', '8 дней и больше', 'fa-calendar-days'),
]

# 🗓️ Сезоны: (код, название, иконка)
SEASON_CHOICES = [
    ('spring', 'Весна', 'fa-seedling'),
    ('summer', 'Лето', 'fa-sun'),
    ('autumn', 'Осень', 'fa-leaf'),
    ('winter', 'Зима', 'fa-snowflake'),
]

# 💵 Цена: (код, название, иконка)
PRICE_CHOICES = [
    ('0-200', 'до $200', 'fa-tag'),
    ('200-500', '$200 – $500', 'fa-tags'),
    ('500-1000', '$500 – $1000', 'fa-gem'),
    ('1000+', 'от $1000', 'fa-crown'),
]


# ============================================================
# 📋 КАТАЛОГ ТУРОВ (с 6 фильтрами + AJAX)
# ============================================================
def index(request):
    # 🔍 Читаем ВСЕ фильтры из адреса одним словарём
    selected = {
        'type': request.GET.get('type', ''),
        'category': request.GET.get('category', ''),
        'direction': request.GET.get('direction', ''),
        'duration': request.GET.get('duration', ''),
        'season': request.GET.get('season', ''),
        'price': request.GET.get('price', ''),
    }

    # prefetch_related('prices') — чтобы цены категорий брались БЕЗ лишних запросов
    tours = Tour.objects.filter(is_active=True).prefetch_related('prices')

    # 1️⃣ ТИП ТУРИЗМА
    if selected['type']:
        tours = tours.filter(tour_type=selected['type'])

    # 2️⃣ КАТЕГОРИЯ — по наличию цены в этой категории!
    #    Тур попадает в «Премиум», если у него ЕСТЬ премиум-цена.
    #    Если у тура вообще нет цен — смотрим на его базовое поле category.
    if selected['category']:
        cat = selected['category']
        ids_with_price = set(
            TourPrice.objects.filter(category=cat).values_list('tour_id', flat=True)
        )
        ids_without_prices = set(
            Tour.objects.filter(prices__isnull=True, category=cat).values_list('id', flat=True)
        )
        tours = tours.filter(id__in=ids_with_price | ids_without_prices)

    # 3️⃣ НАПРАВЛЕНИЕ
    if selected['direction']:
        tours = tours.filter(direction=selected['direction'])

    # 4️⃣ ДЛИТЕЛЬНОСТЬ
    duration = selected['duration']
    if duration == '1':
        tours = tours.filter(duration_days=1)
    elif duration == '2-3':
        tours = tours.filter(duration_days__gte=2, duration_days__lte=3)
    elif duration == '4-7':
        tours = tours.filter(duration_days__gte=4, duration_days__lte=7)
    elif duration == '8+':
        tours = tours.filter(duration_days__gte=8)

    # 5️⃣ СЕЗОН (галочки в модели: season_spring, season_summer, ...)
    if selected['season'] in ('spring', 'summer', 'autumn', 'winter'):
        tours = tours.filter(**{'season_' + selected['season']: True})

    # 💰 ЦЕНА ДЛЯ КАРТОЧКИ
    #    Если выбрана категория — показываем цену ЭТОЙ категории.
    #    Если нет — минимальную цену тура. Нет цен вообще → price_from.
    price_subquery = TourPrice.objects.filter(tour=OuterRef('pk'))
    if selected['category']:
        price_subquery = price_subquery.filter(category=selected['category'])
    price_subquery = price_subquery.order_by('price').values('price')[:1]

    tours = tours.annotate(
        display_price=Coalesce(
            Subquery(
                price_subquery,
                output_field=DecimalField(max_digits=10, decimal_places=2),
            ),
            'price_from',
        )
    )

    # 6️⃣ ФИЛЬТР ПО ЦЕНЕ — работает по той цене, которую видит клиент
    price_range = selected['price']
    if price_range == '0-200':
        tours = tours.filter(display_price__lt=200)
    elif price_range == '200-500':
        tours = tours.filter(display_price__gte=200, display_price__lt=500)
    elif price_range == '500-1000':
        tours = tours.filter(display_price__gte=500, display_price__lt=1000)
    elif price_range == '1000+':
        tours = tours.filter(display_price__gte=1000)

    tours = tours.order_by('order', '-created_at')

    # 📍 Список направлений — собираем прямо из базы (без ручного ввода!)
    directions = (
        Tour.objects.filter(is_active=True)
        .exclude(direction='')
        .order_by('direction')
        .values_list('direction', flat=True)
        .distinct()
    )

    context = {
        'tours': tours,
        'selected': selected,
        'has_filters': any(selected.values()),
        # списки для сайдбара: (код, название, иконка)
        'types_with_icons': [
            (code, name, TYPE_ICONS.get(code, 'fa-tag'))
            for code, name in Tour.TYPE_CHOICES
        ],
        'categories_with_icons': [
            (code, name, CATEGORY_ICONS.get(code, 'fa-tag'))
            for code, name in Tour.CATEGORY_CHOICES
        ],
        'directions': directions,
        'duration_choices': DURATION_CHOICES,
        'season_choices': SEASON_CHOICES,
        'price_choices': PRICE_CHOICES,
        'category_label': dict(Tour.CATEGORY_CHOICES).get(selected['category'], ''),
    }

    # 🚀 AJAX: отдаём сайдбар + сетку туров (без шапки и футера)
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        return render(request, 'tourism/_catalog.html', context)

    return render(request, 'tourism/index.html', context)


# ============================================================
# 📄 ДЕТАЛЬНАЯ СТРАНИЦА ТУРА
# ============================================================
def tour_detail(request, slug):
    tour = get_object_or_404(
        Tour.objects.prefetch_related('images', 'days', 'prices', 'includes', 'category_features'),
        slug=slug,
        is_active=True,
    )

    # 🎠 Похожие туры: тот же тип туризма, кроме текущего
    similar_tours = (
        Tour.objects.filter(is_active=True, tour_type=tour.tour_type)
        .exclude(pk=tour.pk)
        .prefetch_related('prices')
        .order_by('order', '-created_at')[:6]
    )

    context = {
        'tour': tour,
        'images': tour.images.all(),
        'days': tour.days.all(),
        'prices': tour.prices.all(),
        'includes': tour.includes.all(),
        'features': tour.category_features.all(),
        'similar_tours': similar_tours,
    }
    return render(request, 'tourism/tour_detail.html', context)
