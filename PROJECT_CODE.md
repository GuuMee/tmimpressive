# 📦 Код проекта TM IMPRESSIVE

> Собрано: 15.08.2026 21:56
> Всего файлов: 86

## 🌳 Структура проекта

```
tmimpressive/
├── .env
├── .gitignore
├── manage.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── views.py
    ├── __init__.py
    ├── apps.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
        ├── .gitignore
        ├── package.json
        ├── postcss.config.js
        ├── __init__.py
        ├── tour_filters.py
            ├── index.html
            ├── index.html
            ├── index.html
            ├── index.html
            ├── index.html
            ├── base.html
            ├── home.html
            ├── styles.css
            ├── _catalog.html
            ├── _tours_grid.html
            ├── index.html
            ├── tour_detail.html
                ├── footer.html
                ├── header.html
                ├── messenger_panel.html
```

## 📄 Содержимое файлов

### 📄 `.env`

```text
SECRET_KEY=***СКРЫТО***
DEBUG=True
POSTGRES_DB=impressive_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=***СКРЫТО***
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 📄 `.gitignore`

```text
venv/
__pycache__/
*.pyc
*.pyo
*.sqlite3
.env
staticfiles/
media/
```

### 📄 `manage.py`

```python
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
```

### 📄 `about\__init__.py`

```python

```

### 📄 `about\admin.py`

```python
from django.contrib import admin

# Register your models here.
```

### 📄 `about\apps.py`

```python
from django.apps import AppConfig


class AboutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
```

### 📄 `about\models.py`

```python
from django.db import models

# Create your models here.
```

### 📄 `about\tests.py`

```python
from django.test import TestCase

# Create your tests here.
```

### 📄 `about\urls.py`

```python
from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.index, name='index'),
]
```

### 📄 `about\views.py`

```python
from django.shortcuts import render

def index(request):
    return render(request, 'about/index.html')
```

### 📄 `cases\__init__.py`

```python

```

### 📄 `cases\admin.py`

```python
from django.contrib import admin
from .models import Case


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'direction', 'client', 'is_featured', 'is_active', 'order')
    list_editable = ('is_featured', 'is_active', 'order')
    list_filter = ('direction', 'is_featured', 'is_active')
    search_fields = ('title', 'client')
    prepopulated_fields = {'slug': ('title',)}
```

### 📄 `cases\apps.py`

```python
from django.apps import AppConfig


class CasesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cases'
```

### 📄 `cases\models.py`

```python
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
```

### 📄 `cases\tests.py`

```python
from django.test import TestCase

# Create your tests here.
```

### 📄 `cases\urls.py`

```python
from django.urls import path
from . import views

app_name = 'cases'

urlpatterns = [
    path('', views.case_list, name='list'),
]
```

### 📄 `cases\views.py`

```python
from django.shortcuts import render
from .models import Case


def case_list(request):
    cases = Case.objects.filter(is_active=True)
    return render(request, 'cases/case_list.html', {'cases': cases})
```

### 📄 `config\__init__.py`

```python

```

### 📄 `config\asgi.py`

```python
"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
```

### 📄 `config\settings.py`

```python
"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # читает файл .env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

     # --- Наши приложения ---
    'main',
    'tourism',
    'consulting',
    'linguistics',
    'about',
    'contacts',
    'cases',
    'search',

    'tailwind', 
    'theme',

    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
        #'DIRS': [BASE_DIR / 'templates'],
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Ashgabat'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# --- Media files (загружаемые картинки) ---
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djansgoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- Tailwind CSS ---
TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
   "127.0.0.1",
]

NPM_BIN_PATH = "C:\\Program Files\\nodejs\\npm.cmd"

APPEND_SLASH = True
```

### 📄 `config\urls.py`

```python
"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), 
    path('tourism/', include(('tourism.urls', 'tourism'), namespace='tourism')),        # 👈 вот он namespace!
    path('consulting/', include(('consulting.urls', 'consulting'), namespace='consulting')),
    path('linguistics/', include(('linguistics.urls', 'linguistics'), namespace='linguistics')),
    path('about/', include(('about.urls', 'about'), namespace='about')),
    path('contacts/', include(('contacts.urls', 'contacts'), namespace='contacts')),
    path('cases/', include(('cases.urls', 'cases'), namespace='cases')),
    # ... остальные по аналогии
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 📄 `config\wsgi.py`

```python
"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
```

### 📄 `consulting\__init__.py`

```python

```

### 📄 `consulting\admin.py`

```python
from django.contrib import admin

# Register your models here.
```

### 📄 `consulting\apps.py`

```python
from django.apps import AppConfig


class ConsultingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'consulting'
```

### 📄 `consulting\models.py`

```python
from django.db import models

# Create your models here.
```

### 📄 `consulting\tests.py`

```python
from django.test import TestCase

# Create your tests here.
```

### 📄 `consulting\urls.py`

```python
from django.urls import path
from . import views

app_name = 'consulting'

urlpatterns = [
    path('', views.index, name='index'),
]
```

### 📄 `consulting\views.py`

```python
from django.shortcuts import render

def index(request):
    return render(request, 'consulting/index.html')
```

### 📄 `contacts\__init__.py`

```python

```

### 📄 `contacts\admin.py`

```python
from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "created_at")
    search_fields = ("name", "phone", "email")
    list_filter = ("created_at",)
```

### 📄 `contacts\apps.py`

```python
from django.apps import AppConfig


class ContactsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contacts'
```

### 📄 `contacts\forms.py`

```python
from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "phone", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Ваше имя",
                "class": "w-full px-4 py-3 rounded-xl border border-gray-300 focus:border-teal focus:ring-2 focus:ring-teal/30 outline-none transition",
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "+993 __ __-__-__",
                "class": "w-full px-4 py-3 rounded-xl border border-gray-300 focus:border-teal focus:ring-2 focus:ring-teal/30 outline-none transition",
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "email@example.com (необязательно)",
                "class": "w-full px-4 py-3 rounded-xl border border-gray-300 focus:border-teal focus:ring-2 focus:ring-teal/30 outline-none transition",
            }),
            "message": forms.Textarea(attrs={
                "placeholder": "Ваше сообщение...",
                "rows": 4,
                "class": "w-full px-4 py-3 rounded-xl border border-gray-300 focus:border-teal focus:ring-2 focus:ring-teal/30 outline-none transition resize-none",
            }),
        }
```

### 📄 `contacts\models.py`

```python
from django.db import models


class ContactMessage(models.Model):
    name = models.CharField("Имя", max_length=100)
    phone = models.CharField("Телефон", max_length=30)
    email = models.EmailField("Email", blank=True)
    message = models.TextField("Сообщение")
    created_at = models.DateTimeField("Дата", auto_now_add=True)

    class Meta:
        verbose_name = "Заявка с сайта"
        verbose_name_plural = "Заявки с сайта"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.phone}"
```

### 📄 `contacts\tests.py`

```python
from django.test import TestCase

# Create your tests here.
```

### 📄 `contacts\urls.py`

```python
from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.index, name='index'),
]
```

### 📄 `contacts\views.py`

```python
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Спасибо! Ваша заявка отправлена. Мы свяжемся с вами в ближайшее время.")
            return redirect("contacts:index")
    else:
        form = ContactForm()

    return render(request, "contacts/index.html", {"form": form})
```

### 📄 `linguistics\__init__.py`

```python

```

### 📄 `linguistics\admin.py`

```python
from django.contrib import admin

# Register your models here.
```

### 📄 `linguistics\apps.py`

```python
from django.apps import AppConfig


class LinguisticsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'linguistics'
```

### 📄 `linguistics\models.py`

```python
from django.db import models

# Create your models here.
```

### 📄 `linguistics\tests.py`

```python
from django.test import TestCase

# Create your tests here.
```

### 📄 `linguistics\urls.py`

```python
from django.urls import path
from . import views

app_name = 'linguistics'

urlpatterns = [
    path('', views.index, name='index'),
]
```

### 📄 `linguistics\views.py`

```python
from django.shortcuts import render

def index(request):
    return render(request, 'linguistics/index.html')
```

### 📄 `main\__init__.py`

```python

```

### 📄 `main\admin.py`

```python
from django.contrib import admin
```

### 📄 `main\apps.py`

```python
from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
```

### 📄 `main\models.py`

```python
from django.db import models
```

### 📄 `main\tests.py`

```python
from django.test import TestCase

# Create your tests here.
```

### 📄 `main\urls.py`

```python
# 📁 main/urls.py

# --- Импортируем нужное ---
from django.urls import path
from .views import home

urlpatterns = [
   path('', home, name='home'),
]
```

### 📄 `main\views.py`

```python
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
```

### 📄 `search\__init__.py`

```python

```

### 📄 `search\admin.py`

```python
from django.contrib import admin

# Register your models here.
```

### 📄 `search\apps.py`

```python
from django.apps import AppConfig


class SearchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'search'
```

### 📄 `search\models.py`

```python
from django.db import models

# Create your models here.
```

### 📄 `search\tests.py`

```python
from django.test import TestCase

# Create your tests here.
```

### 📄 `search\views.py`

```python
from django.shortcuts import render

# Create your views here.
```

### 📄 `theme\__init__.py`

```python

```

### 📄 `theme\apps.py`

```python
from django.apps import AppConfig


class ThemeConfig(AppConfig):
    name = 'theme'
```

### 📄 `tourism\__init__.py`

```python

```

### 📄 `tourism\admin.py`

```python
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
```

### 📄 `tourism\apps.py`

```python
from django.apps import AppConfig


class TourismConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tourism'
```

### 📄 `tourism\models.py`

```python
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
```

### 📄 `tourism\tests.py`

```python
from django.test import TestCase

# Create your tests here.
```

### 📄 `tourism\urls.py`

```python
# 📁 tourism/urls.py

from django.urls import path
from . import views

app_name = 'tourism'  # <--- Вот эта строка создаёт namespace!

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.tour_detail, name='tour_detail'),
]
```

### 📄 `tourism\views.py`

```python
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
```

### 📄 `theme\static_src\.gitignore`

```text
node_modules
```

### 📄 `theme\static_src\package.json`

```json
{
  "name": "theme",
  "version": "4.5.0",
  "description": "",
  "scripts": {
    "start": "npm run dev",
    "build": "npm run build:clean && npm run build:tailwind",
    "build:clean": "rimraf ../static/css/dist",
    "build:tailwind": "cross-env NODE_ENV=production postcss ./src/styles.css -o ../static/css/dist/styles.css --minify",
    "dev": "cross-env NODE_ENV=development postcss ./src/styles.css -o ../static/css/dist/styles.css --watch"
  },
  "keywords": [],
  "author": "",
  "license": "MIT",
  "devDependencies": {
    "@tailwindcss/postcss": "^4.3.0",
    "daisyui": "^5.5.23",
    "cross-env": "^10.1.0",
    "postcss": "^8.5.15",
    "postcss-cli": "^11.0.1",
    "postcss-nested": "^7.0.2",
    "postcss-simple-vars": "^7.0.1",
    "rimraf": "^6.1.3",
    "tailwindcss": "^4.3.0"
  }
}
```

### 📄 `theme\static_src\postcss.config.js`

```javascript
module.exports = {
  plugins: {
    "@tailwindcss/postcss": {},
    "postcss-simple-vars": {},
    "postcss-nested": {}
  },
}
```

### 📄 `tourism\templatetags\__init__.py`

```python

```

### 📄 `tourism\templatetags\tour_filters.py`

```python
# 📁 tourism/templatetags/tour_filters.py
# 🆕 НОВЫЙ ФАЙЛ. Рядом с ним обязательно создайте пустой __init__.py !
#
# Что делает: строит адрес фильтра, СОХРАНЯЯ все остальные выбранные фильтры.
# Пример: {% filter_url season='summer' %}  →  ?type=cultural&season=summer

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def filter_url(context, **kwargs):
    request = context['request']
    params = request.GET.copy()

    for key, value in kwargs.items():
        if value in ('', None):
            params.pop(key, None)     # пустое значение = убрать фильтр («Все»)
        else:
            params[key] = value

    query = params.urlencode()
    return '?' + query if query else '?'
```

### 📄 `about\templates\about\index.html`

