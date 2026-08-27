# 📦 Код проекта TM IMPRESSIVE

> Собрано: 27.08.2026 00:13
> Всего файлов: 105
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
```

---

## 📄 Содержимое файлов

### 📄 `cases\templates\cases\detail.html`

```html
{% extends "main/base.html" %}
{% load static %}

{% block title %}{{ case.title }} — Кейс{% endblock %}

{% block content %}

<!-- ================= HERO ================= -->
<section class="relative bg-malachite text-white py-20">
    <div class="absolute inset-0 bg-black/20"></div>
    {% if case.image %}
        <img src="{{ case.image.url }}" alt="{{ case.title }}"
             class="absolute inset-0 w-full h-full object-cover opacity-30">
    {% endif %}
    
    <div class="relative max-w-6xl mx-auto px-4 text-center">
        <a href="{% url 'cases:list' %}"
           class="inline-flex items-center gap-2 text-cream/70 hover:text-brass transition mb-6">
            <i class="fa-solid fa-arrow-left"></i> К кейсам
        </a>
        
        <span class="inline-block px-4 py-1 mb-4 rounded-full bg-brass text-malachite
               text-sm font-bold">
            {{ case.get_direction_display }}
        </span>
        
        <h1 class="text-5xl md:text-6xl font-extrabold mb-6">{{ case.title }}</h1>
        
        {% if case.client %}
        <p class="text-xl text-cream/80">
            📌 Клиент: <b>{{ case.client }}</b>
        </p>
        {% endif %}
    </div>
</section>

<!-- ================= КОНТЕНТ ================= -->
<section class="py-16 bg-cream">
    <div class="max-w-4xl mx-auto px-4 space-y-12">
        
        <!-- Основное фото -->
        {% if case.image %}
        <div class="rounded-2xl overflow-hidden shadow-lg">
            <img src="{{ case.image.url }}" alt="{{ case.title }}"
                 class="w-full h-auto object-cover">
        </div>
        {% endif %}
        
        <!-- Описание -->
        {% if case.short_description or case.full_description %}
        <div class="bg-white rounded-2xl p-8 shadow-md">
            <h2 class="text-2xl font-bold text-malachite mb-4">О проекте</h2>
            {% if case.short_description %}
            <p class="text-ink/70 leading-relaxed text-lg mb-4">
                {{ case.short_description }}
            </p>
            {% endif %}
            {% if case.full_description %}
            <div class="text-ink/60 leading-relaxed">
                {{ case.full_description|linebreaks }}
            </div>
            {% endif %}
        </div>
        {% endif %}
        
        <!-- Результат -->
        {% if case.result %}
        <div class="bg-white rounded-2xl p-8 shadow-md border-l-4 border-brass">
            <h2 class="text-2xl font-bold text-malachite mb-4">
                <i class="fa-solid fa-circle-check text-teal mr-2"></i>
                Результат
            </h2>
            <p class="text-ink/70 leading-relaxed text-lg font-semibold">
                {{ case.result }}
            </p>
        </div>
        {% endif %}
    </div>
</section>

<!-- ================= ПОХОЖИЕ КЕЙСЫ ================= -->
{% if similar %}
<section class="py-16 bg-white">
    <div class="max-w-6xl mx-auto px-4">
        <h2 class="text-3xl font-bold text-malachite mb-8 text-center">
            Другие проекты
        </h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {% for s_case in similar %}
            <a href="{% url 'cases:detail' s_case.slug %}"
               class="group bg-cream rounded-2xl overflow-hidden shadow-md
                      hover:shadow-lg transition-all">
                
                <div class="relative h-40 bg-gradient-to-br from-malachite to-teal">
                    {% if s_case.image %}
                        <img src="{{ s_case.image.url }}" alt="{{ s_case.title }}"
                             class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
                    {% else %}
                        <div class="w-full h-full flex items-center justify-center">
                            <i class="fa-solid fa-trophy text-brass/60 text-3xl"></i>
                        </div>
                    {% endif %}
                </div>
                
                <div class="p-4">
                    <h3 class="font-bold text-malachite group-hover:text-teal transition mb-1">
                        {{ s_case.title }}
                    </h3>
                    {% if s_case.client %}
                    <p class="text-xs text-ink/40">{{ s_case.client }}</p>
                    {% endif %}
                </div>
            </a>
            {% endfor %}
        </div>
    </div>
</section>
{% endif %}

<!-- ================= CTA ================= -->
<section class="py-16 bg-malachite text-white">
    <div class="max-w-4xl mx-auto px-4 text-center">
        <h2 class="text-3xl md:text-4xl font-bold mb-4">
            Хотите свой кейс?
        </h2>
        <p class="text-lg text-cream/80 mb-8">
            Давайте создадим вместе что-то впечатляющее
        </p>
        <a href="{% url 'contacts:index' %}"
           class="inline-block px-8 py-4 rounded-full bg-brass text-malachite
                  font-bold text-lg hover:scale-105 transition-transform">
            💬 Начать проект
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

### 📄 `cases\templates\cases\list.html`

