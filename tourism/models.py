from django.db import models


# ============================================================
# 1️⃣ ГЛАВНАЯ МОДЕЛЬ — ТУР
# ============================================================
class Tour(models.Model):
    CATEGORY_CHOICES = [
        ('budget', 'Бюджет'),
        ('standard', 'Стандарт'),
        ('premium', 'Премиум'),
    ]

    # Тип туризма (для фильтров в каталоге)
    TYPE_CHOICES = [
        ('cultural', 'Культурный'),
        ('adventure', 'Приключенческий'),
        ('historical', 'Исторический'),
        ('mice', 'MICE / Деловой'),
        ('individual', 'Индивидуальный'),
        ('photo', 'Фототур'),
    ]

    title = models.CharField('Название тура', max_length=200)
    slug = models.SlugField('URL (латиницей)', unique=True, max_length=200)
    category = models.CharField('Категория', max_length=20, choices=CATEGORY_CHOICES, default='standard')
    tour_type = models.CharField('Тип туризма', max_length=20, choices=TYPE_CHOICES, default='cultural')
    direction = models.CharField('Направление', max_length=200, blank=True)
    duration_days = models.PositiveIntegerField('Длительность (дней)', default=1)
    season = models.CharField('Сезон', max_length=100, blank=True)

     # 🗓️ Сезоны (галочки) — нужны для фильтра по сезону
    season_spring = models.BooleanField('🌷 Весна', default=True)
    season_summer = models.BooleanField('☀️ Лето', default=True)
    season_autumn = models.BooleanField('🍂 Осень', default=True)
    season_winter = models.BooleanField('❄️ Зима', default=True)

    price_from = models.DecimalField('Цена от ($)', max_digits=10, decimal_places=2, default=0)

    short_description = models.TextField('Краткое описание', max_length=300, blank=True)
    full_description = models.TextField('Полное описание', blank=True)

    main_image = models.ImageField('Главное фото', upload_to='tours/', blank=True, null=True)

    is_popular = models.BooleanField('Показывать на главной', default=False)
    is_active = models.BooleanField('Активен', default=True)
    order = models.PositiveIntegerField('Порядок', default=0)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

     # 💰 Цена тура для конкретной категории (Бюджет/Стандарт/Премиум)
    def price_for(self, category):
        """Минимальная цена тура в указанной категории. None — если цены нет."""
        prices = [p.price for p in self.prices.all() if p.category == category]
        return min(prices) if prices else None

    @property
    def budget_price(self):
        return self.price_for('budget')

    @property
    def standard_price(self):
        return self.price_for('standard')

    @property
    def premium_price(self):
        return self.price_for('premium')

    @property
    def available_categories(self):
        """
        Список категорий, у которых ЕСТЬ цена:
        [('budget', 'Бюджет', 300), ('premium', 'Премиум', 650)]
        Используется на карточке тура и в каталоге.
        """
        result = []
        for code, name in self.CATEGORY_CHOICES:
            price = self.price_for(code)
            if price is not None:
                result.append((code, name, price))
        return result

    @property
    def min_price(self):
        """Самая низкая цена среди всех категорий (или price_from, если цен нет)."""
        prices = [p.price for p in self.prices.all()]
        return min(prices) if prices else self.price_from

    @property
    def seasons_display(self):
        """Красивая строка сезонов: 'Весна, Осень' или 'Круглый год'."""
        pairs = [
            (self.season_spring, 'Весна'),
            (self.season_summer, 'Лето'),
            (self.season_autumn, 'Осень'),
            (self.season_winter, 'Зима'),
        ]
        names = [name for flag, name in pairs if flag]
        if len(names) == 4:
            return 'Круглый год'
        return ', '.join(names) if names else (self.season or '—')

    @property
    def price_matrix(self):
        """
        Матрица цен для детальной страницы:
        [
          {'category': 'Бюджет', 'code': 'budget',
           'seasons': {'low': 300, 'high': 350, 'all': None}},
          ...
        ]
        """
        rows = []
        for code, name in self.CATEGORY_CHOICES:
            seasons = {'low': None, 'high': None, 'all': None}
            for p in self.prices.all():
                if p.category == code:
                    seasons[p.season] = p.price
            if any(v is not None for v in seasons.values()):
                rows.append({'code': code, 'category': name, 'seasons': seasons})
        return rows


