# 📦 Код проекта TM IMPRESSIVE

> Собрано: 29.08.2026 14:00
> Всего файлов: 106
> Размер каждой части: ~99 КБ

## 🌳 Структура проекта

```
tmimpressive/
├── .env
├── .gitignore
├── collect_code_split.py
├── manage.py
├── requirements.txt
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
    ├── knowledge.py
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
    ├── site_content.py
    ├── tests.py
    ├── urls.py
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
        ├── case_tags.py
        ├── search_extras.py
        ├── .gitignore
        ├── package.json
        ├── postcss.config.js
        ├── __init__.py
        ├── tour_filters.py
            ├── index.html
            ├── detail.html
            ├── index.html
            ├── list.html
            ├── index.html
            ├── index.html
            ├── index.html
            ├── base.html
            ├── home.html
            ├── results.html
            ├── styles.css
            ├── _catalog.html
            ├── _filters.html
            ├── _tours_grid.html
            ├── index.html
            ├── tour_detail.html
                ├── assistant_widget.html
                ├── footer.html
                ├── header.html
                ├── messenger_panel.html
                ├── desktop.ini
```

---

## 📄 Содержимое файлов

### 📄 `search\templates\search\results.html`

```html
{% extends "main/base.html" %}
{% load search_extras %}

{% block title %}
    {% if query %}Поиск: {{ query }}{% else %}Поиск по сайту{% endif %} — TM IMPRESSIVE
{% endblock %}

{% block content %}

<!-- ================= ПОИСКОВАЯ ШАПКА ================= -->
<section class="bg-malachite text-white py-14 md:py-20">
    <div class="max-w-4xl mx-auto px-4 text-center">
        <h1 class="text-3xl md:text-5xl font-extrabold mb-6">Поиск по сайту</h1>

        <form action="{% url 'search:index' %}" method="get" role="search"
              class="flex gap-2 max-w-2xl mx-auto">
            <label for="q" class="sr-only">Поисковый запрос</label>
            <input id="q" type="search" name="q" value="{{ query }}" autofocus
                   placeholder="Тур, город, услуга…"
                   class="flex-1 px-5 py-3.5 rounded-full text-ink bg-white
                          outline-none focus:ring-2 focus:ring-brass">
            <button type="submit"
                    class="px-6 py-3.5 rounded-full bg-brass text-malachite font-bold
                           hover:scale-105 transition-transform">
                <i class="fa-solid fa-magnifying-glass"></i>
                <span class="hidden sm:inline ml-1">Найти</span>
            </button>
        </form>

        {% if query and not too_short %}
        <p class="mt-5 text-cream/80">
            {% if has_results %}
                Найдено результатов: <b class="text-brass">{{ counts.all }}</b>
                по запросу «{{ query }}»
            {% else %}
                Ничего не найдено по запросу «{{ query }}»
            {% endif %}
        </p>
        {% endif %}
    </div>
</section>

<!-- ================= РАЗДЕЛЫ ================= -->
{% if has_results %}
<section class="bg-white border-b border-cream sticky top-0 z-20">
    <div class="max-w-6xl mx-auto px-4 flex gap-2 overflow-x-auto py-3">
        {% with base=query|urlencode %}
        <a href="?q={{ base }}"
           class="shrink-0 px-4 py-2 rounded-full text-sm font-bold transition
           {% if section == 'all' %}bg-malachite text-white{% else %}text-ink/60 hover:bg-cream{% endif %}">
            Всё <span class="opacity-60">{{ counts.all }}</span>
        </a>
        {% if counts.tours %}
        <a href="?q={{ base }}&section=tours"
           class="shrink-0 px-4 py-2 rounded-full text-sm font-bold transition
           {% if section == 'tours' %}bg-malachite text-white{% else %}text-ink/60 hover:bg-cream{% endif %}">
            <i class="fa-solid fa-plane-departure"></i>
            Туры <span class="opacity-60">{{ counts.tours }}</span>
        </a>
        {% endif %}
        {% if counts.cases %}
        <a href="?q={{ base }}&section=cases"
           class="shrink-0 px-4 py-2 rounded-full text-sm font-bold transition
           {% if section == 'cases' %}bg-malachite text-white{% else %}text-ink/60 hover:bg-cream{% endif %}">
            <i class="fa-solid fa-trophy"></i>
            Кейсы <span class="opacity-60">{{ counts.cases }}</span>
        </a>
        {% endif %}
        {% if counts.pages %}
        <a href="?q={{ base }}&section=pages"
           class="shrink-0 px-4 py-2 rounded-full text-sm font-bold transition
           {% if section == 'pages' %}bg-malachite text-white{% else %}text-ink/60 hover:bg-cream{% endif %}">
            <i class="fa-solid fa-file-lines"></i>
            Страницы <span class="opacity-60">{{ counts.pages }}</span>
        </a>
        {% endif %}
        {% endwith %}
    </div>
</section>
{% endif %}

<!-- ================= РЕЗУЛЬТАТЫ ================= -->
<section class="py-12 bg-cream min-h-[50vh]">
    <div class="max-w-6xl mx-auto px-4 space-y-12">

        {# ---------- запрос слишком короткий ---------- #}
        {% if too_short %}
        <div class="text-center py-16 bg-white rounded-2xl">
            <i class="fa-solid fa-keyboard text-ink/20 text-5xl mb-4"></i>
            <p class="text-ink/60 text-lg">
                Введите минимум {{ min_length }} символа для поиска
            </p>
        </div>

        {# ---------- страница открыта без запроса ---------- #}
        {% elif not query %}
        <div class="text-center py-16 bg-white rounded-2xl">
            <i class="fa-solid fa-magnifying-glass text-brass/40 text-5xl mb-4"></i>
            <p class="text-ink/60 text-lg mb-6">
                Что вы ищете? Введите запрос в поле выше
            </p>
            <div class="flex flex-wrap gap-2 justify-center">
                {% for hint in "Мерв,Ашхабад,перевод,виза,MICE"|slice:":0" %}{% endfor %}
                <a href="?q=Мерв" class="px-4 py-2 rounded-full bg-cream text-teal text-sm font-semibold hover:bg-teal hover:text-white transition">Мерв</a>
                <a href="?q=Ашхабад" class="px-4 py-2 rounded-full bg-cream text-teal text-sm font-semibold hover:bg-teal hover:text-white transition">Ашхабад</a>
                <a href="?q=перевод" class="px-4 py-2 rounded-full bg-cream text-teal text-sm font-semibold hover:bg-teal hover:text-white transition">перевод</a>
                <a href="?q=виза" class="px-4 py-2 rounded-full bg-cream text-teal text-sm font-semibold hover:bg-teal hover:text-white transition">виза</a>
            </div>
        </div>

        {# ---------- ничего не найдено ---------- #}
        {% elif not has_results %}
        <div class="text-center py-16 bg-white rounded-2xl">
            <i class="fa-solid fa-face-frown text-ink/20 text-5xl mb-4"></i>
            <p class="text-ink/70 text-lg font-semibold mb-2">Ничего не найдено</p>
            <p class="text-ink/50 mb-8">
                Попробуйте другой запрос или напишите нам — подберём вручную
            </p>
            <div class="flex flex-wrap gap-3 justify-center">
                <a href="{% url 'tourism:index' %}"
                   class="px-6 py-3 rounded-full bg-malachite text-white font-bold hover:bg-teal transition">
                    🌍 Каталог туров
                </a>
                <a href="{% url 'contacts:index' %}"
                   class="px-6 py-3 rounded-full bg-brass text-malachite font-bold hover:scale-105 transition-transform">
                    📩 Написать нам
                </a>
            </div>
        </div>
        {% endif %}

        {# ---------- 🌍 ТУРЫ ---------- #}
        {% if tours and section == 'all' or tours and section == 'tours' %}
        <div>
            <h2 class="text-xl font-bold text-malachite mb-5">
                <i class="fa-solid fa-plane-departure text-brass"></i>
                Туры <span class="text-ink/40 font-normal">({{ counts.tours }})</span>
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
                {% for tour in tours %}
                <a href="{% url 'tourism:tour_detail' tour.slug %}"
                   class="group bg-white rounded-2xl p-5 shadow-sm hover:shadow-lg
                          flex gap-4 transition-shadow">
                    <div class="w-24 h-24 shrink-0 rounded-xl overflow-hidden
                                bg-gradient-to-br from-malachite to-teal">
                        {% if tour.main_image %}
                            <img src="{{ tour.main_image.url }}" alt="{{ tour.title }}"
                                 class="w-full h-full object-cover">
                        {% else %}
                            <div class="w-full h-full flex items-center justify-center">
                                <i class="fa-solid fa-mountain-sun text-brass/60 text-2xl"></i>
                            </div>
                        {% endif %}
                    </div>
                    <div class="min-w-0">
                        <h3 class="font-bold text-malachite group-hover:text-teal transition mb-1">
                            {{ tour.title|highlight:query }}
                        </h3>
                        {% if tour.direction %}
                        <p class="text-teal text-xs font-semibold mb-1">
                            <i class="fa-solid fa-location-dot"></i>
                            {{ tour.direction|highlight:query }}
                        </p>
                        {% endif %}
                        <p class="text-ink/60 text-sm mb-2">
                            {{ tour.short_description|truncatewords:16|highlight:query }}
                        </p>
                        <div class="flex items-center gap-3 text-xs">
                            <span class="text-ink/50">
                                <i class="fa-regular fa-clock"></i> {{ tour.duration_days }} дн.
                            </span>
                            <span class="text-malachite font-bold">
                                от ${{ tour.price_from|floatformat:0 }}
                            </span>
                        </div>
                    </div>
                </a>
                {% endfor %}
            </div>
        </div>
        {% endif %}

        {# ---------- 🏆 КЕЙСЫ ---------- #}
        {% if cases and section == 'all' or cases and section == 'cases' %}
        <div>
            <h2 class="text-xl font-bold text-malachite mb-5">
                <i class="fa-solid fa-trophy text-brass"></i>
                Кейсы <span class="text-ink/40 font-normal">({{ counts.cases }})</span>
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
                {% for case in cases %}
                <div class="bg-white rounded-2xl p-5 shadow-sm hover:shadow-lg transition-shadow">
                    {% if case.client %}
                    <span class="text-ink/40 text-xs uppercase tracking-wider">
                        {{ case.client|highlight:query }}
                    </span>
                    {% endif %}
                    <h3 class="font-bold text-malachite mb-2 mt-1">
                        {{ case.title|highlight:query }}
                    </h3>
                    <p class="text-ink/60 text-sm mb-3">
                        {{ case.short_description|truncatewords:20|highlight:query }}
                    </p>
                    {% if case.result %}
                    <p class="text-sm text-malachite font-semibold pt-3 border-t border-cream">
                        <i class="fa-solid fa-circle-check text-teal"></i>
                        {{ case.result|highlight:query }}
                    </p>
                    {% endif %}
                    <a href="{% url 'cases:list' %}"
                       class="inline-block mt-3 text-teal text-sm font-bold hover:underline">
                        Все кейсы <i class="fa-solid fa-arrow-right"></i>
                    </a>
                </div>
                {% endfor %}
            </div>
        </div>
        {% endif %}

        {# ---------- 📄 СТРАНИЦЫ ---------- #}
        {% if pages and section == 'all' or pages and section == 'pages' %}
        <div>
            <h2 class="text-xl font-bold text-malachite mb-5">
                <i class="fa-solid fa-file-lines text-brass"></i>
                Страницы сайта <span class="text-ink/40 font-normal">({{ counts.pages }})</span>
            </h2>
            <div class="space-y-3">
                {% for page in pages %}
                <a href="{% url page.url_name %}"
                   class="group flex items-start gap-4 bg-white rounded-2xl p-5
                          shadow-sm hover:shadow-lg transition-shadow">
                    <div class="w-11 h-11 shrink-0 rounded-xl bg-malachite text-brass
                                flex items-center justify-center">
                        <i class="fa-solid {{ page.icon }}"></i>
                    </div>
                    <div>
                        <h3 class="font-bold text-malachite group-hover:text-teal transition">
                            {{ page.title|highlight:query }}
                        </h3>
                        <p class="text-ink/60 text-sm">
                            {{ page.description|highlight:query }}
                        </p>
                    </div>
                </a>
                {% endfor %}
            </div>
        </div>
        {% endif %}

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
   /* --color-malachite: #0B3D2E; был */
      /*--color-malachite: #1a7c63;    /* Светлый зелёный, но не кричащий */
     /* --color-malachite: #1a6b5a;    /* Светлый, но роскошный зелёный */
      --color-malachite: #0f6b52;    /* Роскошный изумрудно-зелёный */

    /* 🟡 Латунь — акценты, кнопки, текст на тёмном фоне */
   /* --color-brass: #D4AF37; был */
     /* --color-brass: #d4a955;         /* Слегка светлее текущего */
    /* --color-brass: #E5C158;         /* Светлая латунь, чуть светлее */
     --color-brass: #DDB74E;         /* Светлая матовая латунь */

    /* 🟢 Бирюзовый — подзаголовки */
    /*--color-teal: #3D7A6F; был */
    /*--color-teal: #059669;          /* Более яркий бирюзовый */
    /*--color-teal: #2a9077;          /* Дополняющий зелёный */
    --color-teal: #1a8070;          /* Премиум бирюза-зелень */

    /* ⚫ Тёмно-серый — основной текст */
    --color-ink: #2C2C2C;

    /* 🤍 Кремовый — фон страницы */
    --color-cream: #F8F5F0;

    /* \(тёмный для футера) */
    /*--color-forest-dark: #082419;  */
     /* 🌑 Тёмный зелёный для футера — премиум элегантный */
    --color-forest-dark: #0a4a37;  

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

### 📄 `tourism\templates\tourism\_filters.html`

```html
{# ============================================================ #}
{# 📁 tourism/templates/tourism/_filters.html                    #}
{# 🆕 НОВЫЙ ФАЙЛ — сайдбар со ВСЕМИ 6 фильтрами                  #}
{# ============================================================ #}
{% load tour_filters %}

<div class="bg-white rounded-2xl p-6 shadow-md lg:sticky lg:top-24 lg:max-h-[calc(100vh-7rem)] lg:overflow-y-auto">

    <div class="flex items-center justify-between mb-5">
        <h2 class="text-lg font-bold text-malachite">
            <i class="fa-solid fa-sliders text-brass"></i> Фильтры
        </h2>
        {% if has_filters %}
        <a href="{% url 'tourism:index' %}"
           class="filter-link text-xs font-semibold text-ink/50 hover:text-malachite transition">
            <i class="fa-solid fa-rotate-left"></i> Сбросить
        </a>
        {% endif %}
    </div>

    {# ============ 🏷️ ТИП ТУРИЗМА (малахит) ============ #}
    <h3 class="text-xs font-bold text-ink/40 uppercase tracking-wider mb-2">Тип туризма</h3>
    <ul class="space-y-1 mb-6">
        <li>
            <a href="{% filter_url type='' %}"
               class="filter-link flex items-center gap-3 px-3 py-2 rounded-xl text-sm font-semibold transition
               {% if not selected.type %}bg-malachite text-white{% else %}text-ink/70 hover:bg-cream{% endif %}">
                <i class="fa-solid fa-globe w-4 text-center"></i> Все
            </a>
        </li>
        {% for code, name, icon in types_with_icons %}
        <li>
            <a href="{% filter_url type=code %}"
               class="filter-link flex items-center gap-3 px-3 py-2 rounded-xl text-sm font-semibold transition
               {% if selected.type == code %}bg-malachite text-white{% else %}text-ink/70 hover:bg-cream{% endif %}">
                <i class="fa-solid {{ icon }} w-4 text-center"></i> {{ name }}
            </a>
        </li>
        {% endfor %}
    </ul>

    {# ============ 💎 КАТЕГОРИЯ (латунь) ============ #}
    <h3 class="text-xs font-bold text-ink/40 uppercase tracking-wider mb-2">Категория</h3>
    <ul class="space-y-1 mb-6">
        <li>
            <a href="{% filter_url category='' %}"
               class="filter-link flex items-center gap-3 px-3 py-2 rounded-xl text-sm font-semibold transition
               {% if not selected.category %}bg-brass text-malachite{% else %}text-ink/70 hover:bg-cream{% endif %}">
                <i class="fa-solid fa-globe w-4 text-center"></i> Все
            </a>
        </li>
        {% for code, name, icon in categories_with_icons %}
        <li>
            <a href="{% filter_url category=code %}"
               class="filter-link flex items-center gap-3 px-3 py-2 rounded-xl text-sm font-semibold transition
               {% if selected.category == code %}bg-brass text-malachite{% else %}text-ink/70 hover:bg-cream{% endif %}">
                <i class="fa-solid {{ icon }} w-4 text-center"></i> {{ name }}
            </a>
        </li>
        {% endfor %}
    </ul>

    {# ============ 📍 НАПРАВЛЕНИЕ (бирюза) ============ #}
    {% if directions %}
    <h3 class="text-xs font-bold text-ink/40 uppercase tracking-wider mb-2">Направление</h3>
    <ul class="space-y-1 mb-6">
        <li>
            <a href="{% filter_url direction='' %}"
               class="filter-link flex items-center gap-3 px-3 py-2 rounded-xl text-sm font-semibold transition
               {% if not selected.direction %}bg-teal text-white{% else %}text-ink/70 hover:bg-cream{% endif %}">
                <i class="fa-solid fa-globe w-4 text-center"></i> Все
            </a>
        </li>
        {% for d in directions %}
        <li>
            <a href="{% filter_url direction=d %}"
               class="filter-link flex items-center gap-3 px-3 py-2 rounded-xl text-sm font-semibold transition
               {% if selected.direction == d %}bg-teal text-white{% else %}text-ink/70 hover:bg-cream{% endif %}">
                <i class="fa-solid fa-location-dot w-4 text-center"></i> {{ d }}
            </a>
        </li>
        {% endfor %}
    </ul>
    {% endif %}

    {# ============ ⏱️ ДЛИТЕЛЬНОСТЬ (бирюза) ============ #}
    <h3 class="text-xs font-bold text-ink/40 uppercase tracking-wider mb-2">Длительность</h3>
    <ul class="space-y-1 mb-6">
        <li>
            <a href="{% filter_url duration='' %}"
               class="filter-link flex items-center gap-3 px-3 py-2 rounded-xl text-sm font-semibold transition
               {% if not selected.duration %}bg-teal text-white{% else %}text-ink/70 hover:bg-cream{% endif %}">
                <i class="fa-solid fa-globe w-4 text-center"></i> Любая
            </a>
        </li>
        {% for code, name, icon in duration_choices %}
        <li>
            <a href="{% filter_url duration=code %}"
               class="filter-link flex items-center gap-3 px-3 py-2 rounded-xl text-sm font-semibold transition
               {% if selected.duration == code %}bg-teal text-white{% else %}text-ink/70 hover:bg-cream{% endif %}">
                <i class="fa-solid {{ icon }} w-4 text-center"></i> {{ name }}
            </a>
        </li>
        {% endfor %}
    </ul>

    {# ============ 🗓️ СЕЗОН (бирюза) ============ #}
    <h3 class="text-xs font-bold text-ink/40 uppercase tracking-wider mb-2">Сезон</h3>
    <ul class="space-y-1 mb-6">
        <li>
            <a href="{% filter_url season='' %}"
               class="filter-link flex items-center gap-3 px-3 py-2 rounded-xl text-sm font-semibold transition
               {% if not selected.season %}bg-teal text-white{% else %}text-ink/70 hover:bg-cream{% endif %}">
                <i class="fa-solid fa-globe w-4 text-center"></i> Любой
            </a>
        </li>
        {% for code, name, icon in season_choices %}
        <li>
            <a href="{% filter_url season=code %}"
               class="filter-link flex items-center gap-3 px-3 py-2 rounded-xl text-sm font-semibold transition
               {% if selected.season == code %}bg-teal text-white{% else %}text-ink/70 hover:bg-cream{% endif %}">
                <i class="fa-solid {{ icon }} w-4 text-center"></i> {{ name }}
            </a>
        </li>
        {% endfor %}
    </ul>

    {# ============ 💵 ЦЕНА (бирюза) ============ #}
    <h3 class="text-xs font-bold text-ink/40 uppercase tracking-wider mb-2">Цена</h3>
    <ul class="space-y-1">
        <li>
            <a href="{% filter_url price='' %}"
               class="filter-link flex items-center gap-3 px-3 py-2 rounded-xl text-sm font-semibold transition
               {% if not selected.price %}bg-teal text-white{% else %}text-ink/70 hover:bg-cream{% endif %}">
                <i class="fa-solid fa-globe w-4 text-center"></i> Любая
            </a>
        </li>
        {% for code, name, icon in price_choices %}
        <li>
            <a href="{% filter_url price=code %}"
               class="filter-link flex items-center gap-3 px-3 py-2 rounded-xl text-sm font-semibold transition
               {% if selected.price == code %}bg-teal text-white{% else %}text-ink/70 hover:bg-cream{% endif %}">
                <i class="fa-solid {{ icon }} w-4 text-center"></i> {{ name }}
            </a>
        </li>
        {% endfor %}
    </ul>

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
<section class="relative  bg-malachite text-white overflow-hidden">
    <img src="{% static 'images/banners/tourism_hero.jpg' %}" alt=""
         class="absolute inset-0 w-full h-full object-cover object-right opacity-90 pointer-events-none">
    <div class="relative max-w-8xl mx-auto px-10 py-24 ml-2 md:py-32">
        <div class="max-w-4xl ">
            <span class="inline-block px-10 py-1 mb-4 rounded-full bg-brass/20 text-brass text-sm font-semibold tracking-wide">
                 <i class="fa-solid fa-mountain-sun mr-2"></i>Туризм и MICE
            </span>
            <h1 class="text-4xl md:text-6xl font-bold mb-6 leading-tight">
                Откройте<br>Туркменистан
            </h1>
            <p class="text-lg md:text-xl text-cream/90 mb-6">
                 Пустыня Каракумы, горы Копетдаг, Каспийское море </br>и древний Шёлковый путь — в одном путешествии.
            </p>
            <
            <a href="{% url 'contacts:index' %}"
               class="inline-block px-8 py-4 rounded-full bg-brass text-malachite font-bold text-lg shadow-xl hover:scale-105 transition-transform duration-200">
                Подобрать тур
            </a>
        </div>
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

### 📄 `main\templates\main\partials\assistant_widget.html`

```html
{# 📁 main/templates/main/partials/assistant_widget.html #}
{# 🤖 Виртуальный ассистент — плавающий чат в правом нижнем углу #}

<div id="tm-assistant" class="fixed bottom-6 right-6 z-50">

    {# ---------- Кнопка открытия ---------- #}
    <button id="tma-toggle" type="button" aria-label="Открыть чат с ассистентом"
            class="w-16 h-16 flex items-center justify-center rounded-full
                   bg-brass text-malachite text-2xl shadow-xl
                   hover:scale-110 transition-transform duration-200">
        <i class="fa-solid fa-robot"></i>
    </button>

    {# ---------- Окно чата ---------- #}
    <div id="tma-panel"
         class="hidden flex-col absolute bottom-20 right-0
                w-[90vw] max-w-sm h-[70vh] max-h-[560px]
                bg-white rounded-2xl shadow-2xl overflow-hidden">

        <!-- Шапка -->
        <div class="bg-malachite text-white px-5 py-4 flex items-center gap-3 shrink-0">
            <div class="w-10 h-10 rounded-full bg-brass text-malachite flex items-center justify-center text-lg">
                <i class="fa-solid fa-robot"></i>
            </div>
            <div class="flex-1">
                <p class="font-bold leading-tight">Виртуальный ассистент</p>
                <p class="text-xs text-cream/70 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-green-400 inline-block"></span>
                    на связи 24/7
                </p>
            </div>
            <button id="tma-close" type="button" aria-label="Закрыть"
                    class="text-white/70 hover:text-white text-xl leading-none">&times;</button>
        </div>

        <!-- Лента сообщений -->
        <div id="tma-messages" class="flex-1 overflow-y-auto px-4 py-4 space-y-3 bg-cream"></div>

        <!-- Кнопки-подсказки -->
        <div id="tma-chips" class="px-4 pb-2 flex flex-wrap gap-2 bg-cream shrink-0"></div>

        <!-- Поле ввода -->
        <div class="p-3 border-t border-cream bg-white flex gap-2 shrink-0">
            <input id="tma-input" type="text" autocomplete="off"
                   placeholder="Напишите вопрос…"
                   class="flex-1 px-4 py-2.5 rounded-full bg-cream text-ink text-sm
                          outline-none focus:ring-2 focus:ring-brass">
            <button id="tma-send" type="button" aria-label="Отправить"
                    class="w-11 h-11 shrink-0 rounded-full bg-malachite text-white
                           hover:bg-teal transition-colors">
                <i class="fa-solid fa-paper-plane"></i>
            </button>
        </div>
    </div>

    {% csrf_token %}
</div>

<script>
(function () {
    const root     = document.getElementById('tm-assistant');
    const toggle   = document.getElementById('tma-toggle');
    const panel    = document.getElementById('tma-panel');
    const closeBtn = document.getElementById('tma-close');
    const list     = document.getElementById('tma-messages');
    const chipsBox = document.getElementById('tma-chips');
    const input    = document.getElementById('tma-input');
    const sendBtn  = document.getElementById('tma-send');

    const csrf = root.querySelector('[name=csrfmiddlewaretoken]').value;
    let started = false;

    // ---------- показать сообщение ----------
    function addMessage(html, who) {
        const row = document.createElement('div');
        row.className = 'flex ' + (who === 'user' ? 'justify-end' : 'justify-start');

        const bubble = document.createElement('div');
        bubble.className = who === 'user'
            ? 'max-w-[80%] px-4 py-2.5 rounded-2xl rounded-br-sm bg-malachite text-white text-sm leading-relaxed'
            : 'max-w-[85%] px-4 py-2.5 rounded-2xl rounded-bl-sm bg-white text-ink text-sm leading-relaxed shadow-sm';
        bubble.innerHTML = html.replace(/\n/g, '<br>');

        row.appendChild(bubble);
        list.appendChild(row);
        list.scrollTop = list.scrollHeight;
        return row;
    }

    // ---------- кнопка-ссылка под ответом ----------
    function addLink(link) {
        const row = document.createElement('div');
        row.className = 'flex justify-start';
        row.innerHTML = '<a href="' + link.url + '" class="px-4 py-2 rounded-full bg-brass ' +
                        'text-malachite text-sm font-bold hover:scale-105 transition-transform">' +
                        link.text + '</a>';
        list.appendChild(row);
        list.scrollTop = list.scrollHeight;
    }

    // ---------- подсказки ----------
    function renderChips(chips) {
        chipsBox.innerHTML = '';
        (chips || []).forEach(function (text) {
            const chip = document.createElement('button');
            chip.type = 'button';
            chip.textContent = text;
            chip.className = 'px-3 py-1.5 rounded-full border border-teal/40 text-teal ' +
                             'text-xs font-semibold hover:bg-teal hover:text-white transition';
            chip.addEventListener('click', function () { send(text); });
            chipsBox.appendChild(chip);
        });
    }

    // ---------- «печатает…» ----------
    function showTyping() {
        return addMessage('<span class="text-ink/40">печатает…</span>', 'bot');
    }

    // ---------- отправка вопроса ----------
    function send(question) {
        if (question) { addMessage(question, 'user'); }
        input.value = '';
        chipsBox.innerHTML = '';
        const typing = showTyping();

        fetch("{% url 'assistant:ask' %}", {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrf },
            body: JSON.stringify({ question: question || '' })
        })
        .then(function (r) { return r.json(); })
        .then(function (data) {
            typing.remove();
            addMessage(data.answer, 'bot');
            if (data.link) { addLink(data.link); }
            renderChips(data.chips);
        })
        .catch(function () {
            typing.remove();
            addMessage('Связь пропала 😔 Попробуйте ещё раз или напишите нам в WhatsApp.', 'bot');
        });
    }

    // ---------- открыть / закрыть ----------
    function openChat() {
        panel.classList.remove('hidden');
        panel.classList.add('flex');
        toggle.innerHTML = '<i class="fa-solid fa-xmark"></i>';
        if (!started) { started = true; send(''); }   // приветствие
        input.focus();
    }
    function closeChat() {
        panel.classList.add('hidden');
        panel.classList.remove('flex');
        toggle.innerHTML = '<i class="fa-solid fa-robot"></i>';
    }

    toggle.addEventListener('click', function () {
        panel.classList.contains('hidden') ? openChat() : closeChat();
    });
    closeBtn.addEventListener('click', closeChat);

    sendBtn.addEventListener('click', function () {
        const q = input.value.trim();
        if (q) { send(q); }
    });
    input.addEventListener('keydown', function (e) {
        if (e.key === 'Enter') {
            const q = input.value.trim();
            if (q) { send(q); }
        }
    });
})();
</script>
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
                    <li>📞 <a href="tel:+99363878057" class="hover:text-[#D4AF37] transition">+993 63 87 80 67</a></li>
                    <li>✉️ <a href="mailto:guzelka9494@gmail.com" class="hover:text-[#D4AF37] transition">info@tmimpressive.tm</a></li>
                    <li>📍 Туркменистан, Ашхабад, Арчабиль шаёлы</li>
                </ul>
            </div>

            <!-- Колонка 4: Мессенджеры -->
            <div>
                <h3 class="text-lg font-bold mb-4 text-[#D4AF37]">Мы на связи</h3>
                <div class="flex gap-3 mb-3">
                    <!-- WhatsApp -->
                    <a href="https://wa.me/99363878057" target="_blank" title="WhatsApp"
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
               <!-- <p class="text-xs text-gray-400">Ответим в течение 1 часа ⭐</p>-->
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

    <!-- 🏠 Логотип — кликабельный, ведёт на главную -->
    <a href="{% url 'home' %}"
       class="flex items-center gap-3 group"
       aria-label="TM IMPRESSIVE — на главную">
      <span class="text-xl md:text-2xl font-extrabold text-brass uppercase tracking-widest
                   group-hover:text-white transition-colors duration-200">
        TM IMPRESSIVE
      </span>
    </a>

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

              <!-- 🔍 Поиск (десктоп) — ИСПРАВЛЕННЫЙ -->
      <form action="{% url 'search:index' %}" method="get" role="search"
            class="relative flex items-center">
        <label for="header-q" class="sr-only">Поиск по сайту</label>
        <input id="header-q" type="search" name="q" placeholder="Поиск…"
               class="w-32 focus:w-56 pl-10 pr-3 py-2 rounded-full text-sm
                      bg-white/10 text-white placeholder-white/50
                      outline-none focus:bg-white focus:text-ink
                      transition-all duration-300">
        <i class="fa-solid fa-magnifying-glass absolute left-3 top-1/2 -translate-y-1/2
                  text-brass text-sm pointer-events-none"></i>
      </form>

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
      
              <!-- 🔍 Поиск (мобилка) -->
      <form action="{% url 'search:index' %}" method="get" role="search" class="flex gap-2">
        <label for="header-q-mobile" class="sr-only">Поиск по сайту</label>
        <input id="header-q-mobile" type="search" name="q" placeholder="Поиск по сайту…" class="flex-1 px-4 py-2 rounded-full text-sm bg-white text-ink outline-none">
        <button type="submit"  class="px-4 py-2 rounded-full bg-brass text-malachite font-bold">
          <i class="fa-solid fa-magnifying-glass"></i>
        </button>
      </form>
      
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
{% load static %}

<div x-data="{ open: false, wechatModal: false, imoModal: false }"
     class="fixed bottom-28 right-6 z-40 flex flex-col items-end gap-3">

    <!-- Кнопки мессенджеров -->
    <div class="flex-col gap-2 hidden md:!flex"
         :class="{ '!flex': open }">

        <!-- WhatsApp -->
        <a href="https://wa.me/99371342731" target="_blank" title="WhatsApp"
           class="w-12 h-12 flex items-center justify-center rounded-full bg-green-500 text-white text-xl hover:scale-110 transition-transform shadow-lg">
            <i class="fa-brands fa-whatsapp"></i>
        </a>

        <!-- Telegram -->
        <a href="https://t.me/tmimpressive" target="_blank" title="Telegram"
           class="w-12 h-12 flex items-center justify-center rounded-full bg-blue-500 text-white text-xl hover:scale-110 transition-transform shadow-lg">
            <i class="fa-brands fa-telegram"></i>
        </a>

        <!-- WeChat — QR код в попапе -->
        <button @click="wechatModal = true" title="WeChat"
           class="w-12 h-12 flex items-center justify-center rounded-full bg-green-600 text-white text-xl hover:scale-110 transition-transform shadow-lg">
            <i class="fa-brands fa-weixin"></i>
        </button>

        <!-- IMO — логотип локально + QR код -->
            <button @click="imoModal = true" title="IMO"
            class="w-12 h-12 flex items-center justify-center rounded-full bg-white text-white text-xl hover:scale-110 transition-transform shadow-lg">
                <img src="{% static 'images/logos/imo_logo.png' %}" 
                    alt="IMO" class="w-6 h-6 object-contain">
            </button>

        <!-- Email -->
        <a href="mailto:guzelka9494@gmail.com" title="Email"
           class="w-12 h-12 flex items-center justify-center rounded-full bg-yellow-500 text-malachite text-xl hover:scale-110 transition-transform shadow-lg">
            <i class="fa-solid fa-envelope"></i>
        </a>

    </div>

    <!-- 📱 МОДАЛЬНОЕ ОКНО WeChat QR CODE -->
    <div x-show="wechatModal" 
         @click.outside="wechatModal = false"
         class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4"
         style="display: none;">
        
        <div class="bg-white rounded-2xl p-8 shadow-2xl max-w-sm w-full animate-in fade-in zoom-in-95 duration-300">
            
            <!-- Заголовок -->
            <div class="flex items-center justify-between mb-6">
                <h3 class="text-2xl font-bold text-malachite flex items-center gap-2">
                    <i class="fa-brands fa-weixin text-green-600"></i>
                    WeChat
                </h3>
                <button @click="wechatModal = false" class="text-ink/50 hover:text-ink text-2xl">
                    ✕
                </button>
            </div>

            <!-- QR код -->
            <div class="bg-cream rounded-xl p-6 mb-6 text-center">
                <img src="https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=https://web.wechat.com" 
                     alt="WeChat QR Code" class="w-full h-auto rounded-lg">
            </div>

            <!-- Инструкция -->
            <div class="space-y-3 mb-6">
                <p class="text-ink/70 text-sm">
                    <strong>Как добавить нас в WeChat:</strong>
                </p>
                <ol class="text-ink/60 text-sm space-y-2 list-decimal list-inside">
                    <li>Откройте WeChat на телефоне</li>
                    <li>Нажмите <strong>+</strong> → <strong>Scan QR Code</strong></li>
                    <li>Отсканируйте этот код</li>
                    <li>Пишите нам! 😊</li>
                </ol>
            </div>

            <!-- Кнопка закрытия -->
            <button @click="wechatModal = false"
                    class="w-full px-6 py-3 rounded-full bg-malachite text-white font-bold hover:bg-teal transition">
                Закрыть
            </button>

        </div>
    </div>

    <!-- 📱 МОДАЛЬНОЕ ОКНО IMO QR CODE -->
    <div x-show="imoModal" 
         @click.outside="imoModal = false"
         class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4"
         style="display: none;">
        
        <div class="bg-white rounded-2xl p-8 shadow-2xl max-w-sm w-full animate-in fade-in zoom-in-95 duration-300">
            
            <!-- Заголовок -->
            <div class="flex items-center justify-between mb-6">
                <h3 class="text-2xl font-bold text-blue-400 flex items-center gap-2">
                    <img src="{% static 'images/logos/imo_logo.png' %}" 
                         alt="IMO" class="w-8 h-8 rounded-full">
                    IMO
                </h3>
                <button @click="imoModal = false" class="text-ink/50 hover:text-ink text-2xl">
                    ✕
                </button>
            </div>

            <!-- QR код -->
            <div class="bg-cream rounded-xl p-6 mb-6 text-center">
                <img src="https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=https://imo.im" 
                     alt="IMO QR Code" class="w-full h-auto rounded-lg">
            </div>

            <!-- Инструкция -->
            <div class="space-y-3 mb-6">
                <p class="text-ink/70 text-sm">
                    <strong>Как добавить нас в IMO:</strong>
                </p>
                <ol class="text-ink/60 text-sm space-y-2 list-decimal list-inside">
                    <li>Откройте IMO на телефоне</li>
                    <li>Нажмите иконку <strong>сканирования</strong></li>
                    <li>Отсканируйте этот код</li>
                    <li>Начните чат с нами! 👋</li>
                </ol>
            </div>

            <!-- Кнопка закрытия -->
            <button @click="imoModal = false"
                    class="w-full px-6 py-3 rounded-full bg-malachite text-white font-bold hover:bg-teal transition">
                Закрыть
            </button>

        </div>
    </div>

    <!-- Кнопка-переключатель (ТОЛЬКО на мобилке/планшете) -->
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

</div>
```

### 📄 `static\images\logos\Videos\desktop.ini`

```text
��
 
 [ . S h e l l C l a s s I n f o ] 
 
 L o c a l i z e d R e s o u r c e N a m e = @ % S y s t e m R o o t % \ s y s t e m 3 2 \ s h e l l 3 2 . d l l , - 2 1 7 9 1 
 
 I n f o T i p = @ % S y s t e m R o o t % \ s y s t e m 3 2 \ s h e l l 3 2 . d l l , - 1 2 6 9 0 
 
 I c o n R e s o u r c e = % S y s t e m R o o t % \ s y s t e m 3 2 \ i m a g e r e s . d l l , - 1 8 9 
 
 I c o n F i l e = % S y s t e m R o o t % \ s y s t e m 3 2 \ s h e l l 3 2 . d l l 
 
 I c o n I n d e x = - 2 3 8 
 
 
```