```html
{% extends "main/base.html" %}
{% load static %}

{% block title %}О компании — TM IMPRESSIVE{% endblock %}

{% block content %}

<!-- ================= HERO ================= -->
<section class="relative bg-malachite text-white">
    <div class="absolute inset-0 bg-black/40"></div>
    <div class="relative max-w-6xl mx-auto px-4 py-24 md:py-32 text-center">
        <span class="inline-block px-4 py-1 mb-4 rounded-full bg-brass/20 text-brass text-sm font-semibold tracking-wide">
            <i class="fa-solid fa-building mr-2"></i>О компании
        </span>
        <h1 class="text-4xl md:text-6xl font-bold mb-6 leading-tight">
            TM IMPRESSIVE
        </h1>
        <p class="max-w-2xl mx-auto text-lg md:text-xl text-cream/90">
            Connecting opportunities, elevating futures
        </p>
    </div>
</section>

<!-- ================= ИСТОРИЯ + МИССИЯ ================= -->
<section class="py-16 md:py-24 bg-white">
    <div class="max-w-6xl mx-auto px-4">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">

            <!-- История -->
            <div>
                <span class="text-teal tracking-widest uppercase font-bold text-sm">Наша история</span>
                <h2 class="text-3xl md:text-4xl font-extrabold text-malachite mt-3 mb-6">
                    Кто мы
                </h2>
                <p class="text-ink/70 leading-relaxed mb-4">
                    TM IMPRESSIVE — команда профессионалов, объединяющая туризм, бизнес-консалтинг
                    и лингвистические услуги в Туркменистане.
                </p>
                <p class="text-ink/70 leading-relaxed">
                    Мы помогаем открывать новые возможности: организуем незабываемые путешествия,
                    сопровождаем бизнес на местном рынке и стираем языковые барьеры.
                    Наш подход — комплексность, надёжность и внимание к каждому клиенту.
                </p>
            </div>

            <!-- Миссия -->
            <div class="bg-cream rounded-2xl p-8 md:p-10 shadow-md">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4">
                    <i class="fa-solid fa-bullseye"></i>
                </div>
                <h3 class="text-2xl font-bold text-malachite mb-3">Наша миссия</h3>
                <p class="text-ink/70 leading-relaxed">
                    Соединять людей, культуры и бизнес — открывая мир Туркменистана
                    для наших партнёров и помогая им достигать целей без границ и барьеров.
                </p>
            </div>

        </div>
    </div>
</section>

<!-- ================= ЦЕННОСТИ ================= -->
<section class="py-16 md:py-24 bg-cream">
    <div class="max-w-6xl mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-extrabold text-center text-malachite mb-4">
            Наши ценности
        </h2>
        <p class="text-center text-ink/70 mb-12 max-w-2xl mx-auto">
            Принципы, которыми мы руководствуемся каждый день
        </p>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300 text-center">
                <div class="w-16 h-16 mx-auto flex items-center justify-center rounded-xl bg-malachite text-brass text-3xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-handshake"></i>
                </div>
                <h3 class="text-lg font-bold text-malachite mb-2">Надёжность</h3>
                <p class="text-ink/70 text-sm">Держим слово и выполняем обязательства в срок.</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300 text-center">
                <div class="w-16 h-16 mx-auto flex items-center justify-center rounded-xl bg-malachite text-brass text-3xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-star"></i>
                </div>
                <h3 class="text-lg font-bold text-malachite mb-2">Качество</h3>
                <p class="text-ink/70 text-sm">Внимание к деталям на каждом этапе работы.</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300 text-center">
                <div class="w-16 h-16 mx-auto flex items-center justify-center rounded-xl bg-malachite text-brass text-3xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-lightbulb"></i>
                </div>
                <h3 class="text-lg font-bold text-malachite mb-2">Индивидуальность</h3>
                <p class="text-ink/70 text-sm">Персональный подход к каждому клиенту.</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300 text-center">
                <div class="w-16 h-16 mx-auto flex items-center justify-center rounded-xl bg-malachite text-brass text-3xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-earth-asia"></i>
                </div>
                <h3 class="text-lg font-bold text-malachite mb-2">Открытость</h3>
                <p class="text-ink/70 text-sm">Работаем честно и прозрачно на 4 языках.</p>
            </div>

        </div>
    </div>
</section>

<!-- ================= БЛОК ЦИФР ================= -->
<section class="py-16 md:py-24 bg-malachite text-white relative overflow-hidden">
    <!-- декоративное свечение -->
    <div class="absolute top-0 right-0 w-96 h-96 bg-brass/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2"></div>
    <div class="absolute bottom-0 left-0 w-96 h-96 bg-teal/20 rounded-full blur-3xl translate-y-1/2 -translate-x-1/2"></div>

    <div class="max-w-6xl mx-auto px-4 relative z-10">
        <h2 class="text-3xl md:text-4xl font-extrabold text-center mb-12">
            TM IMPRESSIVE в цифрах
        </h2>

        <div class="grid grid-cols-2 lg:grid-cols-4 gap-8 text-center">

            <div>
                <div class="text-5xl md:text-6xl font-extrabold text-brass mb-2">7+</div>
                <p class="text-cream/80">лет опыта</p>
            </div>

            <div>
                <div class="text-5xl md:text-6xl font-extrabold text-brass mb-2">500+</div>
                <p class="text-cream/80">довольных клиентов</p>
            </div>

            <div>
                <div class="text-5xl md:text-6xl font-extrabold text-brass mb-2">4</div>
                <p class="text-cream/80">рабочих языка</p>
            </div>

            <div>
                <div class="text-5xl md:text-6xl font-extrabold text-brass mb-2">100+</div>
                <p class="text-cream/80">проектов реализовано</p>
            </div>

        </div>
    </div>
</section>

<!-- ================= СЕРТИФИКАТЫ ================= -->
<section class="py-16 md:py-24 bg-white">
    <div class="max-w-6xl mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-extrabold text-center text-malachite mb-4">
            Сертификаты и лицензии
        </h2>
        <p class="text-center text-ink/70 mb-12 max-w-2xl mx-auto">
            Наша работа подтверждена официальными документами
        </p>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">

            <div class="group bg-cream rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300 text-center">
                <div class="w-16 h-16 mx-auto flex items-center justify-center rounded-xl bg-malachite text-brass text-3xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-certificate"></i>
                </div>
                <h3 class="text-lg font-bold text-malachite mb-2">Лицензия туроператора</h3>
                <p class="text-ink/70 text-sm">Официальное разрешение на туристическую деятельность.</p>
            </div>

            <div class="group bg-cream rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300 text-center">
                <div class="w-16 h-16 mx-auto flex items-center justify-center rounded-xl bg-malachite text-brass text-3xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-award"></i>
                </div>
                <h3 class="text-lg font-bold text-malachite mb-2">Сертификат качества</h3>
                <p class="text-ink/70 text-sm">Соответствие международным стандартам обслуживания.</p>
            </div>

            <div class="group bg-cream rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300 text-center">
                <div class="w-16 h-16 mx-auto flex items-center justify-center rounded-xl bg-malachite text-brass text-3xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-file-shield"></i>
                </div>
                <h3 class="text-lg font-bold text-malachite mb-2">Аккредитация переводчиков</h3>
                <p class="text-ink/70 text-sm">Дипломированные специалисты с профильным образованием.</p>
            </div>

        </div>
    </div>
</section>

<!-- ================= CTA ================= -->
<section class="py-16 md:py-20 bg-cream">
    <div class="max-w-3xl mx-auto px-4 text-center">
        <h2 class="text-3xl md:text-4xl font-extrabold text-malachite mb-4">
            Хотите работать с нами?
        </h2>
        <p class="text-ink/70 text-lg mb-8">
            Свяжитесь с нами — обсудим ваш проект. Ответим в течение 1 часа ⏱️
        </p>
        <a href="{% url 'contacts:index' %}"
           class="inline-block px-8 py-4 rounded-full bg-brass text-malachite font-bold text-lg shadow-xl hover:scale-105 transition-transform duration-200">
            Связаться с нами
        </a>
    </div>
</section>

{% endblock %}
```

### 📄 `cases\templates\cases\index.html`

```html
{% extends "main/base.html" %}
{% block content %}
<h1 class="text-3xl font-bold text-malachite">Кейсы и портфолио</h1>
<p class="mt-4">Наши реализованные проекты и кейсы.</p>
{% endblock %}
```

### 📄 `consulting\templates\consulting\index.html`

```html
{% extends "main/base.html" %}
{% load static %}

{% block title %}Бизнес-консалтинг в Туркменистане — TM IMPRESSIVE{% endblock %}

{% block content %}

<!-- ================= HERO ================= -->
<section class="relative bg-malachite text-white">
    <div class="absolute inset-0 bg-black/40"></div>
    <div class="relative max-w-6xl mx-auto px-4 py-24 md:py-32 text-center">
        <span class="inline-block px-4 py-1 mb-4 rounded-full bg-brass/20 text-brass text-sm font-semibold tracking-wide">
            <i class="fa-solid fa-briefcase mr-2"></i>Бизнес-консалтинг
        </span>
        <h1 class="text-4xl md:text-6xl font-bold mb-6 leading-tight">
            Ваш бизнес-партнёр<br>в Туркменистане
        </h1>
        <p class="max-w-2xl mx-auto text-lg md:text-xl text-cream/90 mb-8">
            Помогаем выйти на рынок, найти партнёров и вести дела уверенно.
        </p>
        <a href="{% url 'contacts:index' %}"
           class="inline-block px-8 py-4 rounded-full bg-brass text-malachite font-bold text-lg shadow-xl hover:scale-105 transition-transform duration-200">
            Обсудить проект
        </a>
    </div>
</section>

<!-- ================= УСЛУГИ ================= -->
<section class="py-16 md:py-24 bg-cream">
    <div class="max-w-6xl mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-extrabold text-center text-malachite mb-4">
            Наши услуги
        </h2>
        <p class="text-center text-ink/70 mb-12 max-w-2xl mx-auto">
            Полное сопровождение вашего бизнеса на всех этапах
        </p>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-door-open"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Выход на рынок</h3>
                <p class="text-ink/70">Анализ рынка и стратегия входа в бизнес-среду Туркменистана.</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-handshake-angle"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Поиск партнёров</h3>
                <p class="text-ink/70">Подбор надёжных местных партнёров и поставщиков.</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-file-signature"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Сопровождение сделок</h3>
                <p class="text-ink/70">Поддержка на переговорах и при заключении контрактов.</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-scale-balanced"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Юридический консалтинг</h3>
                <p class="text-ink/70">Правовое и налоговое сопровождение вашей деятельности.</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-chart-line"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Маркетинговые исследования</h3>
                <p class="text-ink/70">Анализ спроса, конкурентов и потенциала вашей ниши.</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-plane-departure"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Деловые визиты</h3>
                <p class="text-ink/70">Организация бизнес-поездок, встреч и переговоров.</p>
            </div>

        </div>
    </div>
</section>

<!-- ================= ДЛЯ КОГО ================= -->
<section class="py-16 md:py-24 bg-white">
    <div class="max-w-6xl mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-extrabold text-center text-malachite mb-12">
            Для кого
        </h2>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">

            <div class="text-center p-6">
                <div class="w-16 h-16 mx-auto flex items-center justify-center rounded-xl bg-malachite text-brass text-3xl mb-4 transition-colors duration-300 hover:bg-brass hover:text-malachite cursor-pointer">
                    <i class="fa-solid fa-building"></i>
                </div>
                <h3 class="font-bold text-malachite mb-2">Международные компании</h3>
                <p class="text-ink/70 text-sm">Выходящие на рынок Туркменистана.</p>
            </div>

            <div class="text-center p-6">
                <div class="w-16 h-16 mx-auto flex items-center justify-center rounded-xl bg-malachite text-brass text-3xl mb-4 transition-colors duration-300 hover:bg-brass hover:text-malachite cursor-pointer">
                    <i class="fa-solid fa-sack-dollar"></i>
                </div>
                <h3 class="font-bold text-malachite mb-2">Инвесторы</h3>
                <p class="text-ink/70 text-sm">Ищущие перспективные проекты в регионе.</p>
            </div>

            <div class="text-center p-6">
                <div class="w-16 h-16 mx-auto flex items-center justify-center rounded-xl bg-malachite text-brass text-3xl mb-4 transition-colors duration-300 hover:bg-brass hover:text-malachite cursor-pointer">
                    <i class="fa-solid fa-landmark-dome"></i>
                </div>
                <h3 class="font-bold text-malachite mb-2">Госструктуры</h3>
                <p class="text-ink/70 text-sm">Международное сотрудничество и проекты.</p>
            </div>

        </div>
    </div>
</section>

<!-- ================= ПАКЕТЫ ================= -->
<section class="py-16 md:py-24 bg-cream">
    <div class="max-w-6xl mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-extrabold text-center text-malachite mb-4">
            Пакеты консалтинга
        </h2>
        <p class="text-center text-ink/70 mb-12 max-w-2xl mx-auto">
            Выберите формат сотрудничества под ваши задачи
        </p>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-stretch">

            <!-- РАЗОВАЯ -->
            <div class="flex flex-col bg-white rounded-2xl p-8 shadow-md">
                <h3 class="text-2xl font-bold text-malachite mb-1">Разовая консультация</h3>
                <p class="text-ink/60 mb-4">Быстрый старт</p>
                <div class="text-4xl font-bold text-malachite mb-6">от $150</div>
                <ul class="space-y-3 mb-8 flex-1">
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Анализ вашего запроса</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Экспертная консультация</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Рекомендации по шагам</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Ответы на вопросы</li>
                </ul>
                <a href="{% url 'contacts:index' %}"
                   class="block text-center px-6 py-3 rounded-full border-2 border-malachite text-malachite font-bold hover:bg-malachite hover:text-white transition-colors duration-200">
                    Выбрать пакет
                </a>
            </div>

            <!-- СОПРОВОЖДЕНИЕ (популярный) -->
            <div class="flex flex-col bg-malachite text-white rounded-2xl p-8 shadow-2xl md:scale-105 relative border-2 border-brass">
                <span class="absolute -top-4 left-1/2 -translate-x-1/2 px-4 py-1 rounded-full bg-brass text-malachite text-sm font-bold whitespace-nowrap">
                    ⭐ Популярный
                </span>
                <h3 class="text-2xl font-bold mb-1">Сопровождение</h3>
                <p class="text-cream/70 mb-4">Оптимальный выбор</p>
                <div class="text-4xl font-bold text-brass mb-6">от $600</div>
                <ul class="space-y-3 mb-8 flex-1">
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Всё из «Разовой»</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Поиск партнёров</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Помощь на переговорах</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Юридическая поддержка</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Персональный менеджер</li>
                </ul>
                <a href="{% url 'contacts:index' %}"
                   class="block text-center px-6 py-3 rounded-full bg-brass text-malachite font-bold hover:scale-105 transition-transform duration-200">
                    Выбрать пакет
                </a>
            </div>

            <!-- ПОЛНЫЙ -->
            <div class="flex flex-col bg-white rounded-2xl p-8 shadow-md">
                <h3 class="text-2xl font-bold text-malachite mb-1">Полный пакет</h3>
                <p class="text-ink/60 mb-4">Всё под ключ</p>
                <div class="text-4xl font-bold text-malachite mb-6">от $1500</div>
                <ul class="space-y-3 mb-8 flex-1">
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Всё из «Сопровождения»</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Полный выход на рынок</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Маркетинговые исследования</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Организация деловых визитов</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Приоритетная поддержка 24/7</li>
                </ul>
                <a href="{% url 'contacts:index' %}"
                   class="block text-center px-6 py-3 rounded-full border-2 border-malachite text-malachite font-bold hover:bg-malachite hover:text-white transition-colors duration-200">
                    Выбрать пакет
                </a>
            </div>

        </div>
    </div>
</section>

<!-- ================= CTA ================= -->
<section class="py-16 md:py-20 bg-malachite text-white">
    <div class="max-w-3xl mx-auto px-4 text-center">
        <h2 class="text-3xl md:text-4xl font-extrabold mb-4">
            Готовы развивать бизнес?
        </h2>
        <p class="text-cream/90 text-lg mb-8">
            Обсудим ваш проект и найдём лучшее решение. Ответим в течение 1 часа ⏱️
        </p>
        <a href="{% url 'contacts:index' %}"
           class="inline-block px-8 py-4 rounded-full bg-brass text-malachite font-bold text-lg shadow-xl hover:scale-105 transition-transform duration-200">
            Обсудить проект
        </a>
    </div>
</section>

{% endblock %}
```

