from django.contrib import admin
from .models import (
    Tour, TourImage, TourDay, TourPrice, TourInclude,
    CategoryFeature,
)


# ============================================================
# ВСТРОЕННЫЕ БЛОКИ (inline) — появятся ВНУТРИ тура
# ============================================================

class TourImageInline(admin.TabularInline):
    model = TourImage
    extra = 1
    fields = ('image', 'caption', 'order')


class TourDayInline(admin.TabularInline):
    model = TourDay
    extra = 1
    fields = ('day_number', 'title', 'description')


class TourPriceInline(admin.TabularInline):
    model = TourPrice
    extra = 3                      # сразу 3 строки: Бюджет / Стандарт / Премиум
    fields = ('category', 'season', 'price', 'note')


class TourIncludeInline(admin.TabularInline):
    model = TourInclude
    extra = 1
    fields = ('text', 'is_included', 'order')


class CategoryFeatureInline(admin.TabularInline):
    model = CategoryFeature
    extra = 1
    fields = ('feature', 'budget', 'standard', 'premium', 'order')


# ============================================================
# ГЛАВНАЯ АДМИНКА ТУРА
# ============================================================
@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'tour_type', 'direction', 'duration_days',
        'prices_preview', 'seasons_preview',
        'is_popular', 'is_active', 'order',
    )
    list_editable = ('is_popular', 'is_active', 'order')
    list_filter = (
        'tour_type', 'category', 'is_popular', 'is_active',
        'season_spring', 'season_summer', 'season_autumn', 'season_winter',
    )
    search_fields = ('title', 'direction')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('📝 Основное', {
            'fields': ('title', 'slug', 'tour_type', 'category', 'direction',
                       'duration_days', 'price_from')
        }),
        ('🗓️ Сезоны (для фильтра на сайте)', {
            'fields': ('season', ('season_spring', 'season_summer',
                                  'season_autumn', 'season_winter')),
            'description': 'Отметьте, в какие сезоны тур проводится. '
                           'Именно по этим галочкам работает фильтр «Сезон» в каталоге.'
        }),
        ('🖼️ Описание и фото', {
            'fields': ('short_description', 'full_description', 'main_image')
        }),
        ('⚙️ Отображение', {
            'fields': ('is_popular', 'is_active', 'order')
        }),
    )

    inlines = [
        TourImageInline,
        TourDayInline,
        TourPriceInline,
        TourIncludeInline,
        CategoryFeatureInline,
    ]

    # 💰 Показываем все цены прямо в списке туров
    @admin.display(description='Цены (Б / С / П)')
    def prices_preview(self, obj):
        def fmt(value):
            return f'${int(value)}' if value is not None else '—'
        return f'{fmt(obj.budget_price)} / {fmt(obj.standard_price)} / {fmt(obj.premium_price)}'

    @admin.display(description='Сезоны')
    def seasons_preview(self, obj):
        return obj.seasons_display


# Чтобы цены можно было смотреть и отдельным списком
@admin.register(TourPrice)
class TourPriceAdmin(admin.ModelAdmin):
    list_display = ('tour', 'category', 'season', 'price', 'note')
    list_filter = ('category', 'season')
    list_editable = ('price',)
    search_fields = ('tour__title',)