# ============================================================
# 2️⃣ ФОТОГАЛЕРЕЯ ТУРА (5-15 фото)
# ============================================================
class TourImage(models.Model):
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,       # удалим тур → удалятся его фото
        related_name='images',          # обращение: tour.images.all()
        verbose_name='Тур'
    )
    image = models.ImageField('Фото', upload_to='tours/gallery/')
    caption = models.CharField('Подпись', max_length=200, blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Фото тура'
        verbose_name_plural = 'Фотогалерея'
        ordering = ['order']

    def __str__(self):
        return f'Фото — {self.tour.title}'


# ============================================================
# 3️⃣ ПРОГРАММА ПО ДНЯМ (не у всех туров)
# ============================================================
class TourDay(models.Model):
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='days',            # обращение: tour.days.all()
        verbose_name='Тур'
    )
    day_number = models.PositiveIntegerField('День №', default=1)
    title = models.CharField('Заголовок дня', max_length=200)
    description = models.TextField('Описание дня', blank=True)

    class Meta:
        verbose_name = 'День программы'
        verbose_name_plural = 'Программа по дням'
        ordering = ['day_number']

    def __str__(self):
        return f'{self.tour.title} — День {self.day_number}'


# ============================================================
# 4️⃣ ЦЕНЫ (категория + сезон) — гибко!
# ============================================================
class TourPrice(models.Model):
    SEASON_CHOICES = [
        ('low', 'Низкий сезoн'),
        ('high', 'Высокий сезон'),
        ('all', 'Круглый год'),
    ]

    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='prices',          # обращение: tour.prices.all()
        verbose_name='Тур'
    )
    category = models.CharField('Категория', max_length=20, choices=Tour.CATEGORY_CHOICES, default='standard')
    season = models.CharField('Сезон', max_length=10, choices=SEASON_CHOICES, default='all')
    price = models.DecimalField('Цена ($)', max_digits=10, decimal_places=2, default=0)
    note = models.CharField('Примечание', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены (категория + сезон)'
        ordering = ['category', 'season']

    def __str__(self):
        return f'{self.tour.title} — {self.get_category_display()} / {self.get_season_display()}: ${self.price}'


# ============================================================
# 5️⃣ ВКЛЮЧЕНО / НЕ ВКЛЮЧЕНО в тур
# ============================================================
class TourInclude(models.Model):
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='includes',        # обращение: tour.includes.all()
        verbose_name='Тур'
    )
    text = models.CharField('Пункт', max_length=200)
    is_included = models.BooleanField('Включено в тур?', default=True)   # True = ✔, False = ✖
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Пункт (включено/нет)'
        verbose_name_plural = 'Включено / Не включено'
        ordering = ['order']

    def __str__(self):
        mark = '✔' if self.is_included else '✖'
        return f'{mark} {self.text}'


class CategoryFeature(models.Model):
    """Особенность категории — для таблицы сравнения Бюджет/Стандарт/Премиум"""

    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='category_features',
        verbose_name='Тур'
    )

    # Название особенности (одинаковое для строки таблицы)
    feature = models.CharField(
        'Особенность',
        max_length=200,
        help_text='Например: Класс отеля, Питание, Тип группы, Трансфер'
    )

    # Что входит в каждую категорию (текст)
    budget = models.CharField(
        'Бюджет',
        max_length=200,
        blank=True,
        help_text='Например: Отель 3*. Оставь пустым если НЕ входит'
    )
    standard = models.CharField(
        'Стандарт',
        max_length=200,
        blank=True,
        help_text='Например: Отель 4*'
    )
    premium = models.CharField(
        'Премиум',
        max_length=200,
        blank=True,
        help_text='Например: Отель 5*'
    )

    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Особенность категории'
        verbose_name_plural = 'Сравнение категорий (Бюджет/Стандарт/Премиум)'
        ordering = ['order']

    def __str__(self):
        return f'{self.feature} — {self.tour.title}'