### 📄 `contacts\templates\contacts\index.html`

```html
{% extends "main/base.html" %}
{% load static %}

{% block title %}Контакты — TM IMPRESSIVE{% endblock %}

{% block content %}

<!-- ================= HERO ================= -->
<section class="relative bg-malachite text-white">
    <div class="absolute inset-0 bg-black/30"></div>
    <div class="relative max-w-6xl mx-auto px-4 py-20 md:py-28 text-center">
        <span class="inline-block px-4 py-1 mb-4 rounded-full bg-brass/20 text-brass text-sm font-semibold tracking-wide">
            <i class="fa-solid fa-phone mr-2"></i>Контакты
        </span>
        <h1 class="text-4xl md:text-6xl font-bold mb-6 leading-tight">
            Свяжитесь с нами
        </h1>
        <p class="max-w-2xl mx-auto text-lg md:text-xl text-cream/90">
            Ответим на любой вопрос в течение 1 часа ⏱️
        </p>
    </div>
</section>

<!-- ================= МЕССЕНДЖЕРЫ ================= -->
<section class="py-16 md:py-20 bg-white">
    <div class="max-w-6xl mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-extrabold text-center text-malachite mb-4">
            Напишите нам напрямую
        </h2>
        <p class="text-center text-ink/70 mb-12">
            Выберите удобный мессенджер — ответим быстро! 💬
        </p>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 max-w-5xl mx-auto">

            <!-- WhatsApp -->
            <a href="https://wa.me/99363878057" target="_blank" rel="noopener"
               class="group flex flex-col items-center bg-cream rounded-2xl p-8 shadow-md hover:shadow-xl hover:scale-105 transition-all duration-300">
                <div class="w-16 h-16 flex items-center justify-center rounded-full bg-green-500 text-white text-3xl mb-4">
                    <i class="fa-brands fa-whatsapp"></i>
                </div>
                <h3 class="text-lg font-bold text-malachite mb-1">WhatsApp</h3>
                <p class="text-ink/60 text-sm">Написать в чат</p>
            </a>

            <!-- Telegram -->
            <a href="https://t.me/+99363878057" target="_blank" rel="noopener"
               class="group flex flex-col items-center bg-cream rounded-2xl p-8 shadow-md hover:shadow-xl hover:scale-105 transition-all duration-300">
                <div class="w-16 h-16 flex items-center justify-center rounded-full bg-sky-500 text-white text-3xl mb-4">
                    <i class="fa-brands fa-telegram"></i>
                </div>
                <h3 class="text-lg font-bold text-malachite mb-1">Telegram</h3>
                <p class="text-ink/60 text-sm">Написать в чат</p>
            </a>

            <!-- Звонок -->
            <a href="tel:+99363878057"
               class="group flex flex-col items-center bg-cream rounded-2xl p-8 shadow-md hover:shadow-xl hover:scale-105 transition-all duration-300">
                <div class="w-16 h-16 flex items-center justify-center rounded-full bg-brass text-malachite text-3xl mb-4">
                    <i class="fa-solid fa-phone"></i>
                </div>
                <h3 class="text-lg font-bold text-malachite mb-1">Позвонить</h3>
                <p class="text-ink/60 text-sm">+993 63 87-80-57</p>
            </a>

                        <!-- IMO -->
            <div class="group flex flex-col items-center bg-cream rounded-2xl p-8 shadow-md hover:shadow-xl hover:scale-105 transition-all duration-300 cursor-pointer"
                 onclick="copyContact('+99363878057', this)">
                <div class="w-16 h-16 flex items-center justify-center rounded-full bg-indigo-500 text-white text-3xl mb-4">
                    <i class="fa-solid fa-comment-dots"></i>
                </div>
                <h3 class="text-lg font-bold text-malachite mb-1">IMO</h3>
                <p class="text-ink/60 text-sm copy-hint">Нажмите, чтобы скопировать номер</p>
            </div>

            <!-- WeChat -->
            <div class="group flex flex-col items-center bg-cream rounded-2xl p-8 shadow-md hover:shadow-xl hover:scale-105 transition-all duration-300 cursor-pointer"
                 onclick="copyContact('+99363878057', this)">
                <div class="w-16 h-16 flex items-center justify-center rounded-full bg-green-600 text-white text-3xl mb-4">
                    <i class="fa-brands fa-weixin"></i>
                </div>
                <h3 class="text-lg font-bold text-malachite mb-1">WeChat</h3>
                <p class="text-ink/60 text-sm copy-hint">Нажмите, чтобы скопировать номер</p>
            </div>
        </div>
    </div>
</section>

<!-- ================= ИНФО + КАРТА ================= -->
<section class="py-16 md:py-20 bg-cream">
    <div class="max-w-6xl mx-auto px-4">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-10">

            <!-- ЛЕВАЯ КОЛОНКА -->
            <div class="space-y-6">

                <!-- Адрес -->
                <div class="flex items-start gap-4 bg-white rounded-2xl p-6 shadow-md">
                    <div class="w-12 h-12 flex-shrink-0 flex items-center justify-center rounded-xl bg-malachite text-brass text-xl">
                        <i class="fa-solid fa-location-dot"></i>
                    </div>
                    <div>
                        <h3 class="font-bold text-malachite mb-1">Адрес</h3>
                        <p class="text-ink/70">Aziya Hotel, Arçabil şaýoly,<br>Ashgabat, Turkmenistan, 7444000</p>
                    </div>
                </div>

                <!-- Телефон -->
                <div class="flex items-start gap-4 bg-white rounded-2xl p-6 shadow-md">
                    <div class="w-12 h-12 flex-shrink-0 flex items-center justify-center rounded-xl bg-malachite text-brass text-xl">
                        <i class="fa-solid fa-phone"></i>
                    </div>
                    <div>
                        <h3 class="font-bold text-malachite mb-1">Телефон</h3>
                        <a href="tel:+99363878057" class="text-ink/70 hover:text-teal transition-colors">
                            +993 63 87-80-57
                        </a>
                    </div>
                </div>

                <!-- Режим работы -->
                <div class="flex items-start gap-4 bg-white rounded-2xl p-6 shadow-md">
                    <div class="w-12 h-12 flex-shrink-0 flex items-center justify-center rounded-xl bg-malachite text-brass text-xl">
                        <i class="fa-solid fa-clock"></i>
                    </div>
                    <div>
                        <h3 class="font-bold text-malachite mb-2">Режим работы</h3>
                        <ul class="text-ink/70 space-y-1 text-sm">
                            <li class="flex justify-between gap-6">
                                <span>Пн — Пт</span><span class="font-semibold">9:00 — 18:00</span>
                            </li>
                            <li class="flex justify-between gap-6">
                                <span>Суббота</span><span class="font-semibold">10:00 — 15:00</span>
                            </li>
                            <li class="flex justify-between gap-6">
                                <span>Воскресенье</span><span class="text-red-500 font-semibold">Выходной</span>
                            </li>
                        </ul>
                    </div>
                </div>

            </div>

            <!-- ПРАВАЯ КОЛОНКА: карта -->
            <div class="rounded-2xl overflow-hidden shadow-md min-h-[400px] h-full">

                <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3148.9860353059257!2d58.35975017674045!3d37.88400927195808!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3f70029ac4984093%3A0x336c29691e4d4f17!2sAziya%20Hotel!5e0!3m2!1sen!2sjp!4v1786525279711!5m2!1sen!2sjp" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"
                    width="100%" height="100%"
                    frameborder="0" allowfullscreen="true"
                    style="min-height: 400px; border: 0;"
                    title="Карта офиса TM IMPRESSIVE">
                </iframe>
            </div>

        </div>
    </div>
</section>

<!-- ================= ФОРМА ОБРАТНОЙ СВЯЗИ ================= -->
<section class="py-16 md:py-20 bg-white">
    <div class="max-w-2xl mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-extrabold text-center text-malachite mb-4">
            Оставьте заявку
        </h2>
        <p class="text-center text-ink/70 mb-10">
            Заполните форму — и мы свяжемся с вами! 📩
        </p>

        <form method="post" class="bg-cream rounded-2xl p-8 shadow-md space-y-5">
            {% csrf_token %}

            <div>
                <label class="block text-sm font-semibold text-malachite mb-2">Имя *</label>
                {{ form.name }}
            </div>

            <div>
                <label class="block text-sm font-semibold text-malachite mb-2">Телефон *</label>
                {{ form.phone }}
            </div>

            <div>
                <label class="block text-sm font-semibold text-malachite mb-2">Email</label>
                {{ form.email }}
            </div>

            <div>
                <label class="block text-sm font-semibold text-malachite mb-2">Сообщение *</label>
                {{ form.message }}
            </div>

            <button type="submit"
                    class="w-full py-3 rounded-xl bg-malachite text-white font-bold text-lg hover:bg-teal transition-colors duration-300">
                <i class="fa-solid fa-paper-plane mr-2"></i>Отправить заявку
            </button>
        </form>
    </div>
</section>

<!-- ================= POPUP УСПЕХА ================= -->
{% if messages %}
{% for message in messages %}
<div id="successPopup"
     class="fixed inset-0 z-[100] flex items-center justify-center px-4 opacity-0 pointer-events-none transition-opacity duration-300">

    <!-- Затемнённый фон -->
    <div class="absolute inset-0 bg-black/50" onclick="closePopup()"></div>

    <!-- Окно -->
    <div id="popupBox"
         class="relative bg-white rounded-2xl shadow-2xl max-w-md w-full p-8 text-center transform scale-90 transition-transform duration-300">

        <!-- Крестик -->
        <button onclick="closePopup()"
                class="absolute top-4 right-4 w-8 h-8 flex items-center justify-center rounded-full text-gray-400 hover:bg-gray-100 hover:text-gray-700 transition">
            <i class="fa-solid fa-xmark text-lg"></i>
        </button>

        <!-- Иконка -->
        <div class="w-20 h-20 mx-auto mb-5 flex items-center justify-center rounded-full bg-green-100">
            <i class="fa-solid fa-circle-check text-green-500 text-5xl"></i>
        </div>

        <!-- Текст -->
        <h3 class="text-2xl font-bold text-malachite mb-3">Спасибо!</h3>
        <p class="text-ink/70 mb-6">{{ message }}</p>

        <!-- Кнопка -->
        <button onclick="closePopup()"
                class="px-8 py-3 rounded-xl bg-malachite text-white font-bold hover:bg-teal transition-colors duration-300">
            Отлично!
        </button>
    </div>
</div>
{% endfor %}
{% endif %}

<!-- Скрипт popup -->
<script>
function closePopup() {
    var popup = document.getElementById('successPopup');
    if (popup) {
        popup.classList.add('opacity-0');
        popup.classList.remove('opacity-100');
        setTimeout(function () { popup.style.display = 'none'; }, 300);
    }
}

document.addEventListener('DOMContentLoaded', function () {
    var popup = document.getElementById('successPopup');
    if (popup) {
        // Плавное появление
        setTimeout(function () {
            popup.classList.remove('opacity-0', 'pointer-events-none');
            popup.classList.add('opacity-100');
            document.getElementById('popupBox').classList.remove('scale-90');
            document.getElementById('popupBox').classList.add('scale-100');
        }, 100);

        // Автозакрытие через 4 секунды
        setTimeout(closePopup, 4000);
    }
});
</script>

<!-- Скрипт копирования контакта -->
<script>
function copyContact(number, el) {
    navigator.clipboard.writeText(number).then(function () {
        var hint = el.querySelector('.copy-hint');
        var original = hint.textContent;
        hint.textContent = '✅ Скопировано: ' + number;
        hint.classList.add('text-green-600', 'font-semibold');
        setTimeout(function () {
            hint.textContent = original;
            hint.classList.remove('text-green-600', 'font-semibold');
        }, 2000);
    });
}
</script>




{% endblock %}
```