```html
{% extends "main/base.html" %}
{% load static %}

{% block title %}Портфолио / Кейсы — TM IMPRESSIVE{% endblock %}

{% block content %}

<!-- ================= HERO ================= -->
<section class="bg-malachite text-white py-16 md:py-24">
    <div class="max-w-6xl mx-auto px-4 text-center">
        <span class="inline-block px-4 py-1 mb-4 rounded-full bg-brass/20 text-brass text-sm font-semibold">
            🏆 ПОРТФОЛИО
        </span>
        <h1 class="text-4xl md:text-6xl font-extrabold mb-4 leading-tight">
            Реализованные проекты
        </h1>
        <p class="text-lg md:text-xl text-cream/90 max-w-3xl mx-auto">
            Вот что нам удалось создать для наших клиентов — от туров до консалтинга
        </p>
    </div>
</section>

<!-- ================= ФИЛЬТР ================= -->
<section class="bg-white border-b border-cream sticky top-0 z-20">
    <div class="max-w-6xl mx-auto px-4 py-4 flex items-center gap-4 overflow-x-auto">
        <span class="text-sm font-bold text-ink/50 uppercase shrink-0">Фильтр:</span>
        
        <a href="?{% if selected_direction %}{% endif %}"
           class="shrink-0 px-4 py-2 rounded-full text-sm font-bold transition
           {% if not selected_direction %}bg-malachite text-white{% else %}text-ink/60 hover:bg-cream{% endif %}">
            Все
        </a>
        
        {% for code in directions %}
        <a href="?direction={{ code }}"
           class="shrink-0 px-4 py-2 rounded-full text-sm font-bold transition
           {% if selected_direction == code %}bg-malachite text-white{% else %}text-ink/60 hover:bg-cream{% endif %}">
            {{ direction_labels|get_item:code }}
        </a>
        {% endfor %}
    </div>
</section>

<!-- ================= КЕЙСЫ ================= -->
<section class="py-16 bg-cream min-h-[60vh]">
    <div class="max-w-6xl mx-auto px-4">
        
        {% if cases %}
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {% for case in cases %}
            <a href="{% url 'cases:detail' case.slug %}"
               class="group bg-white rounded-2xl overflow-hidden shadow-md
                      hover:shadow-2xl hover:-translate-y-2 transition-all duration-300">
                
                <!-- Фото или градиент -->
                <div class="relative h-48 bg-gradient-to-br from-malachite to-teal overflow-hidden">
                    {% if case.image %}
                        <img src="{{ case.image.url }}" alt="{{ case.title }}"
                             class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
                    {% else %}
                        <div class="w-full h-full flex items-center justify-center">
                            <i class="fa-solid fa-trophy text-brass/60 text-5xl"></i>
                        </div>
                    {% endif %}
                    <!-- Бейдж направления -->
                    <span class="absolute top-3 left-3 px-3 py-1 rounded-full
                           bg-brass text-malachite text-xs font-bold">
                        {{ direction_labels|get_item:case.direction }}
                    </span>
                </div>
                
                <!-- Контент -->
                <div class="p-5">
                    {% if case.client %}
                    <span class="text-ink/40 text-xs uppercase tracking-wider">
                        {{ case.client }}
                    </span>
                    {% endif %}
                    
                    <h3 class="text-lg font-bold text-malachite mt-1 mb-2
                           group-hover:text-teal transition">
                        {{ case.title }}
                    </h3>
                    
                    <p class="text-ink/60 text-sm mb-4 line-clamp-2">
                        {{ case.short_description }}
                    </p>
                    
                    {% if case.result %}
                    <p class="text-sm text-malachite font-semibold pt-3 border-t border-cream">
                        <i class="fa-solid fa-circle-check text-teal mr-1"></i>
                        {{ case.result }}
                    </p>
                    {% endif %}
                </div>
            </a>
            {% endfor %}
        </div>
        
        {% else %}
        <!-- Если кейсов нет -->
        <div class="text-center py-20">
            <i class="fa-solid fa-briefcase text-ink/20 text-6xl mb-4"></i>
            <p class="text-xl text-ink/50 mb-3">Кейсы в разработке</p>
            <p class="text-ink/40 mb-8">
                Прямо сейчас мы работаем над интересными проектами.<br>
                Следите за обновлениями! 🚀
            </p>
            <a href="{% url 'home' %}"
               class="inline-block px-6 py-3 rounded-full bg-malachite text-white
                      font-bold hover:bg-teal transition">
                На главную
            </a>
        </div>
        {% endif %}
    </div>
</section>

{% endblock %}

{# 🔧 Фильтр по словарю #}
{% block scripts %}
<script>
// Этот фильтр добавляет в шаблон функцию get_item для словарей
</script>
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
            Профессиональные переводы на английский, китайский, туркменский и русский языки
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

<!-- ================= БЛОК 1: УСЛУГИ ПЕРЕВОДОВ ================= -->
<section class="py-16 md:py-24 bg-cream">
    <div class="max-w-6xl mx-auto px-4">
        <h2 class="text-3xl md:text-5xl font-extrabold text-center text-malachite mb-4">
            Виды переводов
        </h2>
        <p class="text-center text-ink/70 mb-12 max-w-2xl mx-auto">
            Подберём формат под ваши документы и мероприятия
        </p>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-file-lines"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Письменный перевод</h3>
                <p class="text-ink/70">Документы, статьи, договоры и любые тексты с соблюдением стиля и терминологии.</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-comments"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Устный перевод</h3>
                <p class="text-ink/70">Последовательный и синхронный перевод на встречах, переговорах и презентациях.</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-scale-balanced"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Юридический перевод</h3>
                <p class="text-ink/70">Договоры, контракты и правовые документы с нотариальным оформлением.</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-microchip"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Технический перевод</h3>
                <p class="text-ink/70">Инструкции, спецификации и техдокументация с точными техническими терминами.</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-stamp"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Нотариальный перевод</h3>
                <p class="text-ink/70">Заверенные переводы для официальных органов и государственных учреждений.</p>
            </div>

            {# 🚫 ЗАКОММЕНТИРОВАНО — Сопровождение мероприятий убрано по правкам #}
            {% comment %}
            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-microphone"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Сопровождение мероприятий</h3>
                <p class="text-ink/70">Синхронный перевод конференций, саммитов, семинаров и деловых встреч.</p>
            </div>
            {% endcomment %}

        </div>
    </div>
</section>

{# ===================================================== #}
{# 🚫 ЯЗЫКИ ПЕРЕВОДА — ЗАКОММЕНТИРОВАНО по правкам #}
{# ===================================================== #}
{% comment %}
<!-- ===== ЯЗЫКИ ===== -->
<section class="py-16 md:py-24 bg-white">
    <div class="max-w-6xl mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-extrabold text-center text-malachite mb-12">
            Языки перевода
        </h2>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">

            <div class="bg-gradient-to-br from-malachite to-teal rounded-2xl p-8 text-white text-center shadow-lg hover:shadow-xl transition-all">
                <img src="https://flagcdn.com/w120/ru.png" alt="Русский" class="w-20 h-14 mx-auto mb-4 rounded object-cover ring-2 ring-white/30">
                <h3 class="text-2xl font-bold mb-2">Русский</h3>
                <p class="text-white/80">Деловые документы и межличностное общение</p>
            </div>

            <div class="bg-gradient-to-br from-malachite to-teal rounded-2xl p-8 text-white text-center shadow-lg hover:shadow-xl transition-all">
                <img src="https://flagcdn.com/w120/gb.png" alt="Английский" class="w-20 h-14 mx-auto mb-4 rounded object-cover ring-2 ring-white/30">
                <h3 class="text-2xl font-bold mb-2">Английский</h3>
                <p class="text-white/80">Международные контракты и переговоры</p>
            </div>

            <div class="bg-gradient-to-br from-malachite to-teal rounded-2xl p-8 text-white text-center shadow-lg hover:shadow-xl transition-all">
                <img src="https://flagcdn.com/w120/cn.png" alt="Китайский" class="w-20 h-14 mx-auto mb-4 rounded object-cover ring-2 ring-white/30">
                <h3 class="text-2xl font-bold mb-2">Китайский</h3>
                <p class="text-white/80">Деловые отношения с азиатскими партнёрами</p>
            </div>

            <div class="bg-gradient-to-br from-malachite to-teal rounded-2xl p-8 text-white text-center shadow-lg hover:shadow-xl transition-all">
                <img src="https://flagcdn.com/w120/tm.png" alt="Туркменский" class="w-20 h-14 mx-auto mb-4 rounded object-cover ring-2 ring-white/30">
                <h3 class="text-2xl font-bold mb-2">Туркменский</h3>
                <p class="text-white/80">Локальное общение и гос. документы</p>
            </div>

        </div>
    </div>
</section>
{% endcomment %}

{# ===================================================== #}
{# 🚫 ПАКЕТЫ УСЛУГ — ЗАКОММЕНТИРОВАНО по правкам #}
{# ===================================================== #}
{% comment %}
<!-- ===== ПАКЕТЫ УСЛУГ ===== -->
<section class="py-16 md:py-24 bg-cream">
    <div class="max-w-6xl mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-extrabold text-center text-malachite mb-4">
            Пакеты услуг
        </h2>
        <p class="text-center text-ink/70 mb-12 max-w-2xl mx-auto">
            Выберите подходящий вариант для вашего проекта
        </p>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">

            <!-- Базовый -->
            <div class="relative bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all">
                <h3 class="text-2xl font-bold text-malachite mb-2">Стандарт</h3>
                <p class="text-ink/60 text-sm mb-6">Для небольших проектов</p>

                <div class="mb-6">
                    <span class="text-4xl font-bold text-malachite">от $0.10</span>
                    <span class="text-ink/50 ml-2">за слово</span>
                </div>

                <ul class="space-y-3 mb-8">
                    <li class="flex items-start gap-2">
                        <i class="fa-solid fa-check text-teal mt-1"></i>
                        <span class="text-ink/70">Письменный перевод</span>
                    </li>
                    <li class="flex items-start gap-2">
                        <i class="fa-solid fa-check text-teal mt-1"></i>
                        <span class="text-ink/70">Проверка контента</span>
                    </li>
                    <li class="flex items-start gap-2">
                        <i class="fa-solid fa-check text-teal mt-1"></i>
                        <span class="text-ink/70">Сроки: 3-5 дней</span>
                    </li>
                </ul>

                <a href="{% url 'contacts:index' %}" class="block w-full text-center px-6 py-3 rounded-full bg-malachite text-white font-bold hover:bg-teal transition">
                    Выбрать
                </a>
            </div>

            <!-- Профессиональный (выделен) -->
            <div class="relative bg-gradient-to-br from-malachite to-teal rounded-2xl p-8 shadow-xl text-white border-2 border-brass">
                <span class="absolute -top-4 left-1/2 -translate-x-1/2 px-4 py-1 bg-brass text-malachite text-xs font-bold rounded-full">
                    ⭐ Популярно
                </span>
                <h3 class="text-2xl font-bold mb-2">Профессиональный</h3>
                <p class="text-white/80 text-sm mb-6">Для деловых проектов</p>

                <div class="mb-6">
                    <span class="text-4xl font-bold">от $0.15</span>
                    <span class="text-white/70 ml-2">за слово</span>
                </div>

                <ul class="space-y-3 mb-8">
                    <li class="flex items-start gap-2">
                        <i class="fa-solid fa-check text-brass mt-1"></i>
                        <span class="text-white/90">Всё из Стандарта</span>
                    </li>
                    <li class="flex items-start gap-2">
                        <i class="fa-solid fa-check text-brass mt-1"></i>
                        <span class="text-white/90">Корректор-носитель</span>
                    </li>
                    <li class="flex items-start gap-2">
                        <i class="fa-solid fa-check text-brass mt-1"></i>
                        <span class="text-white/90">Сроки: 1-3 дня</span>
                    </li>
                    <li class="flex items-start gap-2">
                        <i class="fa-solid fa-check text-brass mt-1"></i>
                        <span class="text-white/90">Консультация бесплатно</span>
                    </li>
                </ul>

                <a href="{% url 'contacts:index' %}" class="block w-full text-center px-6 py-3 rounded-full bg-brass text-malachite font-bold hover:scale-105 transition-transform">
                    Выбрать
                </a>
            </div>

            <!-- Премиум -->
            <div class="relative bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all">
                <h3 class="text-2xl font-bold text-malachite mb-2">Премиум</h3>
                <p class="text-ink/60 text-sm mb-6">Для критичных проектов</p>

                <div class="mb-6">
                    <span class="text-4xl font-bold text-malachite">по запросу</span>
                </div>

                <ul class="space-y-3 mb-8">
                    <li class="flex items-start gap-2">
                        <i class="fa-solid fa-check text-teal mt-1"></i>
                        <span class="text-ink/70">Всё из Профессионального</span>
                    </li>
                    <li class="flex items-start gap-2">
                        <i class="fa-solid fa-check text-teal mt-1"></i>
                        <span class="text-ink/70">Экспресс-срок (24 часа)</span>
                    </li>
                    <li class="flex items-start gap-2">
                        <i class="fa-solid fa-check text-teal mt-1"></i>
                        <span class="text-ink/70">Нотариальное заверение</span>
                    </li>
                    <li class="flex items-start gap-2">
                        <i class="fa-solid fa-check text-teal mt-1"></i>
                        <span class="text-ink/70">Синхронный перевод</span>
                    </li>
                </ul>

                <a href="{% url 'contacts:index' %}" class="block w-full text-center px-6 py-3 rounded-full bg-malachite text-white font-bold hover:bg-teal transition">
                    Узнать цену
                </a>
            </div>

        </div>
    </div>
</section>
{% endcomment %}

{# ===================================================== #}
{# 🚫 ПОЧЕМУ ВЫБИРАЮТ НАС — ЗАКОММЕНТИРОВАНО по правкам #}
{# ===================================================== #}
{% comment %}
<!-- ===== ПОЧЕМУ ВЫБИРАЮТ НАС ===== -->
<section class="py-16 md:py-24 bg-cream">
    <div class="max-w-6xl mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-extrabold text-center text-malachite mb-14">
            Почему выбирают нас
        </h2>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">

            <div class="text-center">
                <div class="w-16 h-16 mx-auto flex items-center justify-center rounded-2xl bg-malachite text-brass text-3xl mb-4">
                    <i class="fa-solid fa-graduation-cap"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Носители языка</h3>
                <p class="text-ink/70">Переводчики с профильным образованием.</p>
            </div>

            <div class="text-center">
                <div class="w-16 h-16 mx-auto flex items-center justify-center rounded-2xl bg-malachite text-brass text-3xl mb-4">
                    <i class="fa-solid fa-hourglass-end"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Соблюдаем сроки</h3>
                <p class="text-ink/70">Точно в дедлайн, без задержек.</p>
            </div>

            <div class="text-center">
                <div class="w-16 h-16 mx-auto flex items-center justify-center rounded-2xl bg-malachite text-brass text-3xl mb-4">
                    <i class="fa-solid fa-shield"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Конфиденциальность</h3>
                <p class="text-ink/70">Полная защита ваших документов.</p>
            </div>

            <div class="text-center">
                <div class="w-16 h-16 mx-auto flex items-center justify-center rounded-2xl bg-malachite text-brass text-3xl mb-4">
                    <i class="fa-solid fa-check-double"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Контроль качества</h3>
                <p class="text-ink/70">Двойная проверка каждого перевода.</p>
            </div>

        </div>
    </div>
</section>
{% endcomment %}


<!-- ================= БЛОК: НУЖЕН ПЕРЕВОД? ================= -->
<section class="py-16 md:py-20 bg-malachite text-white">
    <div class="max-w-4xl mx-auto px-4 text-center">
        <h2 class="text-3xl md:text-5xl font-bold mb-4">
            Нужен перевод?
        </h2>
        <p class="text-lg text-cream/90 mb-10">
            Пришлите документ — оценим объём и сроки. Ответим в течение 1 часа.
        </p>
        <a href="{% url 'contacts:index' %}"
           class="inline-block px-10 py-4 rounded-full bg-brass text-malachite font-bold text-lg shadow-xl hover:scale-105 transition-transform duration-200">
            Заказать перевод
        </a>
    </div>
</section>

<!-- ================= БЛОК 2: АРЕНДА ОБОРУДОВАНИЯ ================= -->
<section class="py-16 md:py-24 bg-white">
    <div class="max-w-6xl mx-auto px-4">
        
        <!-- Заголовок -->
        <div class="text-center mb-14">
            <span class="inline-block px-4 py-1 mb-4 rounded-full bg-teal/20 text-teal text-sm font-semibold">
                <i class="fa-solid fa-microphone mr-2"></i>ТЕХНИЧЕСКАЯ ПОДДЕРЖКА
            </span>
            <h2 class="text-4xl md:text-5xl lg:text-5xl font-extrabold text-malachite mb-6">
                Аренда оборудования для переводов
            </h2>
            <p class="max-w-3xl mx-auto text-lg text-ink/70">
                Полный спектр современного оборудования для конференций, форумов и международных мероприятий
            </p>
            <div class="w-24 h-1 bg-teal mx-auto mt-6 rounded-full"></div>
        </div>

        <!-- Основное оборудование -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-14">

            <!-- Синхронная кабина -->
            <div class="bg-gradient-to-br from-cream to-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all border-l-4 border-teal">
                <div class="flex items-start gap-4 mb-6">
                    <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-teal text-white text-2xl shrink-0">
                        <i class="fa-solid fa-microphone"></i>
                    </div>
                    <div>
                        <h3 class="text-2xl font-bold text-malachite mb-2">Синхронная кабина</h3>
                        <p class="text-ink/60">Для переводчиков с шумоизоляцией</p>
                    </div>
                </div>
                <ul class="space-y-2 text-ink/70 mb-6">
                    <li class="flex items-center gap-2">
                        <i class="fa-solid fa-check text-teal"></i>
                        Переносная и стационарная (до 4 шт)
                    </li>
                    <li class="flex items-center gap-2">
                        <i class="fa-solid fa-check text-teal"></i>
                        Высокая звукоизоляция
                    </li>
                    <li class="flex items-center gap-2">
                        <i class="fa-solid fa-check text-teal"></i>
                        Включена стойка для наушников
                    </li>
                </ul>
                <p class="text-sm text-teal font-semibold">Цена: от $150 за кабину в день</p>
            </div>

            <!-- Приёмники и наушники -->
            <div class="bg-gradient-to-br from-cream to-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all border-l-4 border-brass">
                <div class="flex items-start gap-4 mb-6">
                    <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-brass text-malachite text-2xl shrink-0">
                        <i class="fa-solid fa-headphones"></i>
                    </div>
                    <div>
                        <h3 class="text-2xl font-bold text-malachite mb-2">Приёмники и наушники</h3>
                        <p class="text-ink/60">Беспроводная система передачи звука</p>
                    </div>
                </div>
                <ul class="space-y-2 text-ink/70 mb-6">
                    <li class="flex items-center gap-2">
                        <i class="fa-solid fa-check text-brass"></i>
                        Беспроводные приёмники (25–100 шт)
                    </li>
                    <li class="flex items-center gap-2">
                        <i class="fa-solid fa-check text-brass"></i>
                        Удобные и лёгкие наушники
                    </li>
                    <li class="flex items-center gap-2">
                        <i class="fa-solid fa-check text-brass"></i>
                        Зарядка и резерв батарей включены
                    </li>
                </ul>
                <p class="text-sm text-brass font-semibold">Цена: от $2.50 за приёмник в день</p>
            </div>

        </div>

        <!-- Доп. оборудование -->
        <div class="mb-14">
            <h3 class="text-2xl font-bold text-malachite mb-6">Дополнительное оборудование</h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                
                <div class="bg-white rounded-xl p-5 shadow-md hover:shadow-lg transition-all border border-cream hover:border-teal">
                    <div class="text-3xl mb-3 text-teal">🎤</div>
                    <h4 class="font-bold text-malachite mb-2">Микрофоны</h4>
                    <!--<p class="text-sm text-ink/60">Настольные и петличные</p>
                    <p class="text-xs text-teal font-semibold mt-3">от $30</p> -->
                </div>

                <div class="bg-white rounded-xl p-5 shadow-md hover:shadow-lg transition-all border border-cream hover:border-teal">
                    <div class="text-3xl mb-3 text-teal">🔊</div>
                    <h4 class="font-bold text-malachite mb-2">Акустические системы</h4>
                    <!--<p class="text-sm text-ink/60">Колонки и усилители</p>
                    <p class="text-xs text-teal font-semibold mt-3">от $80</p> -->
                </div>

                <div class="bg-white rounded-xl p-5 shadow-md hover:shadow-lg transition-all border border-cream hover:border-teal">
                    <div class="text-3xl mb-3 text-teal">📺</div>
                    <h4 class="font-bold text-malachite mb-2">Экраны и проекторы</h4>
                    <!--<p class="text-sm text-ink/60">Для вывода субтитров</p>
                    <p class="text-xs text-teal font-semibold mt-3">от $120</p> -->
                </div>

                <div class="bg-white rounded-xl p-5 shadow-md hover:shadow-lg transition-all border border-cream hover:border-teal">
                    <div class="text-3xl mb-3 text-teal">🔌</div>
                    <h4 class="font-bold text-malachite mb-2">Смешивающее оборудование</h4>
                    <!--<p class="text-sm text-ink/60">Микшеры и трансляция</p>
                    <p class="text-xs text-teal font-semibold mt-3">от $100</p> -->
                </div>

            </div>
        </div>

        <!-- Преимущества аренды -->
        <div class="bg-gradient-to-r from-teal/10 to-brass/10 rounded-2xl p-10 border border-teal/30">
            <h3 class="text-2xl font-bold text-malachite mb-6">Почему выбирают нашу аренду?</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

                <div class="flex gap-4">
                    <div class="text-2xl shrink-0 text-teal">✓</div>
                    <div>
                        <h4 class="font-bold text-malachite mb-1">Современное оборудование</h4>
                        <p class="text-sm text-ink/70">Только новая и проверенная техника</p>
                    </div>
                </div>

                <div class="flex gap-4">
                    <div class="text-2xl shrink-0 text-teal">✓</div>
                    <div>
                        <h4 class="font-bold text-malachite mb-1">Техническая поддержка 24/7</h4>
                        <p class="text-sm text-ink/70">Наш специалист присутствует на месте</p>
                    </div>
                </div>

                <div class="flex gap-4">
                    <div class="text-2xl shrink-0 text-teal">✓</div>
                    <div>
                        <h4 class="font-bold text-malachite mb-1">Быстрая доставка и установка</h4>
                        <p class="text-sm text-ink/70">Монтаж за 1–2 часа, демонтаж после</p>
                    </div>
                </div>

                <div class="flex gap-4">
                    <div class="text-2xl shrink-0 text-teal">✓</div>
                    <div>
                        <h4 class="font-bold text-malachite mb-1">Гибкие сроки аренды</h4>
                        <p class="text-sm text-ink/70">От нескольких часов до нескольких недель</p>
                    </div>
                </div>

                <div class="flex gap-4">
                    <div class="text-2xl shrink-0 text-teal">✓</div>
                    <div>
                        <h4 class="font-bold text-malachite mb-1">Конкурентные цены</h4>
                        <p class="text-sm text-ink/70">Скидки на пакеты и долгосрочную аренду</p>
                    </div>
                </div>

                <div class="flex gap-4">
                    <div class="text-2xl shrink-0 text-teal">✓</div>
                    <div>
                        <h4 class="font-bold text-malachite mb-1">Страховка включена</h4>
                        <p class="text-sm text-ink/70">Защита от повреждений и потерь</p>
                    </div>
                </div>

            </div>
        </div>

    </div>
</section>

<!-- ================= CTA ================= -->
<section class="py-16 md:py-20 bg-malachite text-white">
    <div class="max-w-4xl mx-auto px-4 text-center">
        <h2 class="text-3xl md:text-4xl font-bold mb-6">
            Организуем перевод и оборудование под ключ
        </h2>
        <p class="text-lg text-cream/90 mb-8 max-w-2xl mx-auto">
            От маленького митинга до большой международной конференции — справимся с любым масштабом
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <a href="{% url 'contacts:index' %}"
               class="inline-block px-8 py-4 rounded-full bg-brass text-malachite font-bold text-lg hover:scale-105 transition-transform">
                Заказать услугу
            </a>
            <a href="{% url 'contacts:index' %}"
               class="inline-block px-8 py-4 rounded-full border-2 border-brass text-brass font-bold text-lg hover:bg-brass/10 transition">
                Получить консультацию
            </a>
        </div>
    </div>
</section>

{% endblock %}
```

