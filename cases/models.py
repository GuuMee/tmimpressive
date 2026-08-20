from django.db import models

class Case(models.Model):
    DIRECTION_CHOICES = [
        ('tourism', 'Туризм'),
        ('consulting', 'Консалтинг'),
        ('linguistics', 'Лингвистика'),
    ]

    title = models.CharField('Название кейса', max_length=200)
    slug = models.SlugField('URL (латиницей)', unique=True, max_length=200)
    direction = models.CharField('Направление', max_length=20, choices=DIRECTION_CHOICES, default='tourism')
    client = models.CharField('Клиент', max_length=200, blank=True)

    short_description = models.TextField('Краткое описание', max_length=300)
    full_description = models.TextField('Полное описание', blank=True)
    result = models.CharField('Результат', max_length=300, blank=True)

    image = models.ImageField('Фото', upload_to='cases/', blank=True, null=True)

    is_featured = models.BooleanField('Показывать на главной', default=False)
    is_active = models.BooleanField('Активен', default=True)
    order = models.PositiveIntegerField('Порядок', default=0)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title