### 📄 `linguistics\templates\linguistics\index.html`

```html
{% extends "main/base.html" %}
{% load static %}

{% block title %}Переводы и лингвистические услуги — TM IMPRESSIVE{% endblock %}

{% block content %}

<!-- ================= HERO ================= -->
<section class="relative bg-malachite text-white">
    <div class="absolute inset-0 bg-black/40"></div>
    <div class="relative max-w-6xl mx-auto px-4 py-24 md:py-32 text-center">
        <span class="inline-block px-4 py-1 mb-4 rounded-full bg-brass/20 text-brass text-sm font-semibold tracking-wide">
            <i class="fa-solid fa-language mr-2"></i>Лингвистические услуги
        </span>
        <h1 class="text-4xl md:text-6xl font-bold mb-6 leading-tight">
            Переводы без<br>языковых барьеров
        </h1>
        <p class="max-w-2xl mx-auto text-lg md:text-xl text-cream/90 mb-6">
            Профессиональные переводы и сопровождение на 4 языках:
        </p>

        <!-- Флажки языков -->
        <div class="flex items-center justify-center gap-4 mb-8">
            <img src="https://flagcdn.com/w80/ru.png" alt="Русский"
                 class="w-9 h-6 object-cover rounded shadow ring-1 ring-white/20">
            <img src="https://flagcdn.com/w80/gb.png" alt="Английский"
                 class="w-9 h-6 object-cover rounded shadow ring-1 ring-white/20">
            <img src="https://flagcdn.com/w80/tm.png" alt="Туркменский"
                 class="w-9 h-6 object-cover rounded shadow ring-1 ring-white/20">
            <img src="https://flagcdn.com/w80/cn.png" alt="Китайский"
                 class="w-9 h-6 object-cover rounded shadow ring-1 ring-white/20">
        </div>

        <a href="{% url 'contacts:index' %}"
           class="inline-block px-8 py-4 rounded-full bg-brass text-malachite font-bold text-lg shadow-xl hover:scale-105 transition-transform duration-200">
            Заказать перевод
        </a>
    </div>
</section>

<!-- ================= УСЛУГИ ================= -->
<section class="py-16 md:py-24 bg-cream">
    <div class="max-w-6xl mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-extrabold text-center text-malachite mb-4">
            Виды переводов
        </h2>
        <p class="text-center text-ink/70 mb-12 max-w-2xl mx-auto">
            Подберём формат под ваши документы и мероприятия
        </p>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300 ">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-file-lines"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Письменный перевод</h3>
                <p class="text-ink/70">Документы, статьи, договоры и любые тексты.</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300 ">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-comments"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Устный перевод</h3>
                <p class="text-ink/70">Последовательный и синхронный на встречах.</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300 ">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-scale-balanced"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Юридический перевод</h3>
                <p class="text-ink/70">Договоры, контракты и правовые документы.</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300 ">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-briefcase-medical"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Технический перевод</h3>
                <p class="text-ink/70">Инструкции, спецификации и техдокументация.</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300 ">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-stamp"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Нотариальный перевод</h3>
                <p class="text-ink/70">Заверенные переводы официальных документов.</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-headphones"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Сопровождение мероприятий</h3>
                <p class="text-ink/70">Переводчик на конференциях и переговорах.</p>
            </div>

        </div>
    </div>
</section>

<!-- ================= ЯЗЫКИ ================= -->
<section class="py-16 md:py-24 bg-white">
    <div class="max-w-6xl mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-bold text-center text-malachite mb-4">
            Языки перевода
        </h2>
        <p class="text-center text-ink/70 mb-12 max-w-2xl mx-auto">
            Работаем со всеми комбинациями этих языков
        </p>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 sm:gap-6">

            <div class="text-center p-4 sm:p-8 bg-cream rounded-2xl shadow-md hover:shadow-xl transition-shadow duration-300">
                <img src="https://flagcdn.com/w160/ru.png" alt="Русский флаг"
                     class="w-20 h-14 sm:w-24 sm:h-16 object-cover mx-auto mb-4 rounded-lg shadow ring-1 ring-black/5">
                <h3 class="font-bold text-malachite text-base sm:text-lg">Русский</h3>
            </div>

            <div class="text-center p-4 sm:p-8 bg-cream rounded-2xl shadow-md hover:shadow-xl transition-shadow duration-300">
                <img src="https://flagcdn.com/w160/gb.png" alt="Английский флаг"
                     class="w-20 h-14 sm:w-24 sm:h-16 object-cover mx-auto mb-4 rounded-lg shadow ring-1 ring-black/5">
                <h3 class="font-bold text-malachite text-base sm:text-lg">Английский</h3>
            </div>

            <div class="text-center p-4 sm:p-8 bg-cream rounded-2xl shadow-md hover:shadow-xl transition-shadow duration-300">
                <img src="https://flagcdn.com/w160/tm.png" alt="Туркменский флаг"
                     class="w-20 h-14 sm:w-24 sm:h-16 object-cover mx-auto mb-4 rounded-lg shadow ring-1 ring-black/5">
                <h3 class="font-bold text-malachite text-base sm:text-lg">Туркменский</h3>
            </div>

            <div class="text-center p-4 sm:p-8 bg-cream rounded-2xl shadow-md hover:shadow-xl transition-shadow duration-300">
                <img src="https://flagcdn.com/w160/cn.png" alt="Китайский флаг"
                     class="w-20 h-14 sm:w-24 sm:h-16 object-cover mx-auto mb-4 rounded-lg shadow ring-1 ring-black/5">
                <h3 class="font-bold text-malachite text-base sm:text-lg">Китайский</h3>
            </div>

        </div>
    </div>
</section>

<!-- ================= ПАКЕТЫ ================= -->
<section class="py-16 md:py-24 bg-cream">
    <div class="max-w-6xl mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-extrabold text-center text-malachite mb-4">
            Пакеты услуг
        </h2>
        <p class="text-center text-ink/70 mb-12 max-w-2xl mx-auto">
            Выберите формат под объём и срочность
        </p>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-stretch">

            <!-- БАЗОВЫЙ -->
            <div class="flex flex-col bg-white rounded-2xl p-8 shadow-md">
                <h3 class="text-2xl font-bold text-malachite mb-1">Базовый</h3>
                <p class="text-ink/60 mb-4">Разовый перевод</p>
                <div class="text-4xl font-bold text-malachite mb-6">от $10</div>
                <p class="text-ink/50 text-sm -mt-4 mb-6">за страницу</p>
                <ul class="space-y-3 mb-8 flex-1">
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Письменный перевод</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> 1 языковая пара</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Стандартный срок</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Проверка редактором</li>
                </ul>
                <a href="{% url 'contacts:index' %}"
                   class="block text-center px-6 py-3 rounded-full border-2 border-malachite text-malachite font-bold hover:bg-malachite hover:text-white transition-colors duration-200">
                    Выбрать пакет
                </a>
            </div>

            <!-- БИЗНЕС (популярный) -->
            <div class="flex flex-col bg-malachite text-white rounded-2xl p-8 shadow-2xl md:scale-105 relative border-2 border-brass">
                <span class="absolute -top-4 left-1/2 -translate-x-1/2 px-4 py-1 rounded-full bg-brass text-malachite text-sm font-bold whitespace-nowrap">
                    ⭐ Популярный
                </span>
                <h3 class="text-2xl font-bold mb-1">Бизнес</h3>
                <p class="text-cream/70 mb-4">Для компаний</p>
                <div class="text-4xl font-bold text-brass mb-6">от $300</div>
                <p class="text-cream/50 text-sm -mt-4 mb-6">за проект</p>
                <ul class="space-y-3 mb-8 flex-1">
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Всё из «Базового»</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Устный перевод</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Юридические документы</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Ускоренные сроки</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Персональный менеджер</li>
                </ul>
                <a href="{% url 'contacts:index' %}"
                   class="block text-center px-6 py-3 rounded-full bg-brass text-malachite font-bold hover:scale-105 transition-transform duration-200">
                    Выбрать пакет
                </a>
            </div>

            <!-- ПРЕМИУМ -->
            <div class="flex flex-col bg-white rounded-2xl p-8 shadow-md">
                <h3 class="text-2xl font-bold text-malachite mb-1">Премиум</h3>
                <p class="text-ink/60 mb-4">Всё включено</p>
                <div class="text-4xl font-bold text-malachite mb-6">от $800</div>
                <p class="text-ink/50 text-sm -mt-4 mb-6">за проект</p>
                <ul class="space-y-3 mb-8 flex-1">
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Всё из «Бизнеса»</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Синхронный перевод</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Нотариальное заверение</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Сопровождение мероприятий</li>
                    <li class="flex items-start gap-2"><span class="text-brass">✔</span> Приоритет и поддержка 24/7</li>
                </ul>
                <a href="{% url 'contacts:index' %}"
                   class="block text-center px-6 py-3 rounded-full border-2 border-malachite text-malachite font-bold hover:bg-malachite hover:text-white transition-colors duration-200">
                    Выбрать пакет
                </a>
            </div>

        </div>
    </div>
</section>

<!-- ================= ПРЕИМУЩЕСТВА ================= -->
<section class="py-16 md:py-24 bg-white">
    <div class="max-w-6xl mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-extrabold text-center text-malachite mb-12">
            Почему выбирают нас
        </h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">

            <div class="text-center p-6">
                <div class="w-16 h-16 mx-auto flex items-center justify-center rounded-xl bg-malachite text-brass text-3xl mb-4 transition-colors duration-300 hover:bg-brass hover:text-malachite cursor-pointer">
                    <i class="fa-solid fa-user-graduate"></i>
                </div>
                <h3 class="font-bold text-malachite mb-2">Носители языка</h3>
                <p class="text-ink/70 text-sm">Переводчики с профильным образованием.</p>
            </div>

            <div class="text-center p-6">
                <div class="w-16 h-16 mx-auto flex items-center justify-center rounded-xl bg-malachite text-brass text-3xl mb-4 transition-colors duration-300 hover:bg-brass hover:text-malachite cursor-pointer">
                    <i class="fa-solid fa-clock"></i>
                </div>
                <h3 class="font-bold text-malachite mb-2">Соблюдаем сроки</h3>
                <p class="text-ink/70 text-sm">Точно в дедлайн, без задержек.</p>
            </div>

            <div class="text-center p-6">
                <div class="w-16 h-16 mx-auto flex items-center justify-center rounded-xl bg-malachite text-brass text-3xl mb-4 transition-colors duration-300 hover:bg-brass hover:text-malachite cursor-pointer">
                    <i class="fa-solid fa-shield-halved"></i>
                </div>
                <h3 class="font-bold text-malachite mb-2">Конфиденциальность</h3>
                <p class="text-ink/70 text-sm">Полная защита ваших документов.</p>
            </div>

            <div class="text-center p-6">
                <div class="w-16 h-16 mx-auto flex items-center justify-center rounded-xl bg-malachite text-brass text-3xl mb-4 transition-colors duration-300 hover:bg-brass hover:text-malachite cursor-pointer">
                    <i class="fa-solid fa-check-double"></i>
                </div>
                <h3 class="font-bold text-malachite mb-2">Контроль качества</h3>
                <p class="text-ink/70 text-sm">Двойная проверка каждого перевода.</p>
            </div>

        </div>
    </div>
</section>

<!-- ================= CTA ================= -->
<section class="py-16 md:py-20 bg-malachite text-white">
    <div class="max-w-3xl mx-auto px-4 text-center">
        <h2 class="text-3xl md:text-4xl font-extrabold mb-4">
            Нужен перевод?
        </h2>
        <p class="text-cream/90 text-lg mb-8">
            Пришлите документ — оценим объём и сроки. Ответим в течение 1 часа ⏱️
        </p>
        <a href="{% url 'contacts:index' %}"
           class="inline-block px-8 py-4 rounded-full bg-brass text-malachite font-bold text-lg shadow-xl hover:scale-105 transition-transform duration-200">
            Заказать перевод
        </a>
    </div>
</section>

{% endblock %}
```