### 📄 `main\templates\main\base.html`

```html
<!-- 📁 main/templates/main/base.html -->
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}TM IMPRESSIVE{% endblock %}</title>
    {% load static tailwind_tags %}
    {% tailwind_css %}
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <!-- ⚡ Alpine.js — нужен для мобильного меню и панели мессенджеров -->
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
</head>
<body class="bg-[#F8F5F0] text-ink min-h-screen flex flex-col">
    {% include "main/partials/header.html" %}

    <main class="flex-1">
        {% block content %}{% endblock %}
    </main>

    {% include "main/partials/footer.html" %}
    {% include "main/partials/messenger_panel.html" %}

    <!-- 🤖 Виртуальный ассистент -->
    {% include "main/partials/assistant_widget.html" %}

    {% block scripts %}{% endblock %}
</body>
</html>
```

### 📄 `main\templates\main\home.html`

```html
{% extends "main/base.html" %}
{% load static %}

{% block content %}
<section class="relative flex flex-col items-start justify-center min-h-[95vh] py-24 px-6 md:px-16">
    <!-- Баннер -->
    <img src="{% static 'images/home_hero_2K-1.jpg' %}" alt="TM IMPRESSIVE Banner" 
        class="absolute inset-0 object-cover w-full h-full opacity-95 pointer-events-none" />
    <!-- Контент поверх баннера -->
    <div class="relative z-10 max-w-2xl mt-8 ml-0 md:ml-20 animate-fade-in-up">
        <span class="text-lg text-teal tracking-widest uppercase font-bold mb-3 block">Откройте мир с</span>
        <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold text-malachite mb-6">TM IMPRESSIVE</h1>
        
        <p class="text-2xl md:text-3xl text-teal font-semibold mb-6">Connecting opportunities,<br> elevating futures</p>
        <p class="mb-8 text-ink leading-relaxed">
            
            Туризм, MICE, бизнес-консалтинг и лингвистика — ваш надёжный партнёр в Туркменистане и за его пределами.
        </p>
        <a href="{% url 'contacts:index' %}" class="inline-block bg-brass hover:bg-teal text-white text-lg font-bold px-8 py-3 rounded-full shadow-lg transition">Оставить заявку</a>
    </div>
    
</section>
<!-- ===== 3 НАПРАВЛЕНИЯ ===== -->
<section class="py-20 px-6 md:px-16 bg-cream">
    <div class="max-w-7xl mx-auto">

        <!-- Заголовок секции -->
        <div class="text-center mb-14">
            <!-- ✏️ было «Что мы делаем» + подзаголовок «Три направления — одна команда» -->
            <h2 class="text-4xl md:text-5xl lg:text-5xl font-extrabold text-malachite">
                Сферы деятельности
            </h2>
            <div class="w-24 h-1 bg-brass mx-auto mt-6 rounded-full"></div>
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
                <h3 class="text-2xl md:text-3xl font-bold text-malachite mb-3">Туризм и MICE</h3>
                <p class="text-ink/70 leading-relaxed mb-5 text-base md:text-lg">
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
                <h3 class="text-2xl md:text-3xl font-bold text-malachite mb-3">Бизнес-консалтинг</h3>
                <p class="text-ink/70 leading-relaxed mb-5 text-base md:text-lg">
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
                <h3 class="text-2xl md:text-3xl font-bold text-malachite mb-3">Лингвистика</h3>
                <p class="text-ink/70 leading-relaxed mb-5 text-base md:text-lg">
                    Профессиональный перевод, синхронный перевод на мероприятиях и аренда оборудования для конференций.
                </p>
                <span class="inline-flex items-center gap-2 text-teal font-bold group-hover:gap-3 transition-all">
                    Подробнее <i class="fa-solid fa-arrow-right"></i>
                </span>
            </a>

        </div>
    </div>
</section>

{# ===================================================== #}
{# 🚫 ПОПУЛЯРНЫЕ ТУРЫ — ВРЕМЕННО ОТКЛЮЧЕНО (закомментировано)      #}
{# ===================================================== #}
{% comment %}
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
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto">
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

{% endcomment %}

<!-- ===== ПОЧЕМУ ВЫБИРАЮТ НАС ===== -->
<section class="py-20 px-6 md:px-16 bg-malachite text-white relative overflow-hidden">
    <!-- Декоративный узор (мягкое свечение) -->
    <div class="absolute top-0 right-0 w-96 h-96 bg-brass/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2"></div>
    <div class="absolute bottom-0 left-0 w-96 h-96 bg-teal/20 rounded-full blur-3xl translate-y-1/2 -translate-x-1/2"></div>

    <div class="max-w-7xl mx-auto relative z-10">

        <!-- Заголовок -->
        <div class="text-center mb-16">
            <span class="text-brass tracking-widest uppercase font-bold text-2xl md:text-2xl">Наши преимущества</span>
            <h2 class="text-4xl md:text-5xl lg:text-5xl font-extrabold mt-4">
                Почему выбирают <span class="text-brass">TM Impressive</span>
            </h2>
            <div class="w-24 h-1 bg-brass mx-auto mt-5 rounded-full"></div>
        </div>

        <!-- 4 преимущества -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-2 gap-8 max-w-6xl mx-auto">

            <!-- 1 -->
             {% comment %}
            <div class="text-center group">
                <div class="w-20 h-20 mx-auto flex items-center justify-center rounded-2xl bg-white/10 text-brass text-4xl mb-5 group-hover:bg-brass group-hover:text-malachite transition-all duration-300">
                    <i class="fa-solid fa-award"></i>
                </div>
                <h3 class="text-2xl md:text-3xl font-bold mb-3">Знаем Туркменистан изнутри</h3>
                <p class="text-white/80 text-base md:text-lg leading-relaxed">
                    Мы живём и работаем здесь: знаем страну, её правила и людей —
                    и открываем двери, которые обычно закрыты.
                </p>
            </div>
            {% endcomment %}

            <!-- 2 -->
            <div class="text-center group">
                <div class="w-20 h-20 mx-auto flex items-center justify-center rounded-2xl bg-white/10 text-brass text-4xl mb-5 group-hover:bg-brass group-hover:text-malachite transition-all duration-300">
                    <i class="fa-solid fa-headset"></i>
                </div>
                <h3 class="text-2xl md:text-3xl font-bold mb-3">Умная поддержка 24/7</h3>
                <p class="text-white/80 text-base md:text-lg leading-relaxed">
                    Наш виртуальный ассистент на связи в любое время,
                    а менеджеры подключаются с 9:00 до 18:00.
                </p>
            </div>

            <!-- 3 -->
            <div class="text-center group">
                <div class="w-20 h-20 mx-auto flex items-center justify-center rounded-2xl bg-white/10 text-brass text-4xl mb-5 group-hover:bg-brass group-hover:text-malachite transition-all duration-300">
                    <i class="fa-solid fa-globe"></i>
                </div>
                <!-- ⚠️ Гузель: в тексте ниже 3 языка, а в заголовке «4». Если нужно —
                     замени строку ниже на: Работаем на 3 языках -->
                <h3 class="text-2xl md:text-3xl font-bold mb-3">Работаем на 4 языках</h3>
                <p class="text-white/80 text-base md:text-lg leading-relaxed">
                    Английский, китайский и русский: коммуникация без барьеров.
                </p>
            </div>

            {# 🚫 Карточка «Комплексный подход» — ОТКЛЮЧЕНА по правкам #}
            {% comment %}
            <!-- 4 -->
            <div class="text-center group">
                <div class="w-20 h-20 mx-auto flex items-center justify-center rounded-2xl bg-white/10 text-brass text-4xl mb-5 group-hover:bg-brass group-hover:text-malachite transition-all duration-300">
                    <i class="fa-solid fa-handshake"></i>
                </div>
                <h3 class="text-2xl md:text-3xl font-bold mb-3">Комплексный подход</h3>
                <p class="text-white/80 text-base md:text-lg leading-relaxed">
                    Туризм, консалтинг и переводы — всё в одном месте, под ключ и без хлопот.
                </p>
            </div>

            {% endcomment %}

        </div>
    </div>
</section>

{# ===================================================== #}
{# 🚫 КЕЙСЫ / Реализованные проекты — ВРЕМЕННО ОТКЛЮЧЕНО (закомментировано)      #}
{# ===================================================== #}
{% comment %}
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

{% endcomment %}

{# ===================================================== #}
{# 🚫 ПАРТНЁРЫ / Нам доверяют — ВРЕМЕННО ОТКЛЮЧЕНО (закомментировано)      #}
{# ===================================================== #}
{% comment %}
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

{% endcomment %}

<!-- ===== CTA — ПРИЗЫВ ОСТАВИТЬ ЗАЯВКУ ===== -->

{% comment %}
<section class="py-24 bg-cream relative overflow-hidden">
    <!-- декоративные размытые круги -->
    <div class="absolute top-0 right-0 w-96 h-96 bg-teal/20 rounded-full blur-3xl -translate-y-1/3 translate-x-1/3"></div>
    <div class="absolute bottom-0 left-0 w-96 h-96 bg-brass/10 rounded-full blur-3xl translate-y-1/3 -translate-x-1/3"></div>

    <div class="max-w-4xl mx-auto px-6 md:px-16 text-center relative z-10">
        <p class="text-malachite uppercase tracking-widest text-sm font-bold mb-6">
            Готовы начать?
        </p>

        <h2 class="text-4xl md:text-5xl font-bold text-malachite leading-tight mb-6">
            Организуем ваше мероприятие<br class="hidden md:block">
            под ключ
        </h2>

        <p class="text-gray-900/70 text-lg mb-10 max-w-2xl mx-auto">
            Оставьте заявку — и мы свяжемся с вами в течение дня,
            чтобы обсудить детали вашего проекта.
        </p>

        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <a href="{% url 'contacts:index' %}"
               class="inline-block bg-brass text-malachite font-bold px-10 py-4 rounded-full hover:bg-brass/90 transition text-lg shadow-lg">
                Оставить заявку
            </a>
            <a href="{% url 'contacts:index' %}"
               class="inline-block border-2 bg-malachite  text-white font-bold px-10 py-4 rounded-full hover:bg-emerald-800 transition text-lg">
                Связаться с нами
            </a>
        </div>
    </div>
</section>
{% endcomment %}
{% endblock %}
```