### 📄 `main\templates\main\base.html`

```html
<!-- main/templates/main/base.html -->
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}TM IMPRESSIVE{% endblock %}</title>
    {% load static tailwind_tags %}
    {% tailwind_css %}
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
</head>
<body class="bg-[#F8F5F0] text-ink min-h-screen flex flex-col">
    {% include "main/partials/header.html" %}
    <main class="flex-1">
        {% block content %}{% endblock %}
    </main>
    {% include "main/partials/footer.html" %}
    {% include "main/partials/messenger_panel.html" %}

    {% block scripts %}{% endblock %}
</body>
</html>
```

### 📄 `main\templates\main\home.html`

```html
{% extends "main/base.html" %}
{% load static %}

{% block content %}
<section class="relative flex flex-col items-start justify-center min-h-[85vh] py-24 px-6 md:px-16">
    <!-- Баннер -->
    <img src="{% static 'images/home_hero_4K.jpg' %}" alt="TM IMPRESSIVE Banner" 
        class="absolute inset-0 object-cover w-full h-full opacity-95 pointer-events-none" />
    <!-- Контент поверх баннера -->
    <div class="relative z-10 max-w-2xl mt-8 ml-0 md:ml-20 animate-fade-in-up">
        <span class="text-lg text-teal tracking-widest uppercase font-bold mb-3 block">Откройте мир с</span>
        <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold text-malachite mb-6">TM IMPRESSIVE</h1>
        
        <p class="text-2xl md:text-3xl text-teal font-semibold mb-6">Connecting opportunities,<br> elevating futures</p>
        <p class="mb-8 text-ink leading-relaxed">
            
            Туризм, MICE, бизнес-консалтинг и лингвистика — ваш надёжный партнёр в Туркменистане и за его пределами.
        </p>
        <a href="/contacts/" class="inline-block bg-brass hover:bg-teal text-white text-lg font-bold px-8 py-3 rounded-full shadow-lg transition">Оставить заявку</a>
    </div>
    
</section>
<!-- ===== 3 НАПРАВЛЕНИЯ ===== -->
<section class="py-20 px-6 md:px-16 bg-cream">
    <div class="max-w-7xl mx-auto">

        <!-- Заголовок секции -->
        <div class="text-center mb-14">
            <span class="text-teal tracking-widest uppercase font-bold text-sm">Что мы делаем</span>
            <h2 class="text-3xl md:text-4xl font-extrabold text-malachite mt-3">
                Три направления — одна команда
            </h2>
            <div class="w-24 h-1 bg-brass mx-auto mt-5 rounded-full"></div>
        </div>

        <!-- Карточки -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">

            <!-- 🗺️ Карточка 1: Туризм (главная, выделена) -->
            <a href="{% url 'tourism:index' %}"
               class="group relative bg-white rounded-2xl p-8 shadow-md hover:shadow-2xl border-2 border-brass hover:-translate-y-2 transition-all duration-300 overflow-hidden">
                <!-- Бейдж «Флагман» -->
                <span class="absolute top-4 right-4 bg-brass text-malachite text-xs font-bold px-3 py-1 rounded-full">★ Флагман</span>
                
                <div class="w-16 h-16 flex items-center justify-center rounded-xl bg-malachite text-brass text-3xl mb-6 group-hover:scale-110 transition-transform">
                    <i class="fa-solid fa-plane-departure"></i>
                </div>
                <h3 class="text-2xl font-bold text-malachite mb-3">Туризм и MICE</h3>
                <p class="text-ink/70 leading-relaxed mb-5">
                    Авторские туры по Туркменистану, деловые поездки, организация мероприятий и корпоративного отдыха.
                </p>
                <span class="inline-flex items-center gap-2 text-brass font-bold group-hover:gap-3 transition-all">
                    Подробнее <i class="fa-solid fa-arrow-right"></i>
                </span>
            </a>

            <!-- 💼 Карточка 2: Консалтинг -->
            <a href="{% url 'consulting:index' %}"
               class="group relative bg-white rounded-2xl p-8 shadow-md hover:shadow-2xl border-2 border-transparent hover:border-teal hover:-translate-y-2 transition-all duration-300">
                <div class="w-16 h-16 flex items-center justify-center rounded-xl bg-teal text-white text-3xl mb-6 group-hover:scale-110 transition-transform">
                    <i class="fa-solid fa-briefcase"></i>
                </div>
                <h3 class="text-2xl font-bold text-malachite mb-3">Бизнес-консалтинг</h3>
                <p class="text-ink/70 leading-relaxed mb-5">
                    Помощь в выходе на рынок Туркменистана, юридическое сопровождение и стратегическое развитие бизнеса.
                </p>
                <span class="inline-flex items-center gap-2 text-teal font-bold group-hover:gap-3 transition-all">
                    Подробнее <i class="fa-solid fa-arrow-right"></i>
                </span>
            </a>

            <!-- 🗣️ Карточка 3: Лингвистика -->
            <a href="{% url 'linguistics:index' %}"
               class="group relative bg-white rounded-2xl p-8 shadow-md hover:shadow-2xl border-2 border-transparent hover:border-teal hover:-translate-y-2 transition-all duration-300">
                <div class="w-16 h-16 flex items-center justify-center rounded-xl bg-teal text-white text-3xl mb-6 group-hover:scale-110 transition-transform">
                    <i class="fa-solid fa-language"></i>
                </div>
                <h3 class="text-2xl font-bold text-malachite mb-3">Лингвистика</h3>
                <p class="text-ink/70 leading-relaxed mb-5">
                    Профессиональный перевод, синхронный перевод на мероприятиях и аренда оборудования для конференций.
                </p>
                <span class="inline-flex items-center gap-2 text-teal font-bold group-hover:gap-3 transition-all">
                    Подробнее <i class="fa-solid fa-arrow-right"></i>
                </span>
            </a>

        </div>
    </div>
</section>

<!-- ===== ПОПУЛЯРНЫЕ ТУРЫ ===== -->
<section class="py-20 px-6 md:px-16 bg-white">
    <div class="max-w-7xl mx-auto">

        <!-- Заголовок -->
        <div class="flex flex-col md:flex-row md:items-end md:justify-between mb-14 gap-4">
            <div>
                <span class="text-teal tracking-widest uppercase font-bold text-sm">Направления</span>
                <h2 class="text-3xl md:text-4xl font-extrabold text-malachite mt-3">
                    Популярные туры
                </h2>
                <div class="w-24 h-1 bg-brass mt-5 rounded-full"></div>
            </div>
            <a href="{% url 'tourism:index' %}"
               class="inline-flex items-center gap-2 text-teal font-bold hover:text-malachite transition self-start md:self-auto">
                Все туры <i class="fa-solid fa-arrow-right"></i>
            </a>
        </div>

        <!-- Сетка туров -->
        {% if popular_tours %}
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            {% for tour in popular_tours %}
            <div class="group bg-cream rounded-2xl overflow-hidden shadow-md hover:shadow-2xl hover:-translate-y-2 transition-all duration-300">

                <!-- Фото или заглушка -->
                <div class="relative h-48 overflow-hidden">
                    {% if tour.main_image %}
                        <img src="{{ tour.main_image.url }}" alt="{{ tour.title }}"
                             class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
                    {% else %}
                        <div class="w-full h-full bg-gradient-to-br from-malachite to-teal flex items-center justify-center">
                            <i class="fa-solid fa-mountain-sun text-brass text-5xl opacity-50"></i>
                        </div>
                    {% endif %}
                    <!-- Категория -->
                    <span class="absolute top-3 left-3 bg-brass text-malachite text-xs font-bold px-3 py-1 rounded-full">
                        {{ tour.get_category_display }}
                    </span>
                </div>

                <!-- Инфо -->
                <div class="p-5">
                    <h3 class="text-lg font-bold text-malachite mb-2 line-clamp-1">{{ tour.title }}</h3>
                    <p class="text-ink/60 text-sm mb-4 line-clamp-2">
                        {{ tour.short_description|default:"Незабываемое путешествие с TM Impressive" }}
                    </p>

                    <div class="flex items-center justify-between text-sm">
                        <span class="text-teal font-semibold">
                            <i class="fa-regular fa-clock"></i> {{ tour.duration_days }} дн.
                        </span>
                        <span class="text-malachite font-extrabold text-lg">
                            от ${{ tour.price_from|floatformat:0 }}
                        </span>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
        {% else %}
        <p class="text-center text-ink/50 py-10">Скоро здесь появятся туры 🌍</p>
        {% endif %}

    </div>
</section>

<!-- ===== ПОЧЕМУ ВЫБИРАЮТ НАС ===== -->
<section class="py-20 px-6 md:px-16 bg-malachite text-white relative overflow-hidden">
    <!-- Декоративный узор (мягкое свечение) -->
    <div class="absolute top-0 right-0 w-96 h-96 bg-brass/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2"></div>
    <div class="absolute bottom-0 left-0 w-96 h-96 bg-teal/20 rounded-full blur-3xl translate-y-1/2 -translate-x-1/2"></div>

    <div class="max-w-7xl mx-auto relative z-10">

        <!-- Заголовок -->
        <div class="text-center mb-16">
            <span class="text-brass tracking-widest uppercase font-bold text-sm">Наши преимущества</span>
            <h2 class="text-3xl md:text-4xl font-extrabold mt-3">
                Почему выбирают <span class="text-brass">TM Impressive</span>
            </h2>
            <div class="w-24 h-1 bg-brass mx-auto mt-5 rounded-full"></div>
        </div>

        <!-- 4 преимущества -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">

            <!-- 1 -->
            <div class="text-center group">
                <div class="w-20 h-20 mx-auto flex items-center justify-center rounded-2xl bg-white/10 text-brass text-4xl mb-5 group-hover:bg-brass group-hover:text-malachite transition-all duration-300">
                    <i class="fa-solid fa-award"></i>
                </div>
                <h3 class="text-xl font-bold mb-2">Локальная экспертиза</h3>
                <p class="text-white/70 text-sm leading-relaxed">
                    Глубокое знание рынка Туркменистана и надёжные связи с местными партнёрами.
                </p>
            </div>

            <!-- 2 -->
            <div class="text-center group">
                <div class="w-20 h-20 mx-auto flex items-center justify-center rounded-2xl bg-white/10 text-brass text-4xl mb-5 group-hover:bg-brass group-hover:text-malachite transition-all duration-300">
                    <i class="fa-solid fa-headset"></i>
                </div>
                <h3 class="text-xl font-bold mb-2">Поддержка 24/7</h3>
                <p class="text-white/70 text-sm leading-relaxed">
                    Всегда на связи — ответим на любой вопрос в течение часа в удобном мессенджере.
                </p>
            </div>

            <!-- 3 -->
            <div class="text-center group">
                <div class="w-20 h-20 mx-auto flex items-center justify-center rounded-2xl bg-white/10 text-brass text-4xl mb-5 group-hover:bg-brass group-hover:text-malachite transition-all duration-300">
                    <i class="fa-solid fa-globe"></i>
                </div>
                <h3 class="text-xl font-bold mb-2">Работаем на 4 языках</h3>
                <p class="text-white/70 text-sm leading-relaxed">
                    Русский, английский, туркменский, китайский — общаемся без языковых барьеров.
                </p>
            </div>

            <!-- 4 -->
            <div class="text-center group">
                <div class="w-20 h-20 mx-auto flex items-center justify-center rounded-2xl bg-white/10 text-brass text-4xl mb-5 group-hover:bg-brass group-hover:text-malachite transition-all duration-300">
                    <i class="fa-solid fa-handshake"></i>
                </div>
                <h3 class="text-xl font-bold mb-2">Комплексный подход</h3>
                <p class="text-white/70 text-sm leading-relaxed">
                    Туризм, консалтинг и переводы — всё в одном месте, под ключ и без хлопот.
                </p>
            </div>

        </div>
    </div>
</section>

<!-- ===== КЕЙСЫ ===== -->
<section class="py-20 px-6 md:px-16 bg-cream">
    <div class="max-w-7xl mx-auto">

        <!-- Заголовок -->
        <div class="flex flex-col md:flex-row md:items-end md:justify-between mb-14 gap-4">
            <div>
                <span class="text-teal tracking-widest uppercase font-bold text-sm">Наши работы</span>
                <h2 class="text-3xl md:text-4xl font-extrabold text-malachite mt-3">
                    Реализованные проекты
                </h2>
                <div class="w-24 h-1 bg-brass mt-5 rounded-full"></div>
            </div>
            <a href="{% url 'cases:list' %}"
               class="inline-flex items-center gap-2 text-teal font-bold hover:text-malachite transition self-start md:self-auto">
                Все кейсы <i class="fa-solid fa-arrow-right"></i>
            </a>
        </div>

        <!-- Сетка кейсов -->
        {% if featured_cases %}
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
            {% for case in featured_cases %}
            <div class="group bg-white rounded-2xl overflow-hidden shadow-md hover:shadow-2xl hover:-translate-y-2 transition-all duration-300">

                <!-- Фото или заглушка -->
                <div class="relative h-56 overflow-hidden">
                    {% if case.image %}
                        <img src="{{ case.image.url }}" alt="{{ case.title }}"
                             class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
                    {% else %}
                        <div class="w-full h-full bg-gradient-to-br from-teal to-malachite flex items-center justify-center">
                            <i class="fa-solid fa-trophy text-brass text-5xl opacity-50"></i>
                        </div>
                    {% endif %}
                    <!-- Направление -->
                    <span class="absolute top-3 left-3 bg-brass text-malachite text-xs font-bold px-3 py-1 rounded-full">
                        {{ case.get_direction_display }}
                    </span>
                </div>

                <!-- Инфо -->
                <div class="p-6">
                    {% if case.client %}
                    <span class="text-ink/50 text-xs uppercase tracking-wider">{{ case.client }}</span>
                    {% endif %}
                    <h3 class="text-xl font-bold text-malachite mb-3 mt-1 line-clamp-2">{{ case.title }}</h3>
                    <p class="text-ink/60 text-sm mb-4 line-clamp-3">
                        {{ case.short_description }}
                    </p>

                    {% if case.result %}
                    <div class="flex items-start gap-2 pt-4 border-t border-cream">
                        <i class="fa-solid fa-circle-check text-teal mt-1"></i>
                        <span class="text-malachite text-sm font-semibold">{{ case.result }}</span>
                    </div>
                    {% endif %}
                </div>
            </div>
            {% endfor %}
        </div>
        {% else %}
        <p class="text-center text-ink/50 py-10">Скоро здесь появятся кейсы 🏆</p>
        {% endif %}

    </div>
</section>

<!-- ===== ПАРТНЁРЫ (marquee) ===== -->
<section class="py-16 bg-white overflow-hidden">
    <div class="max-w-7xl mx-auto px-6 md:px-16">
        <p class="text-center text-ink/40 uppercase tracking-widest text-sm font-bold mb-10">
            Нам доверяют
        </p>
    </div>

    <!-- Бегущая лента -->
    <div class="relative flex overflow-hidden">
        <!-- маска-затемнение по краям -->
        <div class="absolute left-0 top-0 bottom-0 w-32 bg-gradient-to-r from-white to-transparent z-10"></div>
        <div class="absolute right-0 top-0 bottom-0 w-32 bg-gradient-to-l from-white to-transparent z-10"></div>

        <!-- ПЕРВАЯ копия ленты -->
        <div class="flex items-center gap-16 animate-marquee whitespace-nowrap pr-16 shrink-0">
            {% for i in "1234" %}
                <span class="text-2xl font-bold text-malachite/40 hover:text-teal transition">CNPC</span>
                <span class="text-2xl font-bold text-malachite/40 hover:text-teal transition">ЕАЭС Форум</span>
                <span class="text-2xl font-bold text-malachite/40 hover:text-teal transition">ООО «Ромашка»</span>
                <span class="text-2xl font-bold text-malachite/40 hover:text-teal transition">Turkmen Air</span>
                <span class="text-2xl font-bold text-malachite/40 hover:text-teal transition">Business Group</span>
                <span class="text-2xl font-bold text-malachite/40 hover:text-teal transition">Silk Road Co.</span>
            {% endfor %}
        </div>

        <!-- ВТОРАЯ копия ленты (для бесшовности) -->
        <div class="flex items-center gap-16 animate-marquee whitespace-nowrap pr-16 shrink-0" aria-hidden="true">
            {% for i in "1234" %}
                <span class="text-2xl font-bold text-malachite/40 hover:text-teal transition">CNPC</span>
                <span class="text-2xl font-bold text-malachite/40 hover:text-teal transition">ЕАЭС Форум</span>
                <span class="text-2xl font-bold text-malachite/40 hover:text-teal transition">ООО «Ромашка»</span>
                <span class="text-2xl font-bold text-malachite/40 hover:text-teal transition">Turkmen Air</span>
                <span class="text-2xl font-bold text-malachite/40 hover:text-teal transition">Business Group</span>
                <span class="text-2xl font-bold text-malachite/40 hover:text-teal transition">Silk Road Co.</span>
            {% endfor %}
        </div>
    </div>
</section>

<!-- ===== CTA — ПРИЗЫВ ОСТАВИТЬ ЗАЯВКУ ===== -->
<section class="py-24 bg-malachite relative overflow-hidden">
    <!-- декоративные размытые круги -->
    <div class="absolute top-0 right-0 w-96 h-96 bg-teal/20 rounded-full blur-3xl -translate-y-1/3 translate-x-1/3"></div>
    <div class="absolute bottom-0 left-0 w-96 h-96 bg-brass/10 rounded-full blur-3xl translate-y-1/3 -translate-x-1/3"></div>

    <div class="max-w-4xl mx-auto px-6 md:px-16 text-center relative z-10">
        <p class="text-brass uppercase tracking-widest text-sm font-bold mb-6">
            Готовы начать?
        </p>

        <h2 class="text-4xl md:text-5xl font-bold text-cream leading-tight mb-6">
            Организуем ваше мероприятие<br class="hidden md:block">
            под ключ
        </h2>

        <p class="text-cream/70 text-lg mb-10 max-w-2xl mx-auto">
            Оставьте заявку — и мы свяжемся с вами в течение дня,
            чтобы обсудить детали вашего проекта.
        </p>

        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <a href="#"
               class="inline-block bg-brass text-malachite font-bold px-10 py-4 rounded-full hover:bg-brass/90 transition text-lg shadow-lg">
                Оставить заявку
            </a>
            <a href="#"
               class="inline-block border-2 border-cream/30 text-cream font-bold px-10 py-4 rounded-full hover:bg-cream/10 transition text-lg">
                Связаться с нами
            </a>
        </div>
    </div>
</section>
{% endblock %}
```

### 📄 `theme\static_src\src\styles.css`

```css
@import "tailwindcss";
@plugin "daisyui";

/**
  * A catch-all path to Django template files, JavaScript, and Python files
  * that contain Tailwind CSS classes and will be scanned by Tailwind to generate the final CSS file.
  *
  * If your final CSS file is not being updated after code changes, you may want to broaden or narrow
  * the scope of this path.
  */

@theme {
    /* 🟢 Малахитовый — основной, для заголовков и шапки */
    --color-malachite: #0B3D2E;

    /* 🟡 Латунь — акценты, кнопки, текст на тёмном фоне */
    --color-brass: #D4AF37;

    /* 🟢 Бирюзовый — подзаголовки */
    --color-teal: #3D7A6F;

    /* ⚫ Тёмно-серый — основной текст */
    --color-ink: #2C2C2C;

    /* 🤍 Кремовый — фон страницы */
    --color-cream: #F8F5F0;

    /* \(тёмный для футера) */
    --color-forest-dark: #082419;  

      --animate-marquee: marquee 30s linear infinite;
}


@source "../../../**/*.{html,py,js}";


@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(30px); }
  to   { opacity: 1; transform: translateY(0); }
}

.animate-fade-in-up {
  animation: fade-in-up 1s ease-out;
}


@keyframes marquee {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
```

### 📄 `tourism\templates\tourism\_catalog.html`

```html
{# ============================================================ #}
{# 📁 tourism/templates/tourism/_catalog.html                    #}
{# 🆕 НОВЫЙ ФАЙЛ — сайдбар + сетка. Именно ЭТО подменяет AJAX,   #}
{#    поэтому подсветка фильтров всегда правильная (её рисует     #}
{#    Django, а не JavaScript).                                   #}
{# ============================================================ #}

<!-- ЛЕВЫЙ САЙДБАР -->
<aside class="lg:col-span-1">
    {% include 'tourism/_filters.html' %}
</aside>

<!-- ПРАВАЯ ЧАСТЬ — ТУРЫ -->
<div class="lg:col-span-3">
    {% include 'tourism/_tours_grid.html' %}
</div>
```

### 📄 `tourism\templates\tourism\_tours_grid.html`

```html
{# ============================================================ #}
{# 📁 tourism/templates/tourism/_tours_grid.html                 #}
{# 🔄 ЗАМЕНИТЬ ЦЕЛИКОМ — карточки туров с ценами по категориям   #}
{# ============================================================ #}

{# ---------- Плашка: сколько найдено + активная категория ---------- #}
<div class="flex flex-wrap items-center justify-between gap-3 mb-6">
    <p class="text-ink/50">
        Найдено туров: <b class="text-malachite">{{ tours|length }}</b>
    </p>

    {% if selected.category %}
    <p class="text-sm bg-brass/20 text-malachite font-semibold px-4 py-1.5 rounded-full">
        <i class="fa-solid fa-tag"></i> Цены показаны для категории: {{ category_label }}
    </p>
    {% endif %}
</div>

<div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-6">
    {% for tour in tours %}
    <div class="bg-white rounded-2xl shadow-md overflow-hidden flex flex-col hover:shadow-xl transition-shadow duration-300">

        <!-- Фото -->
        <div class="relative h-56 bg-gradient-to-br from-malachite to-teal">
            {% if tour.main_image %}
                <img src="{{ tour.main_image.url }}" alt="{{ tour.title }}"
                     class="w-full h-full object-cover">
            {% else %}
                <div class="w-full h-full flex items-center justify-center">
                    <i class="fa-regular fa-image text-brass/60 text-5xl"></i>
                </div>
            {% endif %}

            <!-- Бейдж категории: если фильтр выбран — показываем выбранную -->
            <span class="absolute top-3 left-3 px-3 py-1 rounded-full bg-brass text-malachite text-xs font-bold">
                {% if selected.category %}{{ category_label }}{% else %}{{ tour.get_category_display }}{% endif %}
            </span>
            <span class="absolute top-3 right-3 px-3 py-1 rounded-full bg-malachite text-white text-xs font-bold">
                {{ tour.get_tour_type_display }}
            </span>
        </div>

        <!-- Контент -->
        <div class="p-6 flex flex-col flex-grow">
            <h3 class="text-xl font-bold text-malachite mb-1">{{ tour.title }}</h3>

            {% if tour.direction %}
            <p class="text-teal text-sm font-semibold mb-2">
                <i class="fa-solid fa-location-dot"></i> {{ tour.direction }}
            </p>
            {% endif %}

            <p class="text-ink/60 text-sm mb-4 flex-grow">
                {{ tour.short_description|default:"Незабываемое путешествие с TM Impressive" }}
            </p>

            <!-- 💰 ЦЕНЫ ПО КАТЕГОРИЯМ -->
            {% if tour.available_categories %}
            <div class="mb-4 space-y-1.5">
                {% for code, name, price in tour.available_categories %}
                <div class="flex items-center justify-between text-sm px-3 py-1.5 rounded-lg
                    {% if selected.category == code %}bg-brass/20 ring-1 ring-brass{% else %}bg-cream{% endif %}">
                    <span class="text-ink/70 font-semibold">
                        {% if code == 'budget' %}<i class="fa-solid fa-wallet text-teal"></i>
                        {% elif code == 'standard' %}<i class="fa-solid fa-star text-teal"></i>
                        {% else %}<i class="fa-solid fa-crown text-brass"></i>{% endif %}
                        {{ name }}
                    </span>
                    <b class="text-malachite">${{ price|floatformat:0 }}</b>
                </div>
                {% endfor %}
            </div>
            {% endif %}

            <!-- Итоговая строка: длительность + цена -->
            <div class="flex items-center justify-between pt-3 border-t border-cream mb-4">
                <span class="text-ink/60 text-sm flex items-center gap-1">
                    <i class="fa-regular fa-clock"></i> {{ tour.duration_days }} дн.
                </span>
                <span class="text-malachite font-extrabold text-lg">
                    {% if selected.category %}
                        ${{ tour.display_price|floatformat:0 }}
                    {% else %}
                        от ${{ tour.display_price|floatformat:0 }}
                    {% endif %}
                </span>
            </div>

            <a href="{% url 'tourism:tour_detail' tour.slug %}{% if selected.category %}?category={{ selected.category }}{% endif %}"
               class="block text-center px-4 py-2.5 rounded-full bg-malachite text-white font-bold text-sm hover:bg-teal transition-colors duration-200">
                Подробнее
            </a>
        </div>
    </div>
    {% empty %}
    <div class="col-span-full text-center py-16 bg-white rounded-2xl">
        <i class="fa-solid fa-magnifying-glass text-ink/20 text-5xl mb-4"></i>
        <p class="text-ink/50 text-lg mb-3">По выбранным фильтрам туров не найдено</p>
        <a href="{% url 'tourism:index' %}"
           class="filter-link inline-block text-malachite font-bold hover:underline">
            <i class="fa-solid fa-rotate-left"></i> Сбросить фильтры
        </a>
    </div>
    {% endfor %}
</div>
```

### 📄 `tourism\templates\tourism\index.html`

```html
{% extends "main/base.html" %}
{% load static %}

{% block title %}Каталог туров — TM IMPRESSIVE{% endblock %}

{% block content %}

<!-- ================= HERO ================= -->
<section class="relative bg-malachite text-white">
    <div class="absolute inset-0 bg-black/40"></div>
    <div class="relative max-w-6xl mx-auto px-4 py-20 md:py-28 text-center">
        <span class="inline-block px-4 py-1 mb-4 rounded-full bg-brass/20 text-brass text-sm font-semibold tracking-wide">
            ⭐ Каталог туров
        </span>
        <h1 class="text-4xl md:text-6xl font-extrabold mb-6 leading-tight">
            Туры по Туркменистану
        </h1>
        <p class="max-w-2xl mx-auto text-lg md:text-xl text-cream/90">
            Выберите направление мечты — от древних городов до пустынных приключений
        </p>
    </div>
</section>

<!-- ================= КАТАЛОГ С САЙДБАРОМ ================= -->
<section id="catalog" class="py-12 bg-cream min-h-screen">
    <div class="max-w-7xl mx-auto px-4">

        <!-- 🎯 Именно это содержимое AJAX подменяет целиком -->
        <div id="catalog-wrapper"
             class="grid grid-cols-1 lg:grid-cols-4 gap-8 transition-opacity duration-200">
            {% include 'tourism/_catalog.html' %}
        </div>

    </div>
</section>

<!-- ================= CTA ================= -->
<section class="py-16 md:py-20 bg-malachite text-white">
    <div class="max-w-3xl mx-auto px-4 text-center">
        <h2 class="text-3xl md:text-4xl font-extrabold mb-4">
            Не нашли подходящий тур?
        </h2>
        <p class="text-cream/90 text-lg mb-8">
            Составим индивидуальный маршрут под ваши пожелания! ⏱️
        </p>
        <a href="{% url 'contacts:index' %}"
           class="inline-block px-8 py-4 rounded-full bg-brass text-malachite font-bold text-lg shadow-xl hover:scale-105 transition-transform duration-200">
            Заказать индивидуальный тур
        </a>
    </div>
</section>

{% endblock %}


{# ⚠️ ВАЖНО: блок scripts ВНЕ блока content! (раньше он был внутри — #}
{#    из-за этого скрипт вставлялся на страницу ДВА раза)             #}
{% block scripts %}
<script>
document.addEventListener('DOMContentLoaded', function () {
    const wrapper = document.getElementById('catalog-wrapper');
    if (!wrapper) return;

    // 🚀 Загружаем каталог (сайдбар + туры) без перезагрузки страницы
    function loadCatalog(url, pushHistory) {
        wrapper.style.opacity = '0.35';
        wrapper.style.pointerEvents = 'none';

        fetch(url, { headers: { 'X-Requested-With': 'XMLHttpRequest' } })
            .then(function (response) { return response.text(); })
            .then(function (html) {
                wrapper.innerHTML = html;
                wrapper.style.opacity = '1';
                wrapper.style.pointerEvents = 'auto';
                if (pushHistory) {
                    history.pushState({ ajax: true }, '', url);
                }
            })
            .catch(function () {
                window.location.href = url;   // если что-то пошло не так — обычный переход
            });
    }

    // 🖱️ Делегирование клика: работает даже после подмены HTML
    document.addEventListener('click', function (e) {
        const link = e.target.closest('a.filter-link');
        if (!link || !wrapper.contains(link)) return;

        e.preventDefault();
        loadCatalog(link.getAttribute('href'), true);
    });

    // ⬅️ Кнопка "Назад" в браузере тоже работает
    window.addEventListener('popstate', function () {
        loadCatalog(window.location.pathname + window.location.search, false);
    });
});
</script>
{% endblock %}
```

### 📄 `tourism\templates\tourism\tour_detail.html`

```html
{% extends "main/base.html" %}
{% load static %}

{% block title %}{{ tour.title }} — TM IMPRESSIVE{% endblock %}

{% block content %}

<!-- ================= HERO с фото ================= -->
<section class="relative bg-malachite text-white">
    {% if tour.main_image %}
        <img src="{{ tour.main_image.url }}" alt="{{ tour.title }}"
             class="absolute inset-0 w-full h-full object-cover opacity-30">
    {% endif %}
    <div class="absolute inset-0 bg-black/40"></div>
    <div class="relative max-w-6xl mx-auto px-4 py-20 md:py-28">
        <a href="{% url 'tourism:index' %}"
           class="inline-flex items-center gap-2 text-cream/80 hover:text-brass transition mb-6">
            <i class="fa-solid fa-arrow-left"></i> Назад к турам
        </a>
        <div class="flex flex-wrap gap-2 mb-4">
            <span class="px-4 py-1 rounded-full bg-brass text-malachite text-sm font-bold">
                {{ tour.get_category_display }}
            </span>
            <span class="px-4 py-1 rounded-full bg-white/20 text-white text-sm font-bold">
                {{ tour.get_tour_type_display }}
            </span>
        </div>
        <h1 class="text-4xl md:text-6xl font-extrabold mb-4 leading-tight">{{ tour.title }}</h1>
        {% if tour.direction %}
        <p class="text-lg md:text-xl text-cream/90">
            <i class="fa-solid fa-location-dot text-brass"></i> {{ tour.direction }}
        </p>
        {% endif %}
    </div>
</section>

<!-- ================= ОСНОВНОЙ КОНТЕНТ ================= -->
<section class="py-16 bg-cream">
    <div class="max-w-6xl mx-auto px-4">
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">

            <!-- ===== ЛЕВАЯ КОЛОНКА ===== -->
            <div class="lg:col-span-2 space-y-10">

                <!-- 📝 Описание -->
                <div class="bg-white rounded-2xl p-8 shadow-md">
                    <h2 class="text-2xl font-bold text-malachite mb-4">О туре</h2>
                    <p class="text-ink/80 leading-relaxed text-lg">{{ tour.short_description }}</p>
                    {% if tour.full_description %}
                        <div class="text-ink/70 leading-relaxed mt-4">
                            {{ tour.full_description|linebreaks }}
                        </div>
                    {% endif %}
                </div>

                <!-- 📷 Фотогалерея -->
                {% if images %}
                <div class="bg-white rounded-2xl p-8 shadow-md">
                    <h2 class="text-2xl font-bold text-malachite mb-6">📷 Фотогалерея</h2>
                    <div class="grid grid-cols-2 sm:grid-cols-3 gap-4">
                        {% for img in images %}
                        <div class="group relative rounded-xl overflow-hidden shadow aspect-square">
                            <img src="{{ img.image.url }}" alt="{{ img.caption }}"
                                 class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
                        </div>
                        {% endfor %}
                    </div>
                </div>
                {% endif %}

                <!-- 📅 Программа по дням -->
                {% if days %}
                <div class="bg-white rounded-2xl p-8 shadow-md">
                    <h2 class="text-2xl font-bold text-malachite mb-6">📅 Программа тура</h2>
                    <div class="space-y-6">
                        {% for day in days %}
                        <div class="flex gap-4">
                            <div class="flex-shrink-0 w-12 h-12 flex items-center justify-center rounded-full bg-malachite text-brass font-bold text-lg">
                                {{ day.day_number }}
                            </div>
                            <div class="pt-1">
                                <h3 class="font-bold text-malachite text-lg mb-1">{{ day.title }}</h3>
                                <p class="text-ink/70 leading-relaxed">{{ day.description }}</p>
                            </div>
                        </div>
                        {% endfor %}
                    </div>
                </div>
                {% endif %}

                <!-- 💎 Сравнение категорий -->
                {% if features %}
                <div class="bg-white rounded-2xl p-8 shadow-md">
                    <h2 class="text-2xl font-bold text-malachite mb-6">💎 Сравнение категорий</h2>
                    <div class="overflow-x-auto">
                        <table class="w-full text-center border-collapse">
                            <thead>
                                <tr class="bg-malachite text-white">
                                    <th class="text-left p-4 rounded-tl-xl">Что входит</th>
                                    <th class="p-4">💰 Бюджет</th>
                                    <th class="p-4">⭐ Стандарт</th>
                                    <th class="p-4 rounded-tr-xl">👑 Премиум</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for f in features %}
                                <tr class="border-b border-cream {% cycle '' 'bg-cream/40' %}">
                                    <td class="text-left p-4 font-semibold text-malachite">{{ f.feature }}</td>
                                    <td class="p-4">
                                        {% if f.budget %}
                                            <span class="text-green-600 text-xl">✔</span>
                                            <div class="text-xs text-ink/60 mt-1">{{ f.budget }}</div>
                                        {% else %}
                                            <span class="text-red-400 text-xl">✖</span>
                                        {% endif %}
                                    </td>
                                    <td class="p-4">
                                        {% if f.standard %}
                                            <span class="text-green-600 text-xl">✔</span>
                                            <div class="text-xs text-ink/60 mt-1">{{ f.standard }}</div>
                                        {% else %}
                                            <span class="text-red-400 text-xl">✖</span>
                                        {% endif %}
                                    </td>
                                    <td class="p-4">
                                        {% if f.premium %}
                                            <span class="text-green-600 text-xl">✔</span>
                                            <div class="text-xs text-ink/60 mt-1">{{ f.premium }}</div>
                                        {% else %}
                                            <span class="text-red-400 text-xl">✖</span>
                                        {% endif %}
                                    </td>
                                </tr>
                                {% endfor %}
                            </tbody>
                        </table>
                    </div>
                </div>
                {% endif %}

                <!-- ✅ Включено / Не включено -->
                {% if includes %}
                <div class="bg-white rounded-2xl p-8 shadow-md">
                    <h2 class="text-2xl font-bold text-malachite mb-6">Что входит в стоимость</h2>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                        <div>
                            <h3 class="font-bold text-green-600 mb-3">✔ Включено</h3>
                            <ul class="space-y-2">
                                {% for item in includes %}
                                    {% if item.is_included %}
                                    <li class="flex items-start gap-2 text-ink/70">
                                        <span class="text-green-500 mt-0.5">✔</span> {{ item.text }}
                                    </li>
                                    {% endif %}
                                {% endfor %}
                            </ul>
                        </div>
                        <div>
                            <h3 class="font-bold text-red-500 mb-3">✖ Оплачивается отдельно</h3>
                            <ul class="space-y-2">
                                {% for item in includes %}
                                    {% if not item.is_included %}
                                    <li class="flex items-start gap-2 text-ink/70">
                                        <span class="text-red-400 mt-0.5">✖</span> {{ item.text }}
                                    </li>
                                    {% endif %}
                                {% endfor %}
                            </ul>
                        </div>
                    </div>
                </div>
                {% endif %}

            </div>

            <!-- ===== ПРАВАЯ КОЛОНКА (цены) ===== -->
            <div class="lg:col-span-1">
                <div class="bg-white rounded-2xl p-8 shadow-md sticky top-24">

                    <div class="text-center mb-6">
                        <span class="text-ink/50 text-sm">Стоимость от</span>
                        <div class="text-4xl font-extrabold text-malachite">
                            ${{ tour.price_from|floatformat:0 }}
                        </div>
                    </div>

                    <ul class="space-y-3 mb-6 pb-6 border-b border-cream">
                        <li class="flex items-center gap-3 text-ink/70">
                            <i class="fa-regular fa-clock text-teal w-5"></i>
                            Длительность: <b class="text-malachite">{{ tour.duration_days }} дн.</b>
                        </li>
                        {% if tour.direction %}
                        <li class="flex items-center gap-3 text-ink/70">
                            <i class="fa-solid fa-location-dot text-teal w-5"></i>
                            {{ tour.direction }}
                        </li>
                        {% endif %}
                        {% if tour.season %}
                        <li class="flex items-center gap-3 text-ink/70">
                            <i class="fa-solid fa-calendar text-teal w-5"></i>
                            {{ tour.season }}
                        </li>
                        {% endif %}
                    </ul>

                    {% if prices %}
                    <h3 class="font-bold text-malachite mb-3">Цены по категориям:</h3>
                    <ul class="space-y-2 mb-6 text-sm">
                        {% for p in prices %}
                        <li class="flex justify-between items-center py-2 border-b border-cream">
                            <span class="text-ink/70">{{ p.get_category_display }}
                                <span class="text-ink/40">({{ p.get_season_display }})</span>
                            </span>
                            <b class="text-malachite">${{ p.price|floatformat:0 }}</b>
                        </li>
                        {% endfor %}
                    </ul>
                    {% endif %}

                    <a href="{% url 'contacts:index' %}"
                       class="block text-center px-6 py-4 rounded-full bg-brass text-malachite font-bold text-lg shadow-lg hover:scale-105 transition-transform duration-200">
                        📩 Оставить заявку
                    </a>

                </div>
            </div>

        </div>
    </div>
</section>

{% endblock %}
```

### 📄 `main\templates\main\partials\footer.html`

```html
<!-- main/templates/main/partials/footer.html -->
<footer class="bg-forest-dark text-white">

    <div class="max-w-7xl mx-auto px-6 md:px-12 py-14">

        <!-- Верхняя часть: 4 колонки -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10">

            <!-- Колонка 1: Логотип + описание -->
            <div>
                <h2 class="text-2xl font-extrabold text-[#D4AF37] mb-4">TM IMPRESSIVE</h2>
                <p class="text-sm leading-relaxed text-gray-300">
                    Ваш надёжный партнёр по туризму, бизнес-консалтингу
                    и лингвистическим услугам в Туркменистане.
                </p>
            </div>

            <!-- Колонка 2: Навигация -->
            <div>
                <h3 class="text-lg font-bold mb-4 text-[#D4AF37]">Навигация</h3>
                <ul class="space-y-2 text-sm text-gray-300">
                    <li><a href="/tourism/" class="hover:text-[#D4AF37] transition">Туризм и MICE</a></li>
                    <li><a href="/consulting/" class="hover:text-[#D4AF37] transition">Бизнес-консалтинг</a></li>
                    <li><a href="/linguistics/" class="hover:text-[#D4AF37] transition">Лингвистика и оборудование</a></li>
                    <li><a href="/about/" class="hover:text-[#D4AF37] transition">О компании</a></li>
                    <li><a href="/contacts/" class="hover:text-[#D4AF37] transition">Контакты</a></li>
                </ul>
            </div>

            <!-- Колонка 3: Контакты -->
            <div>
                <h3 class="text-lg font-bold mb-4 text-[#D4AF37]">Контакты</h3>
                <ul class="space-y-2 text-sm text-gray-300">
                    <li>📞 <a href="tel:+99371342731" class="hover:text-[#D4AF37] transition">+993 71 34 27 31</a></li>
                    <li>✉️ <a href="mailto:guzelka9494@gmail.com" class="hover:text-[#D4AF37] transition">guzelka9494@gmail.com</a></li>
                    <li>📍 Туркменистан, Ашхабад</li>
                </ul>
            </div>

            <!-- Колонка 4: Мессенджеры -->
            <div>
                <h3 class="text-lg font-bold mb-4 text-[#D4AF37]">Мы на связи</h3>
                <div class="flex gap-3 mb-3">
                    <!-- WhatsApp -->
                    <a href="https://wa.me/99371342731" target="_blank" title="WhatsApp"
                    class="w-10 h-10 flex items-center justify-center rounded-full bg-white/10 text-white text-lg hover:bg-[#D4AF37] hover:text-[#0B3D2E] transition">
                        <i class="fa-brands fa-whatsapp"></i>
                    </a>
                    <!-- Telegram -->
                    <a href="https://t.me/username" target="_blank" title="Telegram"
                    class="w-10 h-10 flex items-center justify-center rounded-full bg-white/10 text-white text-lg hover:bg-[#D4AF37] hover:text-[#0B3D2E] transition">
                        <i class="fa-brands fa-telegram"></i>
                    </a>
                    <!-- IMO -->
                    <a href="#" title="IMO"
                    class="w-10 h-10 flex items-center justify-center rounded-full bg-white/10 text-white text-lg hover:bg-[#D4AF37] hover:text-[#0B3D2E] transition">
                        <i class="fa-solid fa-comment-dots"></i>
                    </a>
                    <!-- WeChat -->
                    <a href="#" title="WeChat"
                    class="w-10 h-10 flex items-center justify-center rounded-full bg-white/10 text-white text-lg hover:bg-[#D4AF37] hover:text-[#0B3D2E] transition">
                        <i class="fa-brands fa-weixin"></i>
                    </a>
                </div>
                <p class="text-xs text-gray-400">Ответим в течение 1 часа ⭐</p>
            </div>

        </div>

        <!-- Разделитель -->
        <div class="border-t border-white/10 mt-10 pt-6 flex flex-col md:flex-row items-center justify-between gap-4">
            <p class="text-sm text-gray-400">© 2026 TM IMPRESSIVE. Все права защищены.</p>

            <!-- Переключатель языков -->
            <div class="flex items-center gap-3">
                <img src="https://flagcdn.com/w40/ru.png" alt="Русский"
                    class="w-6 h-4 object-cover rounded-sm shadow ring-1 ring-white/20
                            opacity-70 hover:opacity-100 transition-opacity cursor-pointer">
                <img src="https://flagcdn.com/w40/gb.png" alt="Английский"
                    class="w-6 h-4 object-cover rounded-sm shadow ring-1 ring-white/20
                            opacity-70 hover:opacity-100 transition-opacity cursor-pointer">
                <img src="https://flagcdn.com/w40/tm.png" alt="Туркменский"
                    class="w-6 h-4 object-cover rounded-sm shadow ring-1 ring-white/20
                            opacity-70 hover:opacity-100 transition-opacity cursor-pointer">
                <img src="https://flagcdn.com/w40/cn.png" alt="Китайский"
                    class="w-6 h-4 object-cover rounded-sm shadow ring-1 ring-white/20
                            opacity-70 hover:opacity-100 transition-opacity cursor-pointer">
            </div>
        </div>

    </div>
</footer>
```

### 📄 `main\templates\main\partials\header.html`

```html
<!-- main/templates/main/partials/header.html -->

<header class="bg-malachite text-brass w-full shadow">
  <div class="flex items-center justify-between py-4 px-6 md:py-6 md:px-8">

    <!-- Логотип/название -->
    <div class="flex items-center gap-3">
      <span class="text-xl md:text-2xl font-extrabold text-brass uppercase tracking-widest">TM IMPRESSIVE</span>
    </div>

    <!-- 🍔 Кнопка-бургер (только на мобилке, скрыта на десктопе) -->
    <input type="checkbox" id="menu-toggle" class="hidden peer">
    <label for="menu-toggle" class="lg:hidden cursor-pointer text-brass text-3xl select-none">
      ☰
    </label>

    <!-- Меню для ДЕСКТОПА (скрыто на мобилке) -->
    <nav class="hidden lg:flex gap-6 items-center">
      <a href="{% url 'tourism:index' %}" class="font-semibold text-white hover:text-brass transition">Туризм и MICE</a>
      <a href="{% url 'consulting:index' %}" class="font-semibold text-white hover:text-brass transition">Бизнес-консалтинг</a>
      <a href="{% url 'linguistics:index' %}" class="font-semibold text-white hover:text-brass transition">Лингвистика и оборудование</a>
      <a href="{% url 'about:index' %}" class="font-semibold text-white hover:text-brass transition">О компании</a>
      <a href="{% url 'contacts:index' %}" class="font-semibold text-white hover:text-brass transition">Контакты</a>

      <!-- Переключатель языков (десктоп) -->
      <div class="dropdown dropdown-end ml-4 hidden lg:block">
          <div tabindex="0" role="button" class="flex items-center gap-2 px-3 py-1 rounded font-semibold text-brass hover:bg-brass hover:text-malachite transition cursor-pointer">
              <img src="https://flagcdn.com/w40/ru.png" alt="Русский" class="w-6 h-4 object-cover rounded-sm ring-1 ring-white/20">
              RU ▾
          </div>
          <ul tabindex="0" class="dropdown-content menu bg-malachite rounded-box z-10 mt-2 w-32 p-2 shadow">
              <li><a href="#" class="flex items-center gap-2 text-brass hover:bg-brass hover:text-malachite">
                  <img src="https://flagcdn.com/w40/gb.png" alt="English" class="w-6 h-4 object-cover rounded-sm">EN
              </a></li>
              <li><a href="#" class="flex items-center gap-2 text-brass hover:bg-brass hover:text-malachite">
                  <img src="https://flagcdn.com/w40/tm.png" alt="Türkmen" class="w-6 h-4 object-cover rounded-sm">TM
              </a></li>
              <li><a href="#" class="flex items-center gap-2 text-brass hover:bg-brass hover:text-malachite">
                  <img src="https://flagcdn.com/w40/cn.png" alt="中文" class="w-6 h-4 object-cover rounded-sm">ZH
              </a></li>
          </ul>
      </div>
    </nav>

    <!-- 📱 Меню для МОБИЛКИ (раскрывается по клику на бургер) -->
    <nav class="hidden peer-checked:flex lg:hidden flex-col gap-4 absolute top-[64px] left-0 w-full bg-malachite px-6 py-4 shadow-lg z-40">
      <a href="{% url 'tourism:index' %}" class="font-semibold text-white hover:text-brass transition">Туризм и MICE</a>
      <a href="{% url 'consulting:index' %}" class="font-semibold text-white hover:text-brass transition">Бизнес-консалтинг</a>
      <a href="{% url 'linguistics:index' %}" class="font-semibold text-white hover:text-brass transition">Лингвистика и оборудование</a>
      <a href="{% url 'about:index' %}" class="font-semibold text-white hover:text-brass transition">О компании</a>
      <a href="{% url 'contacts:index' %}" class="font-semibold text-white hover:text-brass transition">Контакты</a>

      <!-- Языки (мобилка) — флажки + подпись -->
      <div class="flex gap-4 pt-3 border-t border-brass/30">
          <a href="#" class="flex items-center gap-1.5 font-semibold text-brass hover:text-white">
              <img src="https://flagcdn.com/w40/ru.png" alt="Русский" class="w-6 h-4 object-cover rounded-sm ring-1 ring-white/20">RU
          </a>
          <a href="#" class="flex items-center gap-1.5 font-semibold text-brass hover:text-white">
              <img src="https://flagcdn.com/w40/gb.png" alt="English" class="w-6 h-4 object-cover rounded-sm ring-1 ring-white/20">EN
          </a>
          <a href="#" class="flex items-center gap-1.5 font-semibold text-brass hover:text-white">
              <img src="https://flagcdn.com/w40/tm.png" alt="Türkmen" class="w-6 h-4 object-cover rounded-sm ring-1 ring-white/20">TM
          </a>
          <a href="#" class="flex items-center gap-1.5 font-semibold text-brass hover:text-white">
              <img src="https://flagcdn.com/w40/cn.png" alt="中文" class="w-6 h-4 object-cover rounded-sm ring-1 ring-white/20">ZH
          </a>
      </div>
    </nav>

  </div>
</header>
```

### 📄 `main\templates\main\partials\messenger_panel.html`

```html
<!-- main/templates/main/partials/messenger_panel.html -->
<div x-data="{ open: false }"
     class="fixed bottom-6 right-6 z-50 flex flex-col items-end gap-3">

    <!-- Кнопки мессенджеров -->
    <div class="flex-col gap-3 hidden md:!flex"
     :class="{ '!flex': open }">

        <!-- WhatsApp -->
        <a href="https://wa.me/99371342731" target="_blank" title="WhatsApp"
           class="w-11 h-11 md:w-12 md:h-12 flex items-center justify-center rounded-full bg-[#25D366] text-white text-lg md:text-xl shadow-lg hover:scale-110 transition-transform duration-200">
            <i class="fa-brands fa-whatsapp"></i>
        </a>

        <!-- Telegram -->
        <a href="https://t.me/username" target="_blank" title="Telegram"
           class="w-11 h-11 md:w-12 md:h-12 flex items-center justify-center rounded-full bg-[#0088cc] text-white text-lg md:text-xl shadow-lg hover:scale-110 transition-transform duration-200">
            <i class="fa-brands fa-telegram"></i>
        </a>

        <!-- IMO -->
        <a href="#" title="IMO"
           class="w-11 h-11 md:w-12 md:h-12 flex items-center justify-center rounded-full bg-[#0a90d4] text-white text-lg md:text-xl shadow-lg hover:scale-110 transition-transform duration-200">
            <i class="fa-solid fa-comment-dots"></i>
        </a>

        <!-- WeChat -->
        <a href="#" title="WeChat"
           class="w-11 h-11 md:w-12 md:h-12 flex items-center justify-center rounded-full bg-[#07C160] text-white text-lg md:text-xl shadow-lg hover:scale-110 transition-transform duration-200">
            <i class="fa-brands fa-weixin"></i>
        </a>

        <!-- Email -->
        <a href="mailto:guzelka9494@gmail.com" title="Email"
           class="w-11 h-11 md:w-12 md:h-12 flex items-center justify-center rounded-full bg-[#D4AF37] text-[#0B3D2E] text-lg md:text-xl shadow-lg hover:scale-110 transition-transform duration-200">
            <i class="fa-solid fa-envelope"></i>
        </a>

    </div>

    <!-- Кнопка-переключатель (ТОЛЬКО на мобилке/планшете) -->
    <!-- Кнопка-переключатель с подсказкой -->
    <div class="md:hidden flex items-center gap-2" x-data="{ hint: true }" 
        x-init="setTimeout(() => hint = false, 4000)">

        <!-- Облачко-подсказка -->
        <div x-show="hint && !open" x-transition
            class="bg-white text-[#0B3D2E] text-xs font-medium px-3 py-2 rounded-lg shadow-lg whitespace-nowrap">
            Напишите нам 👋
        </div>

        <!-- Пузырь -->
        <button @click="open = !open; hint = false" title="Связаться"
            class="w-14 h-14 flex items-center justify-center rounded-full bg-[#0B3D2E] text-white text-2xl shadow-xl hover:scale-110 transition-transform duration-200">
            <span x-show="!open">&#128172;</span>
        </button>
    </div>

    <!-- Подпись (только на десктопе) -->
    <div class="hidden md:block bg-[#0B3D2E] text-white text-xs px-3 py-1.5 rounded-full shadow-lg">
        Ответим в течение 1 часа ⭐
    </div>

</div>
```
