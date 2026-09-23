# 📦 Код проекта TM IMPRESSIVE

> Собрано: 13.09.2026 11:00
> Всего файлов: 112

## 🌳 Структура проекта

```
tmimpressive/
├── .env
├── .gitignore
├── collect_code_split.py
├── manage.py
├── requirements.txt
├── seed_data.py
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
    ├── PROJECT_CODE_PART_1.md
    ├── PROJECT_CODE_PART_2.md
    ├── PROJECT_CODE_PART_3.md
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
        ├── base_site.html
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
            ├── admin_theme.css
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

### 📄 `collect_code_split.py`

```python
"""
================================================================
 collect_code.py — Сборщик кода проекта в несколько файлов
 Проект: TM IMPRESSIVE
================================================================

 Что делает скрипт:
 1. Проходит по всем папкам проекта
 2. Находит файлы с кодом (.py, .html, .css, .js и др.)
 3. Разбивает на части по 99 КБ каждая
 4. Сохраняет в папку project_code_parts/

 Как использовать:
 1. Положи этот файл в КОРЕНЬ проекта (рядом с manage.py)
 2. Запусти:  python collect_code.py
 3. Получишь папку project_code_parts/ с файлами PROJECT_CODE_PART_1.md, 2.md, 3.md...
================================================================
"""

import os
from pathlib import Path
from datetime import datetime

# ================================================================
# НАСТРОЙКИ
# ================================================================

PROJECT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_DIR / "project_code_parts"
MAX_PART_SIZE = 99 * 1024  # 99 КБ для каждого файла

INCLUDE_EXTENSIONS = {
    ".py", ".html", ".css", ".js", ".json", ".yml", ".yaml",
    ".toml", ".txt", ".md", ".cfg", ".ini", ".env",
}

INCLUDE_FILENAMES = {
    "Dockerfile", ".gitignore", ".dockerignore", "Procfile",
    ".env", ".env.example",
}

EXCLUDE_DIRS = {
    "venv", ".venv", "env", "node_modules", "__pycache__",
    ".git", ".idea", ".vscode", "staticfiles", "media",
    "dist", "build", ".pytest_cache", ".mypy_cache", "migrations",
    "project_code_parts",  # Исключаем сами файлы
}

EXCLUDE_FILES = {
    "PROJECT_CODE.md", "collect_code.py", "db.sqlite3",
    "package-lock.json", "poetry.lock",
}

MAX_FILE_SIZE = 200_000  # 200 КБ
SECRET_KEYWORDS = ("KEY", "SECRET", "PASSWORD", "TOKEN", "PASS")


# ================================================================
# ФУНКЦИИ
# ================================================================

def should_include(file_path: Path) -> bool:
    """Проверяем — нужно ли включать этот файл в отчёт."""
    if file_path.name in EXCLUDE_FILES:
        return False
    if file_path.name in INCLUDE_FILENAMES:
        return True
    return file_path.suffix.lower() in INCLUDE_EXTENSIONS


def mask_env_secrets(content: str) -> str:
    """Маскируем секретные значения в .env файле."""
    masked_lines = []
    for line in content.splitlines():
        if "=" in line and not line.strip().startswith("#"):
            key = line.split("=", 1)[0].strip().upper()
            if any(word in key for word in SECRET_KEYWORDS):
                masked_lines.append(f"{line.split('=', 1)[0]}=***СКРЫТО***")
                continue
        masked_lines.append(line)
    return "\n".join(masked_lines)


def get_language(file_path: Path) -> str:
    """Определяем язык для подсветки синтаксиса в Markdown."""
    mapping = {
        ".py": "python",
        ".html": "html",
        ".css": "css",
        ".js": "javascript",
        ".json": "json",
        ".yml": "yaml",
        ".yaml": "yaml",
        ".toml": "toml",
        ".md": "markdown",
    }
    if file_path.name == "Dockerfile":
        return "dockerfile"
    return mapping.get(file_path.suffix.lower(), "text")


def collect_files() -> list:
    """Собираем список всех подходящих файлов проекта."""
    collected = []
    for root, dirs, files in os.walk(PROJECT_DIR):
        # Удаляем мусорные папки из обхода
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for filename in sorted(files):
            file_path = Path(root) / filename
            if should_include(file_path):
                collected.append(file_path)

    # Сортируем
    return sorted(collected, key=lambda p: (len(p.relative_to(PROJECT_DIR).parts), str(p)))


def build_tree(files: list) -> str:
    """Строим текстовое дерево проекта из списка файлов."""
    lines = [f"{PROJECT_DIR.name}/"]
    for f in files:
        rel = f.relative_to(PROJECT_DIR)
        indent = "    " * (len(rel.parts) - 1)
        lines.append(f"{indent}├── {rel.name}")
    return "\n".join(lines)


def main():
    """Главная функция — собираем всё в несколько файлов по 99 КБ."""
    files = collect_files()

    if not files:
        print("⚠️ Файлы не найдены! Проверь что скрипт лежит в корне проекта.")
        return

    # Создаём папку для сохранения
    OUTPUT_DIR.mkdir(exist_ok=True)
    print(f"📁 Папка создана: {OUTPUT_DIR.name}/\n")

    # Строим дерево один раз
    tree = build_tree(files)

    # --- Общая шапка для всех файлов ---
    header = f"""# 📦 Код проекта TM IMPRESSIVE

> Собрано: {datetime.now().strftime('%d.%m.%Y %H:%M')}
> Всего файлов: {len(files)}
> Размер каждой части: ~99 КБ

## 🌳 Структура проекта

```
{tree}
```

---

## 📄 Содержимое файлов

"""

    # --- Переменные для разбиения на части ---
    current_part = 1
    current_content = header
    current_size = len(current_content.encode('utf-8'))
    
    total_size = 0
    processed_files = 0
    skipped_files = 0

    # --- Проходим по всем файлам ---
    for file_path in files:
        rel_path = file_path.relative_to(PROJECT_DIR)

        try:
            size = file_path.stat().st_size
            
            # Пропускаем слишком большие файлы
            if size > MAX_FILE_SIZE:
                print(f"  ⏭️  {rel_path} (пропущен — слишком большой: {size // 1024} КБ)")
                skipped_files += 1
                continue

            # Читаем файл
            content = file_path.read_text(encoding="utf-8", errors="replace")

            # Маскируем секреты в .env файлах
            if file_path.name.startswith(".env"):
                content = mask_env_secrets(content)

            lang = get_language(file_path)
            
            # Формируем блок файла
            file_block = f"### 📄 `{rel_path}`\n\n```{lang}\n{content.rstrip()}\n```\n\n"
            file_block_size = len(file_block.encode('utf-8'))

            # Проверяем — поместится ли файл в текущую часть?
            if current_size + file_block_size > MAX_PART_SIZE and current_content != header:
                # Сохраняем текущую часть
                output_file = OUTPUT_DIR / f"PROJECT_CODE_PART_{current_part}.md"
                output_file.write_text(current_content, encoding="utf-8")
                print(f"  💾 Часть {current_part}: {output_file.name} ({current_size // 1024} КБ)")

                # Начинаем новую часть
                current_part += 1
                current_content = header
                current_size = len(current_content.encode('utf-8'))

            # Добавляем файл в текущую часть
            current_content += file_block
            current_size += file_block_size
            total_size += size
            processed_files += 1

            print(f"  ✅ {rel_path}")

        except Exception as e:
            print(f"  ❌ {rel_path}: {e}")
            skipped_files += 1

    # --- Сохраняем последнюю часть ---
    if current_content != header:
        output_file = OUTPUT_DIR / f"PROJECT_CODE_PART_{current_part}.md"
        output_file.write_text(current_content, encoding="utf-8")
        print(f"  💾 Часть {current_part}: {output_file.name} ({current_size // 1024} КБ)")

    # --- Итоговый отчёт ---
    print("\n" + "=" * 60)
    print(f"🎉 Готово! Папка создана: {OUTPUT_DIR.name}/")
    print(f"📊 Файлов обработано: {processed_files}")
    print(f"⏭️  Файлов пропущено: {skipped_files}")
    print(f"📦 Общий размер кода: {total_size // 1024} КБ")
    print(f"📁 Частей создано: {current_part}")
    print("=" * 60)
    print(f"\n📤 Теперь отправь файлы из папки {OUTPUT_DIR.name}/ в чат!")


# --- Точка входа ---
if __name__ == "__main__":
    main()
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

### 📄 `requirements.txt`

```text
��p y t h o n - d o t e n v = = 1 . 2 . 2 
 
 D j a n g o > = 5 . 0 , < 6 . 0 
 
 p s y c o p g 2 - b i n a r y 
 
 P i l l o w 
 
 g u n i c o r n 
 
 d j - d a t a b a s e - u r l 
 
 p y t h o n - d o t e n v 
 
 d j a n g o - t a i l w i n d 
 
 w h i t e n o i s e 
 
 r e q u e s t s 
 
 r i c h 
 
 c o o k i e c u t t e r 
 
 p y t a i l w i n d c s s 
```

### 📄 `seed_data.py`

```python
#!/usr/bin/env python
"""
================================================================
TM IMPRESSIVE — Seed Script (Тестовые данные)
Создание примеров туров, кейсов, партнёров для демонстрации
================================================================

ЗАПУСК:
    python manage.py shell < seed_data.py

ИЛИ:
    python manage.py shell
    >>> exec(open('seed_data.py').read())
"""

import os
import django

# Инициализация Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tmimpressive.settings')
django.setup()

from tourism.models import Tour, TourImage, TourDay, TourPrice, TourInclude, CategoryFeature
from cases.models import Case, Partner
from contacts.models import ContactMessage

print("🚀 Начинаем загрузку тестовых данных...\n")

# ============================================================
# 1️⃣ ТУРЫ
# ============================================================

print("📍 Создание туров...")

# Тур 1: Классический Туркменистан
tour1, created = Tour.objects.get_or_create(
    slug='klassicheskiy-turkmenistan',
    defaults={
        'title': 'Классический Туркменистан',
        'category': 'standard',
        'tour_type': 'cultural',
        'direction': 'Ашхабад — Дарваза — Дашогуз',
        'duration_days': 7,
        'season': 'Круглый год',
        'season_spring': True,
        'season_summer': True,
        'season_autumn': True,
        'season_winter': True,
        'short_description': 'Познакомьтесь с древними городами, огненным кратером Дарваза и современным Ашхабадом',
        'full_description': '''
Этот маршрут — идеальное введение в Туркменистан. Вы увидите:

• **Ашхабад** — белокаменную столицу с мраморными дворцами
• **Кратер Дарваза** — пылающие «Врата Ада» посреди пустыни Каракумы
• **Древний Мерв** — руины великого города Шёлкового пути
• **Ниса** — столицу Парфянского царства (UNESCO)

Программа включает культурные объекты, природные чудеса и национальную кухню.
        ''',
        'price_from': 1200,
        'is_popular': True,
        'is_active': True,
        'order': 1,
    }
)
if created:
    print(f"  ✓ {tour1.title}")
    
    # Программа по дням
    TourDay.objects.create(
        tour=tour1, day_number=1,
        title='Прибытие в Ашхабад',
        description='Встреча в аэропорту, трансфер в отель. Обзорная экскурсия по столице: площадь Независимости, Arch of Neutrality, мечеть Туркменбаши.'
    )
    TourDay.objects.create(
        tour=tour1, day_number=2,
        title='Ниса и ковровый музей',
        description='Древняя Ниса (UNESCO) — столица Парфянского царства. Посещение Национального музея ковров.'
    )
    TourDay.objects.create(
        tour=tour1, day_number=3,
        title='Дарваза — Врата Ада',
        description='Переезд в пустыню Каракумы (260 км). Прибытие к кратеру Дарваза на закате. Ночёвка в юртовом лагере.'
    )
    
    # Цены
    TourPrice.objects.create(tour=tour1, category='standard', season='all', price=1200)
    TourPrice.objects.create(tour=tour1, category='premium', season='all', price=1800)
    
    # Включено/не включено
    TourInclude.objects.create(tour=tour1, text='Проживание в отелях 3-4*', is_included=True, order=1)
    TourInclude.objects.create(tour=tour1, text='Все трансферы и транспорт', is_included=True, order=2)
    TourInclude.objects.create(tour=tour1, text='Русскоговорящий гид', is_included=True, order=3)
    TourInclude.objects.create(tour=tour1, text='Входные билеты', is_included=True, order=4)
    TourInclude.objects.create(tour=tour1, text='Авиабилеты', is_included=False, order=5)
    TourInclude.objects.create(tour=tour1, text='Личные расходы', is_included=False, order=6)

# Тур 2: Шёлковый путь премиум
tour2, created = Tour.objects.get_or_create(
    slug='shelkovyy-put-premium',
    defaults={
        'title': 'Шёлковый путь — Премиум',
        'category': 'premium',
        'tour_type': 'historical',
        'direction': 'Ашхабад — Мерв — Марыйский велаят',
        'duration_days': 5,
        'season': 'Весна, Осень',
        'season_spring': True,
        'season_autumn': True,
        'short_description': 'VIP-тур по древним городам Великого Шёлкового пути с проживанием в лучших отелях',
        'full_description': '''
Эксклюзивный маршрут для ценителей истории и комфорта:

• Проживание в отелях 5* (Yyldyz, Oguzkent)
• Частные экскурсии с историками
• Трансферы на комфортабельных автомобилях
• Ужины в национальных ресторанах с живой музыкой
• Посещение археологических объектов UNESCO

Идеально для небольших групп и индивидуальных туристов.
        ''',
        'price_from': 2500,
        'is_popular': True,
        'is_active': True,
        'order': 2,
    }
)
if created:
    print(f"  ✓ {tour2.title}")
    
    TourPrice.objects.create(tour=tour2, category='premium', season='all', price=2500)
    TourInclude.objects.create(tour=tour2, text='Отели 5* с завтраками', is_included=True, order=1)
    TourInclude.objects.create(tour=tour2, text='Частный гид-историк', is_included=True, order=2)
    TourInclude.objects.create(tour=tour2, text='VIP-трансферы', is_included=True, order=3)

# Тур 3: Бюджетный уик-энд
tour3, created = Tour.objects.get_or_create(
    slug='byudzhetnyy-ashkhabad',
    defaults={
        'title': 'Уик-энд в Ашхабаде',
        'category': 'budget',
        'tour_type': 'weekend',
        'direction': 'Ашхабад',
        'duration_days': 3,
        'season': 'Круглый год',
        'season_spring': True,
        'season_summer': True,
        'season_autumn': True,
        'season_winter': True,
        'short_description': 'Короткий тур по столице Туркменистана — идеально для первого знакомства',
        'full_description': '''
Экспресс-знакомство с Ашхабадом за 3 дня:

• Основные достопримечательности столицы
• Музеи и памятники архитектуры
• Национальная кухня в местных ресторанах
• Шопинг на Толкучке (восточный базар)

Отличный вариант для деловых поездок с культурной программой.
        ''',
        'price_from': 450,
        'is_popular': False,
        'is_active': True,
        'order': 3,
    }
)
if created:
    print(f"  ✓ {tour3.title}")
    
    TourPrice.objects.create(tour=tour3, category='budget', season='all', price=450)

print(f"  ✅ Создано туров: {Tour.objects.count()}\n")


# ============================================================
# 2️⃣ КАТЕГОРИИ — ФИЧИ
# ============================================================

print("🎯 Создание фич для категорий...")

features_data = [
    # Budget
    ('budget', 'Экономичное проживание', 'Отели 2-3* или гостевые дома', 'fa-hotel', 1),
    ('budget', 'Групповые экскурсии', 'В составе небольших групп до 15 человек', 'fa-users', 2),
    ('budget', 'Базовый транспорт', 'Комфортабельные автобусы или минивэны', 'fa-bus', 3),
    
    # Standard
    ('standard', 'Комфорт и качество', 'Отели 3-4* с завтраками', 'fa-star', 1),
    ('standard', 'Опытные гиды', 'Русско/англоговорящие профессионалы', 'fa-user-tie', 2),
    ('standard', 'Полный пакет', 'Все входные билеты и трансферы включены', 'fa-check-circle', 3),
    
    # Premium
    ('premium', 'Роскошь и эксклюзив', 'Отели 5* (Yyldyz, Oguzkent)', 'fa-gem', 1),
    ('premium', 'Частные туры', 'Индивидуальные маршруты под запрос', 'fa-crown', 2),
    ('premium', 'VIP-сервис', 'Персональный гид, водитель, консьерж', 'fa-concierge-bell', 3),
]

for cat, title, desc, icon, order in features_data:
    CategoryFeature.objects.get_or_create(
        category=cat,
        title=title,
        defaults={'description': desc, 'icon': icon, 'order': order}
    )

print(f"  ✅ Создано фич: {CategoryFeature.objects.count()}\n")


# ============================================================
# 3️⃣ КЕЙСЫ
# ============================================================

print("💼 Создание кейсов...")

case1, created = Case.objects.get_or_create(
    slug='konferentsiya-oil-gas-2025',
    defaults={
        'title': 'Международная конференция Oil & Gas 2025',
        'direction': 'tourism',
        'client': 'Министерство энергетики Туркменистана',
        'short_description': 'Организация 3-дневной конференции для 200+ участников из 15 стран',
        'full_description': '''
**Задача:**  
Провести международную конференцию нефтегазовой отрасли с участием делегаций из стран СНГ, Европы и Азии.

**Решение:**  
• Полное сопровождение участников (визы, трансферы, проживание)  
• Аренда конференц-залов в отеле Oguzkent  
• Синхронный перевод на 4 языках  
• Культурная программа (Ниса, Дарваза)  
• Организация гала-ужина

**Команда:** 2 менеджера, 4 переводчика, 3 гида
        ''',
        'result': 'Конференция прошла успешно. Отзывы участников — 9.2/10. Клиент заказал организацию следующего форума.',
        'is_featured': True,
        'is_active': True,
        'order': 1,
    }
)
if created:
    print(f"  ✓ {case1.title}")

case2, created = Case.objects.get_or_create(
    slug='konsalting-eksport-kazakhstan',
    defaults={
        'title': 'Консалтинг по экспорту текстиля в Казахстан',
        'direction': 'consulting',
        'client': 'ТОО «Ashgabat Textile»',
        'short_description': 'Помощь в выходе туркменской текстильной компании на рынок Казахстана',
        'full_description': '''
**Задача:**  
Компания производитель хлопковых тканей хотела начать экспорт в Казахстан, но не знала требований рынка.

**Решение:**  
• Анализ рынка текстиля Казахстана  
• Подбор дистрибьюторов в Алматы и Астане  
• Консультации по сертификации и логистике  
• Сопровождение первых контрактов

**Срок:** 4 месяца
        ''',
        'result': 'Компания заключила контракты с 3 дистрибьюторами. Объём экспорта в первый год — $1.2 млн.',
        'is_featured': True,
        'is_active': True,
        'order': 2,
    }
)
if created:
    print(f"  ✓ {case2.title}")

case3, created = Case.objects.get_or_create(
    slug='oborudovanie-forum-ashgabat-2024',
    defaults={
        'title': 'Аренда оборудования для форума Ashgabat 2024',
        'direction': 'linguistics',
        'client': 'Организационный комитет форума',
        'short_description': 'Полный комплекс переводческого оборудования для 500+ участников',
        'full_description': '''
**Задача:**  
Обеспечить синхронный перевод на 6 языков для крупного международного форума.

**Решение:**  
• 12 кабин синхронного перевода  
• 600 беспроводных наушников  
• Звуковое оборудование для 3 залов  
• Техническая поддержка 24/7

**Команда:** 3 техника, 12 переводчиков
        ''',
        'result': 'Оборудование работало без сбоев. Клиент продлил договор на следующий год.',
        'is_featured': False,
        'is_active': True,
        'order': 3,
    }
)
if created:
    print(f"  ✓ {case3.title}")

print(f"  ✅ Создано кейсов: {Case.objects.count()}\n")


# ============================================================
# 4️⃣ ПАРТНЁРЫ
# ============================================================

print("🤝 Создание партнёров...")

partners_data = [
    ('Turkmenistan Airlines', 'https://turkmenistanairlines.tm'),
    ('Oguzkent Hotel', 'https://oguzkent.com'),
    ('Yyldyz Hotel', 'https://yyldyzhotel.com'),
    ('Министерство туризма Туркменистана', 'https://tourism.gov.tm'),
    ('Торгово-промышленная палата', 'https://cci.gov.tm'),
]

for idx, (name, url) in enumerate(partners_data, 1):
    Partner.objects.get_or_create(
        name=name,
        defaults={'url': url, 'order': idx, 'is_active': True}
    )

print(f"  ✅ Создано партнёров: {Partner.objects.count()}\n")


# ============================================================
# 5️⃣ ТЕСТОВЫЕ ЗАЯВКИ
# ============================================================

print("📩 Создание тестовых заявок...")

ContactMessage.objects.get_or_create(
    phone='+7 777 123 4567',
    defaults={
        'name': 'Алексей Иванов',
        'email': 'ivanov@example.com',
        'message': 'Здравствуйте! Интересует тур "Классический Туркменистан" на июнь 2026. Есть ли скидки для группы из 4 человек?'
    }
)

ContactMessage.objects.get_or_create(
    phone='+993 65 123456',
    defaults={
        'name': 'Mahri Gurbanova',
        'email': 'mahri@gmail.com',
        'message': 'Salam! We need interpretation equipment for conference on March 15. Please contact me.'
    }
)

print(f"  ✅ Создано заявок: {ContactMessage.objects.count()}\n")


# ============================================================
# ИТОГО
# ============================================================

print("="*60)
print("✅ ЗАГРУЗКА ЗАВЕРШЕНА!")
print("="*60)
print(f"📍 Туров: {Tour.objects.count()}")
print(f"🎯 Фич категорий: {CategoryFeature.objects.count()}")
print(f"💼 Кейсов: {Case.objects.count()}")
print(f"🤝 Партнёров: {Partner.objects.count()}")
print(f"📩 Заявок: {ContactMessage.objects.count()}")
print("="*60)
print("\n🔐 Теперь войдите в админку: http://127.0.0.1:8000/admin/")
print("   (создайте суперпользователя: python manage.py createsuperuser)\n")
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

### 📄 `assistant\__init__.py`

```python

```

### 📄 `assistant\admin.py`

```python
from django.contrib import admin

# Register your models here.
```

### 📄 `assistant\apps.py`

```python
from django.apps import AppConfig


class AssistantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'assistant'
    verbose_name = 'Виртуальный ассистент'
```

### 📄 `assistant\knowledge.py`

```python
# 📁 assistant/knowledge.py
# 🧠 «Мозг» виртуального ассистента: база знаний + подбор ответа.
# Здесь НЕТ нейросети — ассистент отвечает по ключевым словам.
# Работает мгновенно, бесплатно и без интернета.

import re


# ============================================================
# 1️⃣ БАЗА ЗНАНИЙ
#    keywords — слова, по которым узнаём вопрос
#    answer   — что ответить
#    chips    — кнопки-подсказки под ответом
# ============================================================

KNOWLEDGE = [
    {
        'id': 'greeting',
        'keywords': ['привет', 'здравств', 'добрый день', 'добрый вечер', 'доброе утро',
                     'hello', 'hi', 'салам', 'ассалам'],
        'answer': 'Здравствуйте! 👋 Я виртуальный ассистент TM Impressive. '
                  'Помогу подобрать тур, расскажу об услугах и ценах. О чём расскажу?',
        'chips': ['Какие есть туры?', 'Сколько стоит тур?', 'Как забронировать?'],
    },
    {
        'id': 'tours',
        'keywords': ['тур', 'туры', 'поездк', 'путешеств', 'экскурс', 'маршрут',
                     'мерв', 'дарваза', 'ашхабад', 'куня', 'ургенч', 'каракум'],
        'answer': None,          # ← ответ соберём из базы данных (см. views.py)
        'dynamic': 'tours',
        'chips': ['Сколько стоит тур?', 'В какой сезон лучше ехать?', 'Как забронировать?'],
    },
    {
        'id': 'price',
        'keywords': ['цена', 'цены', 'стоимость', 'стоит', 'сколько', 'бюджет',
                     'дорого', 'дёшево', 'дешево', 'прайс', 'тариф'],
        'answer': 'Цена зависит от тура и категории обслуживания:\n\n'
                  '💰 <b>Бюджет</b> — отель 3*, групповой формат\n'
                  '⭐ <b>Стандарт</b> — отель 4*, завтраки, малые группы\n'
                  '👑 <b>Премиум</b> — отель 5*, всё включено, индивидуально\n\n'
                  'Точные цены каждого тура — в каталоге, в карточке видны все три категории.',
        'chips': ['Открыть каталог туров', 'Как забронировать?'],
    },
    {
        'id': 'booking',
        'keywords': ['бронир', 'заброн', 'заказ', 'заявк', 'оформить', 'купить',
                     'записаться', 'как заказать'],
        'answer': 'Забронировать очень просто:\n\n'
                  '1️⃣ Выберите тур в каталоге\n'
                  '2️⃣ Нажмите «Оставить заявку»\n'
                  '3️⃣ Менеджер свяжется с вами и уточнит детали\n\n'
                  'Или напишите нам сразу в WhatsApp / Telegram — кнопки справа внизу. 📱',
        'chips': ['Ваши контакты', 'Открыть каталог туров'],
    },
    {
        'id': 'contacts',
        'keywords': ['контакт', 'телефон', 'номер', 'связат', 'позвонить', 'написать',
                     'whatsapp', 'ватсап', 'телеграм', 'telegram', 'почта', 'email', 'адрес',
                     'где вы', 'офис'],
        'answer': 'Связаться с нами можно так:\n\n'
                  '📱 WhatsApp: +993 71 34 27 31\n'
                  '✉️ Email: guzelka9494@gmail.com\n'
                  '💬 Telegram и другие мессенджеры — кнопки справа внизу\n\n'
                  'Менеджеры на связи с 9:00 до 18:00, а я — круглосуточно. 🌙',
        'chips': ['Как забронировать?', 'Какие есть туры?'],
    },
    {
        'id': 'season',
        'keywords': ['сезон', 'когда лучше', 'погод', 'весн', 'лет', 'осен', 'зим',
                     'какое время года', 'жарко', 'холодно'],
        'answer': 'Лучшее время для поездок в Туркменистан:\n\n'
                  '🌷 <b>Весна (апрель–май)</b> — комфортно, всё цветёт. Идеально!\n'
                  '🍂 <b>Осень (сентябрь–октябрь)</b> — тепло, мягкий климат. Отлично!\n'
                  '☀️ <b>Лето</b> — очень жарко (+40°C), подходит для коротких туров\n'
                  '❄️ <b>Зима</b> — прохладно, но отличные цены\n\n'
                  'В каталоге можно отфильтровать туры по сезону.',
        'chips': ['Открыть каталог туров', 'Какие есть туры?'],
    },
    {
        'id': 'visa',
        'keywords': ['виза', 'визов', 'документ', 'загранпаспорт', 'приглашен',
                     'въезд', 'граница', 'разрешение'],
        'answer': 'Для въезда в Туркменистан нужна виза и приглашение (visa support). '
                  'Мы полностью берём это на себя: готовим приглашение, '
                  'помогаем с документами и сопровождаем весь процесс.\n\n'
                  'Оформление занимает обычно 10–15 рабочих дней — планируйте заранее. 📄',
        'chips': ['Ваши контакты', 'Как забронировать?'],
    },
    {
        'id': 'consulting',
        'keywords': ['консалтинг', 'бизнес', 'компан', 'рынок', 'юридич', 'регистрац',
                     'партнёр', 'партнер', 'инвест'],
        'answer': 'Направление <b>Бизнес-консалтинг</b>: помогаем выйти на рынок '
                  'Туркменистана, сопровождаем юридически, ищем надёжных местных партнёров '
                  'и выстраиваем стратегию развития. 💼',
        'chips': ['Ваши контакты', 'Что ещё вы делаете?'],
    },
    {
        'id': 'linguistics',
        'keywords': ['перевод', 'лингвист', 'язык', 'синхрон', 'переводчик',
                     'оборудован'],
        'answer': 'Направление <b>Лингвистика</b>: письменные и устные переводы, '
                  'синхронный перевод на мероприятиях, аренда оборудования для конференций.\n\n'
                  'Работаем с английским, китайским и русским языками. 🗣️',
        'chips': ['Ваши контакты', 'Что ещё вы делаете?'],
    },
    {
        'id': 'services',
        'keywords': ['услуг', 'чем занима', 'что вы делаете', 'что ещё', 'что еще',
                     'направлен', 'сферы', 'о компании', 'кто вы'],
        'answer': 'TM Impressive работает в трёх направлениях:\n\n'
                  '✈️ <b>Туризм и MICE</b> — авторские туры, деловые поездки, мероприятия\n'
                  '💼 <b>Бизнес-консалтинг</b> — выход на рынок Туркменистана\n'
                  '🗣️ <b>Лингвистика</b> — переводы и оборудование для конференций',
        'chips': ['Какие есть туры?', 'Ваши контакты'],
    },
    {
        'id': 'mice',
        'keywords': ['mice', 'майс', 'конференц', 'корпоратив', 'мероприят',
                     'делов', 'форум', 'выставк'],
        'answer': 'Организуем деловые поездки и мероприятия под ключ: конференции, '
                  'корпоративы, форумы и выставки. Берём на себя логистику, площадку, '
                  'проживание, переводчиков и культурную программу. 🎤',
        'chips': ['Ваши контакты', 'Как забронировать?'],
    },
    {
        'id': 'thanks',
        'keywords': ['спасибо', 'благодар', 'пока', 'до свидан', 'thanks'],
        'answer': 'Спасибо вам! 💚 Будут вопросы — я всегда здесь. '
                  'Хорошего дня и лёгких путешествий! ✈️',
        'chips': ['Какие есть туры?', 'Ваши контакты'],
    },
]


# 💬 Приветствие при открытии чата
WELCOME = {
    'text': 'Здравствуйте! 👋 Я виртуальный ассистент <b>TM Impressive</b>.\n'
            'Отвечу на вопросы о турах, ценах и услугах в любое время.',
    'chips': ['Какие есть туры?', 'Сколько стоит тур?', 'В какой сезон лучше ехать?', 'Ваши контакты'],
}

# 🤷 Если не поняли вопрос
FALLBACK = {
    'text': 'Хм, кажется, этого я пока не знаю. 🤔\n'
            'Но менеджер точно поможет — напишите нам в WhatsApp или Telegram '
            '(кнопки справа внизу), ответим с 9:00 до 18:00.\n\n'
            'А пока могу рассказать вот о чём:',
    'chips': ['Какие есть туры?', 'Сколько стоит тур?', 'Как забронировать?', 'Ваши контакты'],
}


# ============================================================
# 2️⃣ ПОИСК ОТВЕТА
# ============================================================
def normalize(text):
    """Приводим вопрос к простому виду: маленькие буквы, без лишних знаков."""
    text = text.lower().replace('ё', 'е')
    return re.sub(r'[^a-zа-я0-9\s+]', ' ', text)


def find_intent(question):
    """
    Ищем подходящую тему. Возвращаем словарь темы или None.
    Считаем, сколько ключевых слов совпало — побеждает тема с наибольшим счётом.
    """
    text = normalize(question)
    if not text.strip():
        return None

    best, best_score = None, 0
    for item in KNOWLEDGE:
        score = 0
        for kw in item['keywords']:
            if normalize(kw) in text:
                score += len(kw)      # длинное совпадение весомее короткого
        if score > best_score:
            best, best_score = item, score

    return best
```

### 📄 `assistant\models.py`

```python
from django.db import models

# Create your models here.
```

### 📄 `assistant\tests.py`

```python
from django.test import TestCase

# Create your tests here.
```

### 📄 `assistant\urls.py`

```python
# 📁 assistant/urls.py

from django.urls import path

from . import views

app_name = 'assistant'

urlpatterns = [
    path('ask/', views.ask, name='ask'),
]
```

### 📄 `assistant\views.py`

```python
# 📁 assistant/views.py
# Принимает вопрос пользователя и возвращает ответ в формате JSON.

import json

from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .knowledge import FALLBACK, WELCOME, find_intent


def _tours_answer():
    """Динамический ответ про туры — берём реальные туры из базы."""
    try:
        from tourism.models import Tour
        tours = Tour.objects.filter(is_active=True).order_by('order')[:5]
    except Exception:
        tours = []

    if not tours:
        return ('Сейчас каталог обновляется — совсем скоро здесь появятся туры! 🌍\n'
                'Напишите нам, и менеджер подберёт маршрут вручную.')

    lines = ['Вот что у нас есть прямо сейчас:\n']
    for t in tours:
        price = getattr(t, 'min_price', None) or t.price_from
        lines.append(f'📍 <b>{t.title}</b> — {t.duration_days} дн., от ${int(price)}')
    lines.append('\nПолный список — в каталоге туров. Могу рассказать про любой подробнее!')
    return '\n'.join(lines)


@require_POST
def ask(request):
    """POST {'question': '...'} -> {'answer': '...', 'chips': [...], 'link': {...}}"""
    try:
        data = json.loads(request.body.decode('utf-8'))
    except (ValueError, UnicodeDecodeError):
        data = {}

    question = (data.get('question') or '').strip()[:500]

    # первое открытие чата
    if not question:
        return JsonResponse({'answer': WELCOME['text'], 'chips': WELCOME['chips']})

    intent = find_intent(question)

    if intent is None:
        return JsonResponse({'answer': FALLBACK['text'], 'chips': FALLBACK['chips']})

    if intent.get('dynamic') == 'tours':
        answer = _tours_answer()
    else:
        answer = intent['answer']

    payload = {'answer': answer, 'chips': intent.get('chips', [])}

    # к некоторым ответам добавляем кнопку-ссылку
    if intent['id'] in ('tours', 'price', 'season'):
        payload['link'] = {'url': '/tourism/', 'text': '🌍 Открыть каталог туров'}
    elif intent['id'] in ('booking', 'contacts', 'visa', 'consulting', 'linguistics', 'mice'):
        payload['link'] = {'url': '/contacts/', 'text': '📩 Оставить заявку'}

    return JsonResponse(payload)
```

### 📄 `cases\__init__.py`

```python
# Пустой файл — он говорит Python, что это приложение.
```

### 📄 `cases\admin.py`

```python
"""
================================================================
TM IMPRESSIVE — Cases & Partners Admin
Кейсы и партнёры компании
================================================================
"""
from django.contrib import admin
from django.utils.html import format_html
from .models import Case, Partner


# ============================================================
# КЕЙСЫ (ПОРТФОЛИО)
# ============================================================

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'direction_badge',
        'client',
        'is_featured',
        'is_active',
        'order',
        'created_at',
    )
    list_filter = ('direction', 'is_featured', 'is_active')
    search_fields = ('title', 'client', 'short_description', 'full_description')
    prepopulated_fields = {'slug': ('title',)}
    
    list_editable = ('is_featured', 'is_active', 'order')
    list_per_page = 20
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('📝 Основная информация', {
            'fields': (
                'title',
                'slug',
                'direction',
                'client',
            )
        }),
        ('📄 Описание', {
            'fields': (
                'short_description',
                'full_description',
                'result',
            )
        }),
        ('🖼️ Изображение', {
            'fields': ('image',)
        }),
        ('⚙️ Настройки', {
            'fields': (
                'is_featured',
                'is_active',
                'order',
            )
        }),
    )
    
    def direction_badge(self, obj):
        colors = {
            'tourism': '#0f6b52',       # malachite
            'consulting': '#3b82f6',    # blue
            'linguistics': '#DDB74E',   # brass
        }
        color = colors.get(obj.direction, '#6b7280')
        return format_html(
            '<span style="background: ; color: white; padding: 4px 12px; '
            'border-radius: 12px; font-weight: 600; font-size: 11px;">{}</span>',
            color,
            obj.get_direction_display()
        )
    direction_badge.short_description = 'Направление'


# ============================================================
# ПАРТНЁРЫ
# ============================================================

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'logo_preview',
        'url_link',
        'is_active',
        'order',
    )
    list_filter = ('is_active',)
    search_fields = ('name', 'url')
    
    list_editable = ('is_active', 'order')
    list_per_page = 30
    
    fieldsets = (
        ('📝 Информация о партнёре', {
            'fields': (
                'name',
                'logo',
                'url',
            )
        }),
        ('⚙️ Настройки', {
            'fields': (
                'order',
                'is_active',
            )
        }),
    )
    
    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 120px; '
                'object-fit: contain; border-radius: 4px;" />',
                obj.logo.url
            )
        return '—'
    logo_preview.short_description = 'Логотип'
    
    def url_link(self, obj):
        if obj.url:
            return format_html(
                '<a href="{}" target="_blank" style="color: #0f6b52;">🔗 Открыть</a>',
                obj.url
            )
        return '—'
    url_link.short_description = 'Ссылка'
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


class Partner(models.Model):
    """Партнёр / компания, которой мы доверяем."""
    name = models.CharField('Название', max_length=100)
    logo = models.ImageField('Логотип', upload_to='partners/', blank=True)
    url = models.URLField('Ссылка', blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активен', default=True)
    
    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'
        ordering = ('order',)
    
    def __str__(self):
        return self.name
```

### 📄 `cases\tests.py`

```python
from django.test import TestCase

# Create your tests here.
```

### 📄 `cases\urls.py`

```python
# 📁 cases/urls.py

from django.urls import path

from . import views

app_name = 'cases'

urlpatterns = [
    path('', views.list_view, name='list'),
    path('<slug:slug>/', views.detail_view, name='detail'),
]
```

### 📄 `cases\views.py`

```python
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
"""
import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

load_dotenv()  # читает файл .env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-fallback-key-for-build')

# Включаем DEBUG только локально, на Render автоматически выключится
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Разрешаем все хосты на Render (включая .onrender.com)
ALLOWED_HOSTS = ['*'] if not DEBUG else os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')


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
    'assistant',
    'tailwind', 
    'theme',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Включаем отдачу статики на Render
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
        'DIRS': [
            BASE_DIR / 'templates',  # Папка для кастомных шаблонов админки
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# Автоматически берёт DATABASE_URL от Render или собирает из .env для локалки
DATABASES = {
    'default': dj_database_url.config(
        default=f"postgres://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}",
        conn_max_age=600
    )
}


# Password validation
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
LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Ashgabat'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Куда collectstatic будет собирать файлы для сервера
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'static_custom',  # Папка для кастомного CSS админки
]

# Хранилище WhiteNoise для сжатия и кэширования статики
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- Media files (загружаемые картинки) ---
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- Tailwind CSS ---
TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
   "127.0.0.1",
]

# На сервере нет Windows-путей к Node.js, берем системный npm
NPM_BIN_PATH = os.getenv('NPM_BIN_PATH', 'npm') if not DEBUG else "C:\\Program Files\\nodejs\\npm.cmd"

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
    path('assistant/', include('assistant.urls')),
    path('search/', include(('search.urls', 'search'), namespace='search')), 
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
"""
================================================================
TM IMPRESSIVE — Contacts Admin
Заявки с сайта (контактная форма)
================================================================
"""
from django.contrib import admin
from django.utils.html import format_html
from .models import ContactMessage


# ============================================================
# КОНТАКТНЫЕ ЗАЯВКИ (только просмотр)
# ============================================================

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
        'email',
        'message_preview',
        'created_at',
    )
    list_filter = ('created_at',)
    search_fields = ('name', 'phone', 'email', 'message')
    date_hierarchy = 'created_at'
    
    list_per_page = 50
    
    # Только чтение — менеджеры не должны редактировать заявки
    readonly_fields = ('name', 'phone', 'email', 'message', 'created_at')
    
    fieldsets = (
        ('👤 Контактная информация', {
            'fields': (
                'name',
                'phone',
                'email',
            )
        }),
        ('💬 Сообщение', {
            'fields': ('message',)
        }),
        ('📅 Дата получения', {
            'fields': ('created_at',)
        }),
    )
    
    def message_preview(self, obj):
        """Первые 60 символов сообщения"""
        if len(obj.message) > 60:
            return obj.message[:60] + '...'
        return obj.message
    message_preview.short_description = 'Сообщение'
    
    # Запрет на добавление и удаление через админку
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        # Разрешаем удаление только суперпользователям
        return request.user.is_superuser
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

### 📄 `project_code_parts\PROJECT_CODE_PART_1.md`

```markdown
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

### 📄 `collect_code_split.py`

```python
"""
================================================================
 collect_code.py — Сборщик кода проекта в несколько файлов
 Проект: TM IMPRESSIVE
================================================================

 Что делает скрипт:
 1. Проходит по всем папкам проекта
 2. Находит файлы с кодом (.py, .html, .css, .js и др.)
 3. Разбивает на части по 99 КБ каждая
 4. Сохраняет в папку project_code_parts/

 Как использовать:
 1. Положи этот файл в КОРЕНЬ проекта (рядом с manage.py)
 2. Запусти:  python collect_code.py
 3. Получишь папку project_code_parts/ с файлами PROJECT_CODE_PART_1.md, 2.md, 3.md...
================================================================
"""

import os
from pathlib import Path
from datetime import datetime

# ================================================================
# НАСТРОЙКИ
# ================================================================

PROJECT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_DIR / "project_code_parts"
MAX_PART_SIZE = 99 * 1024  # 99 КБ для каждого файла

INCLUDE_EXTENSIONS = {
    ".py", ".html", ".css", ".js", ".json", ".yml", ".yaml",
    ".toml", ".txt", ".md", ".cfg", ".ini", ".env",
}

INCLUDE_FILENAMES = {
    "Dockerfile", ".gitignore", ".dockerignore", "Procfile",
    ".env", ".env.example",
}

EXCLUDE_DIRS = {
    "venv", ".venv", "env", "node_modules", "__pycache__",
    ".git", ".idea", ".vscode", "staticfiles", "media",
    "dist", "build", ".pytest_cache", ".mypy_cache", "migrations",
    "project_code_parts",  # Исключаем сами файлы
}

EXCLUDE_FILES = {
    "PROJECT_CODE.md", "collect_code.py", "db.sqlite3",
    "package-lock.json", "poetry.lock",
}

MAX_FILE_SIZE = 200_000  # 200 КБ
SECRET_KEYWORDS = ("KEY", "SECRET", "PASSWORD", "TOKEN", "PASS")


# ================================================================
# ФУНКЦИИ
# ================================================================

def should_include(file_path: Path) -> bool:
    """Проверяем — нужно ли включать этот файл в отчёт."""
    if file_path.name in EXCLUDE_FILES:
        return False
    if file_path.name in INCLUDE_FILENAMES:
        return True
    return file_path.suffix.lower() in INCLUDE_EXTENSIONS


def mask_env_secrets(content: str) -> str:
    """Маскируем секретные значения в .env файле."""
    masked_lines = []
    for line in content.splitlines():
        if "=" in line and not line.strip().startswith("#"):
            key = line.split("=", 1)[0].strip().upper()
            if any(word in key for word in SECRET_KEYWORDS):
                masked_lines.append(f"{line.split('=', 1)[0]}=***СКРЫТО***")
                continue
        masked_lines.append(line)
    return "\n".join(masked_lines)


def get_language(file_path: Path) -> str:
    """Определяем язык для подсветки синтаксиса в Markdown."""
    mapping = {
        ".py": "python",
        ".html": "html",
        ".css": "css",
        ".js": "javascript",
        ".json": "json",
        ".yml": "yaml",
        ".yaml": "yaml",
        ".toml": "toml",
        ".md": "markdown",
    }
    if file_path.name == "Dockerfile":
        return "dockerfile"
    return mapping.get(file_path.suffix.lower(), "text")


def collect_files() -> list:
    """Собираем список всех подходящих файлов проекта."""
    collected = []
    for root, dirs, files in os.walk(PROJECT_DIR):
        # Удаляем мусорные папки из обхода
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for filename in sorted(files):
            file_path = Path(root) / filename
            if should_include(file_path):
                collected.append(file_path)

    # Сортируем
    return sorted(collected, key=lambda p: (len(p.relative_to(PROJECT_DIR).parts), str(p)))


def build_tree(files: list) -> str:
    """Строим текстовое дерево проекта из списка файлов."""
    lines = [f"{PROJECT_DIR.name}/"]
    for f in files:
        rel = f.relative_to(PROJECT_DIR)
        indent = "    " * (len(rel.parts) - 1)
        lines.append(f"{indent}├── {rel.name}")
    return "\n".join(lines)


def main():
    """Главная функция — собираем всё в несколько файлов по 99 КБ."""
    files = collect_files()

    if not files:
        print("⚠️ Файлы не найдены! Проверь что скрипт лежит в корне проекта.")
        return

    # Создаём папку для сохранения
    OUTPUT_DIR.mkdir(exist_ok=True)
    print(f"📁 Папка создана: {OUTPUT_DIR.name}/\n")

    # Строим дерево один раз
    tree = build_tree(files)

    # --- Общая шапка для всех файлов ---
    header = f"""# 📦 Код проекта TM IMPRESSIVE

> Собрано: {datetime.now().strftime('%d.%m.%Y %H:%M')}
> Всего файлов: {len(files)}
> Размер каждой части: ~99 КБ

## 🌳 Структура проекта

```
{tree}
```

---

## 📄 Содержимое файлов

"""

    # --- Переменные для разбиения на части ---
    current_part = 1
    current_content = header
    current_size = len(current_content.encode('utf-8'))
    
    total_size = 0
    processed_files = 0
    skipped_files = 0

    # --- Проходим по всем файлам ---
    for file_path in files:
        rel_path = file_path.relative_to(PROJECT_DIR)

        try:
            size = file_path.stat().st_size
            
            # Пропускаем слишком большие файлы
            if size > MAX_FILE_SIZE:
                print(f"  ⏭️  {rel_path} (пропущен — слишком большой: {size // 1024} КБ)")
                skipped_files += 1
                continue

            # Читаем файл
            content = file_path.read_text(encoding="utf-8", errors="replace")

            # Маскируем секреты в .env файлах
            if file_path.name.startswith(".env"):
                content = mask_env_secrets(content)

            lang = get_language(file_path)
            
            # Формируем блок файла
            file_block = f"### 📄 `{rel_path}`\n\n```{lang}\n{content.rstrip()}\n```\n\n"
            file_block_size = len(file_block.encode('utf-8'))

            # Проверяем — поместится ли файл в текущую часть?
            if current_size + file_block_size > MAX_PART_SIZE and current_content != header:
                # Сохраняем текущую часть
                output_file = OUTPUT_DIR / f"PROJECT_CODE_PART_{current_part}.md"
                output_file.write_text(current_content, encoding="utf-8")
                print(f"  💾 Часть {current_part}: {output_file.name} ({current_size // 1024} КБ)")

                # Начинаем новую часть
                current_part += 1
                current_content = header
                current_size = len(current_content.encode('utf-8'))

            # Добавляем файл в текущую часть
            current_content += file_block
            current_size += file_block_size
            total_size += size
            processed_files += 1

            print(f"  ✅ {rel_path}")

        except Exception as e:
            print(f"  ❌ {rel_path}: {e}")
            skipped_files += 1

    # --- Сохраняем последнюю часть ---
    if current_content != header:
        output_file = OUTPUT_DIR / f"PROJECT_CODE_PART_{current_part}.md"
        output_file.write_text(current_content, encoding="utf-8")
        print(f"  💾 Часть {current_part}: {output_file.name} ({current_size // 1024} КБ)")

    # --- Итоговый отчёт ---
    print("\n" + "=" * 60)
    print(f"🎉 Готово! Папка создана: {OUTPUT_DIR.name}/")
    print(f"📊 Файлов обработано: {processed_files}")
    print(f"⏭️  Файлов пропущено: {skipped_files}")
    print(f"📦 Общий размер кода: {total_size // 1024} КБ")
    print(f"📁 Частей создано: {current_part}")
    print("=" * 60)
    print(f"\n📤 Теперь отправь файлы из папки {OUTPUT_DIR.name}/ в чат!")


# --- Точка входа ---
if __name__ == "__main__":
    main()
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

### 📄 `requirements.txt`

```text
��p y t h o n - d o t e n v = = 1 . 2 . 2 
 
 D j a n g o > = 5 . 0 , < 6 . 0 
 
 p s y c o p g 2 - b i n a r y 
 
 P i l l o w 
 
 g u n i c o r n 
 
 d j - d a t a b a s e - u r l 
 
 p y t h o n - d o t e n v 
 
 d j a n g o - t a i l w i n d 
 
 w h i t e n o i s e 
 
 r e q u e s t s 
 
 r i c h 
 
 c o o k i e c u t t e r 
 
 p y t a i l w i n d c s s 
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

### 📄 `assistant\__init__.py`

```python

```

### 📄 `assistant\admin.py`

```python
from django.contrib import admin

# Register your models here.
```

### 📄 `assistant\apps.py`

```python
from django.apps import AppConfig


class AssistantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'assistant'
    verbose_name = 'Виртуальный ассистент'
```

### 📄 `assistant\knowledge.py`

```python
# 📁 assistant/knowledge.py
# 🧠 «Мозг» виртуального ассистента: база знаний + подбор ответа.
# Здесь НЕТ нейросети — ассистент отвечает по ключевым словам.
# Работает мгновенно, бесплатно и без интернета.

import re


# ============================================================
# 1️⃣ БАЗА ЗНАНИЙ
#    keywords — слова, по которым узнаём вопрос
#    answer   — что ответить
#    chips    — кнопки-подсказки под ответом
# ============================================================

KNOWLEDGE = [
    {
        'id': 'greeting',
        'keywords': ['привет', 'здравств', 'добрый день', 'добрый вечер', 'доброе утро',
                     'hello', 'hi', 'салам', 'ассалам'],
        'answer': 'Здравствуйте! 👋 Я виртуальный ассистент TM Impressive. '
                  'Помогу подобрать тур, расскажу об услугах и ценах. О чём расскажу?',
        'chips': ['Какие есть туры?', 'Сколько стоит тур?', 'Как забронировать?'],
    },
    {
        'id': 'tours',
        'keywords': ['тур', 'туры', 'поездк', 'путешеств', 'экскурс', 'маршрут',
                     'мерв', 'дарваза', 'ашхабад', 'куня', 'ургенч', 'каракум'],
        'answer': None,          # ← ответ соберём из базы данных (см. views.py)
        'dynamic': 'tours',
        'chips': ['Сколько стоит тур?', 'В какой сезон лучше ехать?', 'Как забронировать?'],
    },
    {
        'id': 'price',
        'keywords': ['цена', 'цены', 'стоимость', 'стоит', 'сколько', 'бюджет',
                     'дорого', 'дёшево', 'дешево', 'прайс', 'тариф'],
        'answer': 'Цена зависит от тура и категории обслуживания:\n\n'
                  '💰 <b>Бюджет</b> — отель 3*, групповой формат\n'
                  '⭐ <b>Стандарт</b> — отель 4*, завтраки, малые группы\n'
                  '👑 <b>Премиум</b> — отель 5*, всё включено, индивидуально\n\n'
                  'Точные цены каждого тура — в каталоге, в карточке видны все три категории.',
        'chips': ['Открыть каталог туров', 'Как забронировать?'],
    },
    {
        'id': 'booking',
        'keywords': ['бронир', 'заброн', 'заказ', 'заявк', 'оформить', 'купить',
                     'записаться', 'как заказать'],
        'answer': 'Забронировать очень просто:\n\n'
                  '1️⃣ Выберите тур в каталоге\n'
                  '2️⃣ Нажмите «Оставить заявку»\n'
                  '3️⃣ Менеджер свяжется с вами и уточнит детали\n\n'
                  'Или напишите нам сразу в WhatsApp / Telegram — кнопки справа внизу. 📱',
        'chips': ['Ваши контакты', 'Открыть каталог туров'],
    },
    {
        'id': 'contacts',
        'keywords': ['контакт', 'телефон', 'номер', 'связат', 'позвонить', 'написать',
                     'whatsapp', 'ватсап', 'телеграм', 'telegram', 'почта', 'email', 'адрес',
                     'где вы', 'офис'],
        'answer': 'Связаться с нами можно так:\n\n'
                  '📱 WhatsApp: +993 71 34 27 31\n'
                  '✉️ Email: guzelka9494@gmail.com\n'
                  '💬 Telegram и другие мессенджеры — кнопки справа внизу\n\n'
                  'Менеджеры на связи с 9:00 до 18:00, а я — круглосуточно. 🌙',
        'chips': ['Как забронировать?', 'Какие есть туры?'],
    },
    {
        'id': 'season',
        'keywords': ['сезон', 'когда лучше', 'погод', 'весн', 'лет', 'осен', 'зим',
                     'какое время года', 'жарко', 'холодно'],
        'answer': 'Лучшее время для поездок в Туркменистан:\n\n'
                  '🌷 <b>Весна (апрель–май)</b> — комфортно, всё цветёт. Идеально!\n'
                  '🍂 <b>Осень (сентябрь–октябрь)</b> — тепло, мягкий климат. Отлично!\n'
                  '☀️ <b>Лето</b> — очень жарко (+40°C), подходит для коротких туров\n'
                  '❄️ <b>Зима</b> — прохладно, но отличные цены\n\n'
                  'В каталоге можно отфильтровать туры по сезону.',
        'chips': ['Открыть каталог туров', 'Какие есть туры?'],
    },
    {
        'id': 'visa',
        'keywords': ['виза', 'визов', 'документ', 'загранпаспорт', 'приглашен',
                     'въезд', 'граница', 'разрешение'],
        'answer': 'Для въезда в Туркменистан нужна виза и приглашение (visa support). '
                  'Мы полностью берём это на себя: готовим приглашение, '
                  'помогаем с документами и сопровождаем весь процесс.\n\n'
                  'Оформление занимает обычно 10–15 рабочих дней — планируйте заранее. 📄',
        'chips': ['Ваши контакты', 'Как забронировать?'],
    },
    {
        'id': 'consulting',
        'keywords': ['консалтинг', 'бизнес', 'компан', 'рынок', 'юридич', 'регистрац',
                     'партнёр', 'партнер', 'инвест'],
        'answer': 'Направление <b>Бизнес-консалтинг</b>: помогаем выйти на рынок '
                  'Туркменистана, сопровождаем юридически, ищем надёжных местных партнёров '
                  'и выстраиваем стратегию развития. 💼',
        'chips': ['Ваши контакты', 'Что ещё вы делаете?'],
    },
    {
        'id': 'linguistics',
        'keywords': ['перевод', 'лингвист', 'язык', 'синхрон', 'переводчик',
                     'оборудован'],
        'answer': 'Направление <b>Лингвистика</b>: письменные и устные переводы, '
                  'синхронный перевод на мероприятиях, аренда оборудования для конференций.\n\n'
                  'Работаем с английским, китайским и русским языками. 🗣️',
        'chips': ['Ваши контакты', 'Что ещё вы делаете?'],
    },
    {
        'id': 'services',
        'keywords': ['услуг', 'чем занима', 'что вы делаете', 'что ещё', 'что еще',
                     'направлен', 'сферы', 'о компании', 'кто вы'],
        'answer': 'TM Impressive работает в трёх направлениях:\n\n'
                  '✈️ <b>Туризм и MICE</b> — авторские туры, деловые поездки, мероприятия\n'
                  '💼 <b>Бизнес-консалтинг</b> — выход на рынок Туркменистана\n'
                  '🗣️ <b>Лингвистика</b> — переводы и оборудование для конференций',
        'chips': ['Какие есть туры?', 'Ваши контакты'],
    },
    {
        'id': 'mice',
        'keywords': ['mice', 'майс', 'конференц', 'корпоратив', 'мероприят',
                     'делов', 'форум', 'выставк'],
        'answer': 'Организуем деловые поездки и мероприятия под ключ: конференции, '
                  'корпоративы, форумы и выставки. Берём на себя логистику, площадку, '
                  'проживание, переводчиков и культурную программу. 🎤',
        'chips': ['Ваши контакты', 'Как забронировать?'],
    },
    {
        'id': 'thanks',
        'keywords': ['спасибо', 'благодар', 'пока', 'до свидан', 'thanks'],
        'answer': 'Спасибо вам! 💚 Будут вопросы — я всегда здесь. '
                  'Хорошего дня и лёгких путешествий! ✈️',
        'chips': ['Какие есть туры?', 'Ваши контакты'],
    },
]


# 💬 Приветствие при открытии чата
WELCOME = {
    'text': 'Здравствуйте! 👋 Я виртуальный ассистент <b>TM Impressive</b>.\n'
            'Отвечу на вопросы о турах, ценах и услугах в любое время.',
    'chips': ['Какие есть туры?', 'Сколько стоит тур?', 'В какой сезон лучше ехать?', 'Ваши контакты'],
}

# 🤷 Если не поняли вопрос
FALLBACK = {
    'text': 'Хм, кажется, этого я пока не знаю. 🤔\n'
            'Но менеджер точно поможет — напишите нам в WhatsApp или Telegram '
            '(кнопки справа внизу), ответим с 9:00 до 18:00.\n\n'
            'А пока могу рассказать вот о чём:',
    'chips': ['Какие есть туры?', 'Сколько стоит тур?', 'Как забронировать?', 'Ваши контакты'],
}


# ============================================================
# 2️⃣ ПОИСК ОТВЕТА
# ============================================================
def normalize(text):
    """Приводим вопрос к простому виду: маленькие буквы, без лишних знаков."""
    text = text.lower().replace('ё', 'е')
    return re.sub(r'[^a-zа-я0-9\s+]', ' ', text)


def find_intent(question):
    """
    Ищем подходящую тему. Возвращаем словарь темы или None.
    Считаем, сколько ключевых слов совпало — побеждает тема с наибольшим счётом.
    """
    text = normalize(question)
    if not text.strip():
        return None

    best, best_score = None, 0
    for item in KNOWLEDGE:
        score = 0
        for kw in item['keywords']:
            if normalize(kw) in text:
                score += len(kw)      # длинное совпадение весомее короткого
        if score > best_score:
            best, best_score = item, score

    return best
```

### 📄 `assistant\models.py`

```python
from django.db import models

# Create your models here.
```

### 📄 `assistant\tests.py`

```python
from django.test import TestCase

# Create your tests here.
```

### 📄 `assistant\urls.py`

```python
# 📁 assistant/urls.py

from django.urls import path

from . import views

app_name = 'assistant'

urlpatterns = [
    path('ask/', views.ask, name='ask'),
]
```

### 📄 `assistant\views.py`

```python
# 📁 assistant/views.py
# Принимает вопрос пользователя и возвращает ответ в формате JSON.

import json

from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .knowledge import FALLBACK, WELCOME, find_intent


def _tours_answer():
    """Динамический ответ про туры — берём реальные туры из базы."""
    try:
        from tourism.models import Tour
        tours = Tour.objects.filter(is_active=True).order_by('order')[:5]
    except Exception:
        tours = []

    if not tours:
        return ('Сейчас каталог обновляется — совсем скоро здесь появятся туры! 🌍\n'
                'Напишите нам, и менеджер подберёт маршрут вручную.')

    lines = ['Вот что у нас есть прямо сейчас:\n']
    for t in tours:
        price = getattr(t, 'min_price', None) or t.price_from
        lines.append(f'📍 <b>{t.title}</b> — {t.duration_days} дн., от ${int(price)}')
    lines.append('\nПолный список — в каталоге туров. Могу рассказать про любой подробнее!')
    return '\n'.join(lines)


@require_POST
def ask(request):
    """POST {'question': '...'} -> {'answer': '...', 'chips': [...], 'link': {...}}"""
    try:
        data = json.loads(request.body.decode('utf-8'))
    except (ValueError, UnicodeDecodeError):
        data = {}

    question = (data.get('question') or '').strip()[:500]

    # первое открытие чата
    if not question:
        return JsonResponse({'answer': WELCOME['text'], 'chips': WELCOME['chips']})

    intent = find_intent(question)

    if intent is None:
        return JsonResponse({'answer': FALLBACK['text'], 'chips': FALLBACK['chips']})

    if intent.get('dynamic') == 'tours':
        answer = _tours_answer()
    else:
        answer = intent['answer']

    payload = {'answer': answer, 'chips': intent.get('chips', [])}

    # к некоторым ответам добавляем кнопку-ссылку
    if intent['id'] in ('tours', 'price', 'season'):
        payload['link'] = {'url': '/tourism/', 'text': '🌍 Открыть каталог туров'}
    elif intent['id'] in ('booking', 'contacts', 'visa', 'consulting', 'linguistics', 'mice'):
        payload['link'] = {'url': '/contacts/', 'text': '📩 Оставить заявку'}

    return JsonResponse(payload)
```

### 📄 `cases\__init__.py`

```python
# Пустой файл — он говорит Python, что это приложение.
```

### 📄 `cases\admin.py`

```python
# 📁 cases/admin.py

from django.contrib import admin

from .models import Case, Partner


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'get_direction_display', 'is_featured', 'is_active', 'order')
    list_editable = ('is_featured', 'is_active', 'order')
    list_filter = ('direction', 'is_active', 'is_featured', 'created_at')
    search_fields = ('title', 'client', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at',)  # ← только created_at
    
    fieldsets = (
        ('📝 Основное', {
            'fields': ('title', 'slug', 'client', 'direction')
        }),
        ('📄 Контент', {
            'fields': ('short_description', 'full_description', 'image', 'result')
        }),
        ('⚙️ Отображение', {
            'fields': ('is_featured', 'is_active', 'order')
        }),
        ('📅 Дата создания', {
            'fields': ('created_at',),  # ← только created_at
            'classes': ('collapse',)
        }),
    )

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    fields = ('name', 'logo', 'url', 'is_active', 'order')
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


class Partner(models.Model):
    """Партнёр / компания, которой мы доверяем."""
    name = models.CharField('Название', max_length=100)
    logo = models.ImageField('Логотип', upload_to='partners/', blank=True)
    url = models.URLField('Ссылка', blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активен', default=True)
    
    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'
        ordering = ('order',)
    
    def __str__(self):
        return self.name
```

### 📄 `cases\tests.py`

```python
from django.test import TestCase

# Create your tests here.
```

### 📄 `cases\urls.py`

```python
# 📁 cases/urls.py

from django.urls import path

from . import views

app_name = 'cases'

urlpatterns = [
    path('', views.list_view, name='list'),
    path('<slug:slug>/', views.detail_view, name='detail'),
]
```

### 📄 `cases\views.py`

```python
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
"""
import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

load_dotenv()  # читает файл .env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-fallback-key-for-build')

# Включаем DEBUG только локально, на Render автоматически выключится
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Разрешаем все хосты на Render (включая .onrender.com)
ALLOWED_HOSTS = ['*'] if not DEBUG else os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')


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
    'assistant',
    'tailwind', 
    'theme',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Включаем отдачу статики на Render
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
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# Автоматически берёт DATABASE_URL от Render или собирает из .env для локалки
DATABASES = {
    'default': dj_database_url.config(
        default=f"postgres://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}",
        conn_max_age=600
    )
}


# Password validation
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
LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Ashgabat'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Куда collectstatic будет собирать файлы для сервера
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Хранилище WhiteNoise для сжатия и кэширования статики
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- Media files (загружаемые картинки) ---
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- Tailwind CSS ---
TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
   "127.0.0.1",
]

# На сервере нет Windows-путей к Node.js, берем системный npm
NPM_BIN_PATH = os.getenv('NPM_BIN_PATH', 'npm') if not DEBUG else "C:\\Program Files\\nodejs\\npm.cmd"

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
    path('assistant/', include('assistant.urls')),
    path('search/', include(('search.urls', 'search'), namespace='search')), 
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

### 📄 `search\site_content.py`

```python
# 📁 search/site_content.py
# 📄 Статические страницы сайта — чтобы поиск находил и разделы тоже.
#    Хотите добавить страницу в поиск? Просто допишите блок в список.

PAGES = [
    {
        'title': 'Туризм и MICE',
        'url_name': 'tourism:index',
        'icon': 'fa-plane-departure',
        'description': 'Авторские туры по Туркменистану, деловые поездки, '
                       'организация мероприятий и корпоративного отдыха.',
        'keywords': 'туризм mice туры поездки экскурсии мероприятия корпоратив '
                    'отдых путешествия каталог маршруты',
    },
    {
        'title': 'Бизнес-консалтинг',
        'url_name': 'consulting:index',
        'icon': 'fa-briefcase',
        'description': 'Помощь в выходе на рынок Туркменистана, юридическое '
                       'сопровождение и стратегическое развитие бизнеса.',
        'keywords': 'консалтинг бизнес рынок юридическое сопровождение регистрация '
                    'компания партнёры инвестиции стратегия',
    },
    {
        'title': 'Лингвистика и оборудование',
        'url_name': 'linguistics:index',
        'icon': 'fa-language',
        'description': 'Профессиональный письменный и устный перевод, синхронный '
                       'перевод, аренда оборудования для конференций.',
        'keywords': 'лингвистика перевод переводчик синхронный устный письменный '
                    'английский китайский русский оборудование конференция аренда',
    },
    {
        'title': 'О компании',
        'url_name': 'about:index',
        'icon': 'fa-building',
        'description': 'TM Impressive — ваш надёжный партнёр в Туркменистане: '
                       'туризм, консалтинг и лингвистика в одной команде.',
        'keywords': 'о компании кто мы команда история миссия опыт tm impressive '
                    'преимущества',
    },
    {
        'title': 'Контакты',
        'url_name': 'contacts:index',
        'icon': 'fa-envelope',
        'description': 'Телефон, email, мессенджеры и форма заявки — '
                       'свяжитесь с нами удобным способом.',
        'keywords': 'контакты телефон номер email почта адрес офис whatsapp telegram '
                    'связаться написать позвонить заявка',
    },
    {
        'title': 'Кейсы',
        'url_name': 'cases:list',
        'icon': 'fa-trophy',
        'description': 'Реализованные проекты и результаты нашей работы.',
        'keywords': 'кейсы проекты работы портфолио результаты клиенты',
    },
]


def search_pages(query):
    """Ищем страницы по названию, описанию и ключевым словам."""
    q = query.lower()
    found = []
    for page in PAGES:
        haystack = ' '.join([
            page['title'].lower(),
            page['description'].lower(),
            page['keywords'],
        ])
        if q in haystack:
            found.append(page)
    return found
```

### 📄 `search\tests.py`

```python
from django.test import TestCase

# Create your tests here.
```

### 📄 `search\urls.py`

```python
# 📁 search/urls.py

from django.urls import path

from . import views

app_name = 'search'

urlpatterns = [
    path('', views.search, name='index'),
]
```

### 📄 `search\views.py`

```python
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

### 📄 `cases\templatetags\case_tags.py`

```python
# 📁 cases/templatetags/case_tags.py

from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    """{{ dict|get_item:key }} — получить значение из словаря по ключу."""
    if isinstance(dictionary, dict):
        return dictionary.get(key, '')
    return ''
```

### 📄 `search\templatetags\search_extras.py`

```python
# 📁 search/templatetags/search_extras.py
# ⭐ Фильтр подсветки: оборачивает найденные слова в <mark>

import re

from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

MARK_OPEN = '<mark class="bg-brass/50 text-malachite rounded px-0.5">'
MARK_CLOSE = '</mark>'


@register.filter
def highlight(text, query):
    """
    {{ tour.title|highlight:query }}

    Важно: сначала экранируем текст (защита от XSS),
    и только потом вставляем безопасные теги <mark>.
    """
    if not text:
        return ''

    safe_text = escape(str(text))

    if not query:
        return mark_safe(safe_text)

    # разбиваем запрос на слова, короткие отбрасываем
    words = [w for w in re.split(r'\s+', str(query).strip()) if len(w) >= 2]
    if not words:
        return mark_safe(safe_text)

    # длинные слова первыми — иначе короткое совпадение «съест» длинное
    words.sort(key=len, reverse=True)
    pattern = '|'.join(re.escape(escape(w)) for w in words)

    highlighted = re.sub(
        pattern,
        lambda m: MARK_OPEN + m.group(0) + MARK_CLOSE,
        safe_text,
        flags=re.IGNORECASE,
    )
    return mark_safe(highlighted)
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
<section class="relative  bg-malachite text-malachite overflow-hidden">
    <img src="{% static 'images/banners/about_hero.jpg' %}" alt="О компании TM IMPRESSIVE"
         class="absolute inset-0 w-full h-full object-cover object-right opacity-90 pointer-events-none">
    <div class="relative max-w-8xl mx-auto px-10 py-24 ml-3 md:py-32">
        <div class="max-w-4xl ">
        
            <h1 class="text-4xl md:text-6xl font-bold mb-6 leading-tight">
                О компании<br>TM IMPRESSIVE
            </h1>
            <p class="text-lg md:text-xl text-malachite mb-6">
                Туризм, бизнес-консалтинг и лингвистика — три направления, объединённые одной целью: связывать возможности.
                </p>
            
            <a href="{% url 'contacts:index' %}"
               class="inline-block px-8 py-4 rounded-full bg-brass text-malachite font-bold text-lg shadow-xl hover:scale-105 transition-transform duration-200">
                Связаться с нами
            </a>
        </div>
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
```

### 📄 `project_code_parts\PROJECT_CODE_PART_2.md`

```markdown
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
<section class="relative bg-malachite text-white overflow-hidden py-16 md:py-24">
    <img src="{% static 'images/banners/cases_hero.jpg' %}" alt=""
         class="absolute inset-0 w-full h-full object-cover object-right opacity-90 pointer-events-none">
    <div class="relative max-w-8xl mx-auto px-10">
        <div class="max-w-4xl">
            <span class="inline-block px-4 py-1 mb-4 rounded-full bg-brass/20 text-brass text-sm font-semibold">
                🏆 ПОРТФОЛИО
            </span>
            <h1 class="text-4xl md:text-6xl font-extrabold mb-4 leading-tight">
                Реализованные проекты
            </h1>
            <p class="text-lg md:text-xl text-cream/90">
                Вот что нам удалось создать для наших клиентов — от туров до консалтинга
            </p>
        </div>
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
<section class="relative bg-malachite text-white overflow-hidden">
    <img src="{% static 'images/banners/business_hero.jpg' %}" alt=""
         class="absolute inset-0 w-full h-full object-cover object-right opacity-90 pointer-events-none">
    <div class="relative max-w-8xl ml-2 mx-auto px-10 py-24 md:py-32">
        <div class="max-w-4xl">
            <span class="inline-block px-4 py-1 mb-4 rounded-full bg-brass/20 text-brass text-sm font-semibold tracking-wide">
                <i class="fa-solid fa-briefcase mr-2"></i>Бизнес-консалтинг
            </span>
            <h1 class="text-4xl md:text-6xl font-bold mb-6 leading-tight">
                Ваш бизнес-партнёр<br>в Туркменистане
            </h1>
            <p class="text-lg md:text-xl text-cream/90 mb-8">
                Помогаем выйти на рынок, найти партнёров и вести дела уверенно.
            </p>
            <a href="{% url 'contacts:index' %}"
               class="inline-block px-8 py-4 rounded-full bg-brass text-malachite font-bold text-lg shadow-xl hover:scale-105 transition-transform duration-200">
                Обсудить проект
            </a>
        </div>
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
<section class="relative  bg-malachite text-white overflow-hidden  min-h-[90vh] ">
    <img src="{% static 'images/banners/contacts_hero.jpg' %}" alt=""
         class="absolute inset-0 w-full h-full object-cover object-right opacity-90 pointer-events-none">
    <div class="relative max-w-8xl mx-auto px-10 py-24 ml-2 md:py-32">
        <div class="max-w-4xl ">
            <span class="inline-block px-4 py-1 mb-4 rounded-full bg-brass/20 text-brass text-sm font-semibold tracking-wide">
               <i class="fa-solid fa-phone mr-2"></i>Контакты
            </span>
            <h1 class="text-4xl md:text-6xl font-bold mb-6 leading-tight">
                Свяжитесь с нами
            </h1>
            <p class="text-lg md:text-xl text-cream/90 mb-6">
                Ответим на любой вопрос в ближайшее время
            </p>
           
        </div>
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
<section class="relative  bg-malachite text-white overflow-hidden">
    <img src="{% static 'images/banners/linguistics_hero.jpg' %}" alt=""
         class="absolute inset-0 w-full h-full object-cover object-right opacity-90 pointer-events-none">
    <div class="relative max-w-8xl mx-auto px-10 py-24 ml-2 md:py-32">
        <div class="max-w-4xl ">
            <span class="inline-block px-4 py-1 mb-4 rounded-full bg-brass/20 text-brass text-sm font-semibold tracking-wide">
                <i class="fa-solid fa-language mr-2"></i>Лингвистические услуги
            </span>
            <h1 class="text-4xl md:text-6xl font-bold mb-6 leading-tight">
                Переводы без<br>языковых барьеров
            </h1>
            <p class="text-lg md:text-xl text-cream/90 mb-6">
                Профессиональные переводы на английский, китайский, туркменский и русский языки
            </p>
            <div class="flex items-center gap-4 mb-8">
                <img src="https://flagcdn.com/w80/ru.png" alt="Русский" class="w-9 h-6 object-cover rounded shadow ring-1 ring-white/20">
                <img src="https://flagcdn.com/w80/gb.png" alt="Английский" class="w-9 h-6 object-cover rounded shadow ring-1 ring-white/20">
                <img src="https://flagcdn.com/w80/tm.png" alt="Туркменский" class="w-9 h-6 object-cover rounded shadow ring-1 ring-white/20">
                <img src="https://flagcdn.com/w80/cn.png" alt="Китайский" class="w-9 h-6 object-cover rounded shadow ring-1 ring-white/20">
            </div>
            <a href="{% url 'contacts:index' %}"
               class="inline-block px-8 py-4 rounded-full bg-brass text-malachite font-bold text-lg shadow-xl hover:scale-105 transition-transform duration-200">
                Заказать перевод
            </a>
        </div>
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
<section class="relative flex flex-col items-left md:items-start justify-center min-h-[95vh] py-16 px-6 md:px-16 bg-cream overflow-hidden">
    <!-- Баннер: на десктопе cover, но фокус смещён; фон cream закрывает края -->
    <img src="{% static 'images/banners/home_hero_dark.jpg' %}" alt="TM IMPRESSIVE"
         class="absolute inset-0 w-full h-full object-cover object-right pointer-events-none" />

    <!-- Контент поверх (слева, там пустое место на баннере) -->
    <div class="relative z-10 max-w-3xl mt-8 md:ml-20 animate-fade-in-up
                bg-cream/60 md:bg-transparent rounded-2xl p-6 md:p-0 backdrop-blur-sm md:backdrop-blur-none">
        <span class="text-lg text-white tracking-widest uppercase font-bold mb-3 block">Откройте мир с</span>
        <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold text-white mb-6">TM IMPRESSIVE</h1>
        <p class="text-2xl md:text-3xl text-white font-semibold mb-6">Connecting opportunities,<br> elevating futures</p>
        <p class="mb-8 text-white leading-relaxed">
            Туризм, MICE, бизнес-консалтинг и лингвистика — ваш надёжный </br>партнёр в Туркменистане и за его пределами.
        </p>
        <a href="{% url 'contacts:index' %}" class="inline-block bg-brass hover:bg-teal text-forest-dark text-lg font-bold px-8 py-3 rounded-full shadow-lg transition">Оставить заявку</a>
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
```

### 📄 `project_code_parts\PROJECT_CODE_PART_3.md`

```markdown
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

### 📄 `search\site_content.py`

```python
# 📁 search/site_content.py
# 📄 Статические страницы сайта — чтобы поиск находил и разделы тоже.
#    Хотите добавить страницу в поиск? Просто допишите блок в список.

PAGES = [
    {
        'title': 'Туризм и MICE',
        'url_name': 'tourism:index',
        'icon': 'fa-plane-departure',
        'description': 'Авторские туры по Туркменистану, деловые поездки, '
                       'организация мероприятий и корпоративного отдыха.',
        'keywords': 'туризм mice туры поездки экскурсии мероприятия корпоратив '
                    'отдых путешествия каталог маршруты',
    },
    {
        'title': 'Бизнес-консалтинг',
        'url_name': 'consulting:index',
        'icon': 'fa-briefcase',
        'description': 'Помощь в выходе на рынок Туркменистана, юридическое '
                       'сопровождение и стратегическое развитие бизнеса.',
        'keywords': 'консалтинг бизнес рынок юридическое сопровождение регистрация '
                    'компания партнёры инвестиции стратегия',
    },
    {
        'title': 'Лингвистика и оборудование',
        'url_name': 'linguistics:index',
        'icon': 'fa-language',
        'description': 'Профессиональный письменный и устный перевод, синхронный '
                       'перевод, аренда оборудования для конференций.',
        'keywords': 'лингвистика перевод переводчик синхронный устный письменный '
                    'английский китайский русский оборудование конференция аренда',
    },
    {
        'title': 'О компании',
        'url_name': 'about:index',
        'icon': 'fa-building',
        'description': 'TM Impressive — ваш надёжный партнёр в Туркменистане: '
                       'туризм, консалтинг и лингвистика в одной команде.',
        'keywords': 'о компании кто мы команда история миссия опыт tm impressive '
                    'преимущества',
    },
    {
        'title': 'Контакты',
        'url_name': 'contacts:index',
        'icon': 'fa-envelope',
        'description': 'Телефон, email, мессенджеры и форма заявки — '
                       'свяжитесь с нами удобным способом.',
        'keywords': 'контакты телефон номер email почта адрес офис whatsapp telegram '
                    'связаться написать позвонить заявка',
    },
    {
        'title': 'Кейсы',
        'url_name': 'cases:list',
        'icon': 'fa-trophy',
        'description': 'Реализованные проекты и результаты нашей работы.',
        'keywords': 'кейсы проекты работы портфолио результаты клиенты',
    },
]


def search_pages(query):
    """Ищем страницы по названию, описанию и ключевым словам."""
    q = query.lower()
    found = []
    for page in PAGES:
        haystack = ' '.join([
            page['title'].lower(),
            page['description'].lower(),
            page['keywords'],
        ])
        if q in haystack:
            found.append(page)
    return found
```

### 📄 `search\tests.py`

```python
from django.test import TestCase

# Create your tests here.
```

### 📄 `search\urls.py`

```python
# 📁 search/urls.py

from django.urls import path

from . import views

app_name = 'search'

urlpatterns = [
    path('', views.search, name='index'),
]
```

### 📄 `search\views.py`

```python
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

### 📄 `cases\templatetags\case_tags.py`

```python
# 📁 cases/templatetags/case_tags.py

from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    """{{ dict|get_item:key }} — получить значение из словаря по ключу."""
    if isinstance(dictionary, dict):
        return dictionary.get(key, '')
    return ''
```

### 📄 `search\templatetags\search_extras.py`

```python
# 📁 search/templatetags/search_extras.py
# ⭐ Фильтр подсветки: оборачивает найденные слова в <mark>

import re

from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

MARK_OPEN = '<mark class="bg-brass/50 text-malachite rounded px-0.5">'
MARK_CLOSE = '</mark>'


@register.filter
def highlight(text, query):
    """
    {{ tour.title|highlight:query }}

    Важно: сначала экранируем текст (защита от XSS),
    и только потом вставляем безопасные теги <mark>.
    """
    if not text:
        return ''

    safe_text = escape(str(text))

    if not query:
        return mark_safe(safe_text)

    # разбиваем запрос на слова, короткие отбрасываем
    words = [w for w in re.split(r'\s+', str(query).strip()) if len(w) >= 2]
    if not words:
        return mark_safe(safe_text)

    # длинные слова первыми — иначе короткое совпадение «съест» длинное
    words.sort(key=len, reverse=True)
    pattern = '|'.join(re.escape(escape(w)) for w in words)

    highlighted = re.sub(
        pattern,
        lambda m: MARK_OPEN + m.group(0) + MARK_CLOSE,
        safe_text,
        flags=re.IGNORECASE,
    )
    return mark_safe(highlighted)
```

### 📄 `templates\admin\base_site.html`

```html
{% extends "admin/base.html" %}
{% load static %}

{% block title %}{{ title }} | TM IMPRESSIVE{% endblock %}

{% block extrastyle %}
    {{ block.super }}
    <link rel="stylesheet" type="text/css" href="{% static 'admin/css/admin_theme.css' %}">
{% endblock %}

{% block branding %}
<h1 id="site-name">
    <a href="{% url 'admin:index' %}" style="color: #DDB74E; text-decoration: none;">
        <span style="font-weight: 700; font-size: 1.3rem;">TM IMPRESSIVE</span>
        <span style="font-size: 0.85rem; margin-left: 1rem; color: rgba(255,255,255,0.7);">Управление</span>
    </a>
</h1>
{% endblock %}

{% block nav-global %}
<div style="color: rgba(255,255,255,0.85); font-size: 0.9rem;">
    {% if user.is_active and user.is_staff %}
        👤 {{ user.get_username }} |
        <a href="{% url 'admin:password_change' %}" style="color: white; text-decoration: none; margin: 0 1rem;">🔐 Пароль</a>
        <a href="/" target="_blank" style="color: #DDB74E; text-decoration: none; margin: 0 1rem;">🌐 На сайт</a>
        <a href="{% url 'admin:logout' %}" style="color: white; text-decoration: none; margin-left: 1rem;">Выход</a>
    {% endif %}
</div>
{% endblock %}
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
<section class="relative  bg-malachite text-malachite overflow-hidden">
    <img src="{% static 'images/banners/about_hero.jpg' %}" alt="О компании TM IMPRESSIVE"
         class="absolute inset-0 w-full h-full object-cover object-right opacity-90 pointer-events-none">
    <div class="relative max-w-8xl mx-auto px-10 py-24 ml-3 md:py-32">
        <div class="max-w-4xl ">
        
            <h1 class="text-4xl md:text-6xl font-bold mb-6 leading-tight">
                О компании<br>TM IMPRESSIVE
            </h1>
            <p class="text-lg md:text-xl text-malachite mb-6">
                Туризм, бизнес-консалтинг и лингвистика — три направления, объединённые одной целью: связывать возможности.
                </p>
            
            <a href="{% url 'contacts:index' %}"
               class="inline-block px-8 py-4 rounded-full bg-brass text-malachite font-bold text-lg shadow-xl hover:scale-105 transition-transform duration-200">
                Связаться с нами
            </a>
        </div>
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
<section class="relative bg-malachite text-white overflow-hidden py-16 md:py-24">
    <img src="{% static 'images/banners/cases_hero.jpg' %}" alt=""
         class="absolute inset-0 w-full h-full object-cover object-right opacity-90 pointer-events-none">
    <div class="relative max-w-8xl mx-auto px-10">
        <div class="max-w-4xl">
            <span class="inline-block px-4 py-1 mb-4 rounded-full bg-brass/20 text-brass text-sm font-semibold">
                🏆 ПОРТФОЛИО
            </span>
            <h1 class="text-4xl md:text-6xl font-extrabold mb-4 leading-tight">
                Реализованные проекты
            </h1>
            <p class="text-lg md:text-xl text-cream/90">
                Вот что нам удалось создать для наших клиентов — от туров до консалтинга
            </p>
        </div>
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
<section class="relative bg-malachite text-white overflow-hidden">
    <img src="{% static 'images/banners/business_hero.jpg' %}" alt=""
         class="absolute inset-0 w-full h-full object-cover object-right opacity-90 pointer-events-none">
    <div class="relative max-w-8xl ml-2 mx-auto px-10 py-24 md:py-32">
        <div class="max-w-4xl">
            <span class="inline-block px-4 py-1 mb-4 rounded-full bg-brass/20 text-brass text-sm font-semibold tracking-wide">
                <i class="fa-solid fa-briefcase mr-2"></i>Бизнес-консалтинг
            </span>
            <h1 class="text-4xl md:text-6xl font-bold mb-6 leading-tight">
                Ваш бизнес-партнёр<br>в Туркменистане
            </h1>
            <p class="text-lg md:text-xl text-cream/90 mb-8">
                Помогаем выйти на рынок, найти партнёров и вести дела уверенно.
            </p>
            <a href="{% url 'contacts:index' %}"
               class="inline-block px-8 py-4 rounded-full bg-brass text-malachite font-bold text-lg shadow-xl hover:scale-105 transition-transform duration-200">
                Обсудить проект
            </a>
        </div>
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
 <!--
<section class="py-16 md:py-24 bg-cream">
    <div class="max-w-6xl mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-extrabold text-center text-malachite mb-4">
            Пакеты консалтинга
        </h2>
        <p class="text-center text-ink/70 mb-12 max-w-2xl mx-auto">
            Выберите формат сотрудничества под ваши задачи
        </p>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-stretch">
            -->
        
            <!-- РАЗОВАЯ -->
             <!--
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
            -->
            <!-- СОПРОВОЖДЕНИЕ (популярный) -->
             <!--
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
            -->
            <!-- ПОЛНЫЙ -->
             <!--
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
-->
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
<section class="relative  bg-malachite text-white overflow-hidden  min-h-[90vh] ">
    <img src="{% static 'images/banners/contacts_hero.jpg' %}" alt=""
         class="absolute inset-0 w-full h-full object-cover object-right opacity-90 pointer-events-none">
    <div class="relative max-w-8xl mx-auto px-10 py-24 ml-2 md:py-32">
        <div class="max-w-4xl ">
            <span class="inline-block px-4 py-1 mb-4 rounded-full bg-brass/20 text-brass text-sm font-semibold tracking-wide">
               <i class="fa-solid fa-phone mr-2"></i>Контакты
            </span>
            <h1 class="text-4xl md:text-6xl font-bold mb-6 leading-tight">
                Свяжитесь с нами
            </h1>
            <p class="text-lg md:text-xl text-cream/90 mb-6">
                Ответим на любой вопрос в ближайшее время
            </p>
           
        </div>
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
<section class="relative  bg-malachite text-white overflow-hidden">
    <img src="{% static 'images/banners/linguistics_hero.jpg' %}" alt=""
         class="absolute inset-0 w-full h-full object-cover object-right opacity-90 pointer-events-none">
    <div class="relative max-w-8xl mx-auto px-10 py-24 ml-2 md:py-32">
        <div class="max-w-4xl ">
            <span class="inline-block px-4 py-1 mb-4 rounded-full bg-brass/20 text-brass text-sm font-semibold tracking-wide">
                <i class="fa-solid fa-language mr-2"></i>Лингвистические услуги
            </span>
            <h1 class="text-4xl md:text-6xl font-bold mb-6 leading-tight">
                Переводы без<br>языковых барьеров
            </h1>
            <p class="text-lg md:text-xl text-cream/90 mb-6">
                Профессиональные переводы 
            </p>
            <div class="flex items-center gap-4 mb-8">
                <img src="https://flagcdn.com/w80/ru.png" alt="Русский" class="w-9 h-6 object-cover rounded shadow ring-1 ring-white/20">
                <img src="https://flagcdn.com/w80/gb.png" alt="Английский" class="w-9 h-6 object-cover rounded shadow ring-1 ring-white/20">
                <img src="https://flagcdn.com/w80/tm.png" alt="Туркменский" class="w-9 h-6 object-cover rounded shadow ring-1 ring-white/20">
                <img src="https://flagcdn.com/w80/cn.png" alt="Китайский" class="w-9 h-6 object-cover rounded shadow ring-1 ring-white/20">
            </div>
            <a href="{% url 'contacts:index' %}"
               class="inline-block px-8 py-4 rounded-full bg-brass text-malachite font-bold text-lg shadow-xl hover:scale-105 transition-transform duration-200">
                Заказать перевод
            </a>
        </div>
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
                <p class="text-ink/70">Документы, статьи, договоры и любые тексты с соблюдением стиля и терминологии</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-comments"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Устный перевод</h3>
                <p class="text-ink/70">Последовательный и синхронный перевод на встречах, переговорах и презентациях</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-scale-balanced"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Юридический перевод</h3>
                <p class="text-ink/70">Договоры, контракты и правовые документы с нотариальным оформлением</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-microchip"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Технический перевод</h3>
                <p class="text-ink/70">Инструкции, спецификации и техдокументация с точными техническими терминами</p>
            </div>

            <div class="group bg-white rounded-2xl p-8 shadow-md hover:shadow-xl transition-all duration-300">
                <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite text-brass text-2xl mb-4 transition-colors duration-300 group-hover:bg-brass group-hover:text-malachite">
                    <i class="fa-solid fa-stamp"></i>
                </div>
                <h3 class="text-xl font-bold text-malachite mb-2">Нотариальный перевод</h3>
                <p class="text-ink/70">Заверенные переводы для официальных органов и государственных учреждений</p>
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
                <!-- КАРТИНКА -->
                <div class="mb-6 h-48 bg-malachite/5 rounded-xl flex items-center justify-center overflow-hidden">
                    <img src="{% static 'images/equipment/booth.jpg' %}" 
                        alt="Кабина синхронного перевода"
                        class="w-full h-full object-cover">
                </div>
                <div class="flex items-start gap-4 mb-6">
                    <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-teal text-white text-2xl shrink-0">
                        <i class="fa-solid fa-microphone"></i>
                    </div>
                    <div>
                        <h3 class="text-2xl font-bold text-malachite mb-2">Кабины синхронного перевода</h3>
                        
                    </div>
                </div>
                <ul class="space-y-2 text-ink/70 mb-6">
                    <li class="flex items-center gap-2">
                        
                        <i class="fa-solid fa-check text-teal"></i>
                        Высокая звукоизоляция
                    </li>
                    <li class="flex items-center gap-2">
                        <i class="fa-solid fa-check text-teal"></i>
                        Включена стойка для наушников
                    </li>
                </ul>
            </div>

            <!-- Приёмники и наушники -->
            <div class="bg-gradient-to-br from-cream to-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-all border-l-4 border-brass">
                <!-- КАРТИНКА -->
                <div class="mb-6 h-48 bg-brass/5 rounded-xl flex items-center justify-center overflow-hidden">
                    <img src="{% static 'images/equipment/headphones.jpg' %}" 
                        alt="Система передачи звука"
                        class="w-full h-full object-cover">
                </div>
                <div class="flex items-start gap-4 mb-6">
                    <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-brass text-malachite text-2xl shrink-0">
                        <i class="fa-solid fa-headphones"></i>
                    </div>
                    <div>
                       <h3 class="text-2xl font-bold text-malachite mb-2">Проводная и беспроводная система передачи звука</h3>
                    </div>
                </div>
                <ul class="space-y-2 text-ink/70 mb-6">
                     <li>Беспроводные приёмники (количество по заказу)</li>
                     <li>Удобные и лёгкие наушники</li>
                </ul>
            </div>

        </div>

        <!-- Доп. оборудование -->
        <div class="mb-14">
            <h3 class="text-2xl font-bold text-malachite mb-6">Дополнительное оборудование</h3>
            <!-- СТАЛО: иконки Material -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                
                <div class="flex flex-col items-center gap-3 p-6 rounded-2xl bg-white shadow-sm hover:shadow-md transition">
                    <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite/10 text-malachite text-3xl">
                        <i class="fa-solid fa-microphone"></i>
                    </div>
                    <p class="font-semibold text-malachite text-center">Микрофоны</p>
                </div>

                <div class="flex flex-col items-center gap-3 p-6 rounded-2xl bg-white shadow-sm hover:shadow-md transition">
                    <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite/10 text-malachite text-3xl">
                        <i class="fa-solid fa-volume-high"></i>
                    </div>
                    <p class="font-semibold text-malachite text-center">Акустические системы</p>
                </div>

                <div class="flex flex-col items-center gap-3 p-6 rounded-2xl bg-white shadow-sm hover:shadow-md transition">
                    <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite/10 text-malachite text-3xl">
                        <i class="fa-solid fa-display"></i>
                    </div>
                    <p class="font-semibold text-malachite text-center">Экраны и проекторы</p>
                </div>

                <div class="flex flex-col items-center gap-3 p-6 rounded-2xl bg-white shadow-sm hover:shadow-md transition">
                    <div class="w-14 h-14 flex items-center justify-center rounded-xl bg-malachite/10 text-malachite text-3xl">
                        <i class="fa-solid fa-sliders"></i>
                    </div>
                    <p class="font-semibold text-malachite text-center">Смешивающее оборудование</p>
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
<section class="relative flex flex-col items-left md:items-start justify-center min-h-[95vh] py-16 px-6 md:px-16 bg-cream overflow-hidden">
    <!-- Баннер: на десктопе cover, но фокус смещён; фон cream закрывает края -->
    <img src="{% static 'images/banners/home_hero_dark.jpg' %}" alt="TM IMPRESSIVE"
         class="absolute inset-0 w-full h-full object-cover object-right pointer-events-none" />

    <!-- Контент поверх (слева, там пустое место на баннере) -->
    <div class="relative z-10 max-w-3xl mt-8 md:ml-20 animate-fade-in-up
                bg-cream/60 md:bg-transparent rounded-2xl p-6 md:p-0 backdrop-blur-sm md:backdrop-blur-none">
        <span class="text-lg text-white tracking-widest uppercase font-bold mb-3 block">Откройте мир с</span>
        <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold text-white mb-6">TM IMPRESSIVE</h1>
        <p class="text-2xl md:text-3xl text-white font-semibold mb-6">Connecting opportunities,<br> elevating futures</p>
        <p class="mb-8 text-white leading-relaxed">
            Туризм, MICE, бизнес-консалтинг и лингвистика — ваш надёжный </br>партнёр в Туркменистане и за его пределами.
        </p>
        <a href="{% url 'contacts:index' %}" class="inline-block bg-brass hover:bg-teal text-forest-dark text-lg font-bold px-8 py-3 rounded-full shadow-lg transition">Оставить заявку</a>
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
                    Авторские туры по Туркменистану, деловые поездки, организация мероприятий и корпоративного отдыха
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
                    Помощь в выходе на рынок Туркменистана, юридическое сопровождение и стратегическое развитие бизнеса
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
                    Профессиональный перевод, синхронный перевод на мероприятиях и аренда оборудования для конференций
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
                    Английский, китайский и русский: коммуникация без барьеров
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

### 📄 `static_custom\admin\css\admin_theme.css`

```css
/* 
================================================================
TM IMPRESSIVE — Premium Admin Theme
Palette: Malachite #0f6b52, Brass #DDB74E, Cream #F8F5F0
================================================================
*/

:root {
    --primary: #0f6b52;        /* Malachite - main brand */
    --accent: #DDB74E;         /* Brass - highlights */
    --bg-light: #F8F5F0;       /* Cream - backgrounds */
    --dark: #0a4a37;           /* Forest dark - headers */
    --text-muted: #6b7280;
}

/* ============================================================
   HEADER & BRANDING
============================================================ */
#header {
    background: linear-gradient(135deg, var(--dark) 0%, var(--primary) 100%) !important;
    color: white !important;
    padding: 1rem 2rem !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

#branding h1 {
    color: var(--accent) !important;
    font-weight: 700 !important;
    font-size: 1.5rem !important;
    letter-spacing: 0.5px;
}

#branding h1 a:link,
#branding h1 a:visited {
    color: var(--accent) !important;
}

#user-tools {
    color: rgba(255,255,255,0.9) !important;
}

#user-tools a {
    color: white !important;
    border-bottom: 1px solid transparent;
    transition: border-color 0.2s;
}

#user-tools a:hover {
    border-bottom-color: var(--accent);
}

/* ============================================================
   SIDEBAR / NAVIGATION
============================================================ */
.module h2,
.module caption,
.inline-group h2 {
    background: var(--primary) !important;
    color: white !important;
    font-weight: 600 !important;
    padding: 0.75rem 1rem !important;
    border-radius: 6px 6px 0 0;
}

#content-main {
    background: var(--bg-light);
    padding: 2rem;
    border-radius: 8px;
}

/* ============================================================
   BUTTONS
============================================================ */
.button,
input[type=submit],
input[type=button],
.submit-row input,
a.button {
    background: var(--primary) !important;
    color: white !important;
    border: none !important;
    padding: 0.65rem 1.5rem !important;
    border-radius: 6px !important;
    font-weight: 600 !important;
    transition: all 0.2s !important;
    cursor: pointer !important;
}

.button:hover,
input[type=submit]:hover,
input[type=button]:hover,
.submit-row input:hover,
a.button:hover {
    background: var(--dark) !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 8px rgba(15, 107, 82, 0.3) !important;
}

.button.default,
input[type=submit].default,
.submit-row input.default {
    background: var(--accent) !important;
    color: var(--dark) !important;
}

.button.default:hover {
    background: #c8952a !important;
}

/* Delete button */
.deletelink,
.deletelink-box a {
    background: #dc2626 !important;
}

.deletelink:hover {
    background: #b91c1c !important;
}

/* ============================================================
   TABLES
============================================================ */
#result_list {
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

#result_list thead th {
    background: var(--primary) !important;
    color: white !important;
    font-weight: 600 !important;
    padding: 1rem !important;
    border: none !important;
}

#result_list tbody tr {
    background: white;
    transition: background 0.15s;
}

#result_list tbody tr:hover {
    background: var(--bg-light) !important;
}

#result_list tbody tr:nth-child(even) {
    background: #fafafa;
}

#result_list tbody tr:nth-child(even):hover {
    background: var(--bg-light) !important;
}

#result_list tbody td {
    padding: 0.75rem 1rem;
    border-bottom: 1px solid #e5e7eb;
}

/* ============================================================
   CHANGELIST FILTERS
============================================================ */
#changelist-filter {
    background: white;
    border-radius: 8px;
    padding: 1rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

#changelist-filter h2 {
    background: var(--dark) !important;
    color: white !important;
    margin: -1rem -1rem 1rem -1rem;
    padding: 0.75rem 1rem;
    border-radius: 8px 8px 0 0;
}

#changelist-filter h3 {
    color: var(--primary);
    font-weight: 600;
    margin-top: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--accent);
}

#changelist-filter a {
    color: var(--primary);
    transition: color 0.2s;
}

#changelist-filter a:hover {
    color: var(--accent);
}

#changelist-filter li.selected a {
    color: var(--accent) !important;
    font-weight: 600;
}

/* ============================================================
   FORMS
============================================================ */
.form-row {
    padding: 1rem;
    border-bottom: 1px solid #e5e7eb;
}

.form-row:hover {
    background: var(--bg-light);
}

/* Все input-поля по ширине контейнера */
input[type=text],
input[type=email],
input[type=url],
input[type=number],
textarea,
select,
.admin-readonly {
    width: 100% !important;
    border: 2px solid #e5e7eb !important;
    border-radius: 6px !important;
    padding: 0.65rem 0.75rem !important;
    transition: border-color 0.2s !important;
    font-size: 1rem !important;
    box-sizing: border-box !important;
    max-width: 100% !important;
}

/* На узких экранах тоже нормально */
@media (max-width: 768px) {
    input[type=text],
    input[type=email],
    input[type=url],
    input[type=number],
    textarea,
    select {
        width: 100% !important;
        min-width: 200px !important;
    }
}

/* Textarea больше */
textarea {
    min-height: 150px !important;
    resize: vertical !important;
}

input[type=text]:focus,
input[type=email]:focus,
input[type=url]:focus,
input[type=number]:focus,
textarea:focus,
select:focus {
    border-color: var(--primary) !important;
    outline: none !important;
    box-shadow: 0 0 0 3px rgba(15, 107, 82, 0.1) !important;
}

/* ============================================================
   INLINE FORMS (Gallery, Prices, Days)
============================================================ */
.inline-group {
    background: white;
    border-radius: 8px;
    padding: 1rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.inline-related {
    background: var(--bg-light);
    padding: 1rem;
    margin-bottom: 0.75rem;
    border-radius: 6px;
    border-left: 3px solid var(--accent);
}

.inline-related:hover {
    border-left-color: var(--primary);
}

/* ============================================================
   MESSAGES & NOTIFICATIONS
============================================================ */
.messagelist {
    padding: 0;
    margin: 0 0 1.5rem 0;
}

.messagelist li {
    padding: 1rem 1.5rem;
    margin-bottom: 0.75rem;
    border-radius: 6px;
    font-weight: 500;
    display: block;
}

.messagelist .success {
    background: #d1fae5;
    color: #065f46;
    border-left: 4px solid #10b981;
}

.messagelist .warning {
    background: #fef3c7;
    color: #92400e;
    border-left: 4px solid #f59e0b;
}

.messagelist .error {
    background: #fee2e2;
    color: #991b1b;
    border-left: 4px solid #ef4444;
}

.messagelist .info {
    background: #dbeafe;
    color: #1e40af;
    border-left: 4px solid #3b82f6;
}

/* ============================================================
   BREADCRUMBS
============================================================ */
.breadcrumbs {
    background: white !important;
    padding: 0.75rem 2rem !important;
    border-radius: 6px;
    margin-bottom: 1.5rem;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
}

.breadcrumbs a {
    color: var(--primary) !important;
    font-weight: 500;
}

.breadcrumbs a:hover {
    color: var(--accent) !important;
}

/* ============================================================
   DASHBOARD (INDEX PAGE)
============================================================ */
.module h2 a {
    color: white !important;
}

.module h2 a:hover {
    color: var(--accent) !important;
}

#content-main .module {
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    margin-bottom: 1.5rem;
}

.module table {
    width: 100%;
}

.module tbody tr:hover {
    background: var(--bg-light);
}

/* ============================================================
   BOOLEAN ICONS (✓ / ✗)
============================================================ */
img[src*="icon-yes"],
img[alt="True"] {
    /* Green checkmark */
    filter: hue-rotate(90deg) saturate(3);
}

img[src*="icon-no"],
img[alt="False"] {
    /* Red X */
    opacity: 0.5;
}

/* ============================================================
   PAGINATION
============================================================ */
.paginator {
    color: var(--text-muted);
    padding: 1rem 0;
}

.paginator a {
    color: var(--primary);
    padding: 0.5rem 0.75rem;
    border-radius: 4px;
    transition: all 0.2s;
}

.paginator a:hover {
    background: var(--primary);
    color: white;
}

/* ============================================================
   HELP TEXT
============================================================ */
.help,
.helptext {
    color: var(--text-muted);
    font-size: 0.875rem;
    font-style: italic;
}

/* ============================================================
   RESPONSIVE TWEAKS
============================================================ */
@media (max-width: 1024px) {
    #content-main {
        padding: 1rem;
    }
}


/* ============================================================
   SIDEBAR / NAVIGATION
============================================================ */
#sidebar {
    background: linear-gradient(180deg, var(--dark) 0%, var(--primary) 100%) !important;
    border-right: 3px solid var(--accent) !important;
    padding: 1rem 0 !important;
    color: white !important;
}

#sidebar h2 {
    background: transparent !important;
    color: var(--accent) !important;
    padding: 1rem !important;
    margin: 0 !important;
    font-weight: 700 !important;
    font-size: 1.1rem !important;
    border-bottom: 2px solid var(--accent) !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
}

#sidebar .module {
    background: transparent !important;
    border: none !important;
    margin: 0.5rem 0 !important;
    padding: 0 !important;
}

#sidebar .module h3 {
    background: rgba(255, 255, 255, 0.1) !important;
    color: white !important;
    padding: 0.75rem 1rem !important;
    margin: 0 !important;
    font-weight: 600 !important;
    border-left: 3px solid var(--accent) !important;
    transition: all 0.2s !important;
    cursor: pointer !important;
}

#sidebar .module h3:hover {
    background: rgba(255, 255, 255, 0.2) !important;
    padding-left: 1.25rem !important;
}

#sidebar .module ul {
    list-style: none !important;
    padding: 0 !important;
    margin: 0 !important;
    background: rgba(0, 0, 0, 0.2) !important;
}

#sidebar .module ul li {
    margin: 0 !important;
    padding: 0 !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
}

#sidebar .module ul li a {
    display: block !important;
    padding: 0.75rem 1rem 0.75rem 1.5rem !important;
    color: rgba(255, 255, 255, 0.9) !important;
    text-decoration: none !important;
    transition: all 0.2s !important;
    font-size: 0.95rem !important;
    border-left: 2px solid transparent !important;
}

#sidebar .module ul li a:hover {
    background: rgba(255, 255, 255, 0.1) !important;
    color: var(--accent) !important;
    border-left-color: var(--accent) !important;
    padding-left: 1.75rem !important;
}

#sidebar .module ul li a.selected {
    background: var(--accent) !important;
    color: var(--dark) !important;
    font-weight: 600 !important;
    border-left-color: var(--dark) !important;
}

/* Search box в sidebar */
#id_q {
    background: rgba(255, 255, 255, 0.95) !important;
    border: 2px solid var(--accent) !important;
    border-radius: 6px !important;
    padding: 0.75rem !important;
    margin: 1rem !important;
    width: calc(100% - 2rem) !important;
    box-sizing: border-box !important;
    color: var(--dark) !important;
}

#id_q:focus {
    background: white !important;
    box-shadow: 0 0 0 3px rgba(221, 183, 78, 0.3) !important;
}

/* ============================================================
   COLORS
============================================================ */
:root {
    --dark: #0a4a37;
    --primary: #0f6b52;
    --accent: #DDB74E;
    --bg-light: #F8F5F0;
}

/* ============================================================
   SIDEBAR / NAVIGATION
============================================================ */

/* Скрыть sidebar на главной странице */
body.change-list #sidebar,
body.dashboard #sidebar {
    display: none !important;
}

#sidebar {
    background: linear-gradient(180deg, #0a4a37 0%, #0f6b52 100%) !important;
    border-right: 3px solid #DDB74E !important;
    padding: 1rem 0 !important;
    color: white !important;
}

#sidebar h2 {
    background: transparent !important;
    color: #DDB74E !important;
    padding: 1rem !important;
    margin: 0 !important;
    font-weight: 700 !important;
    font-size: 1.1rem !important;
    border-bottom: 2px solid #DDB74E !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
}

#sidebar .module {
    background: transparent !important;
    border: none !important;
    margin: 0.5rem 0 !important;
    padding: 0 !important;
}

#sidebar .module h3 {
    background: rgba(255, 255, 255, 0.1) !important;
    color: white !important;
    padding: 0.75rem 1rem !important;
    margin: 0 !important;
    font-weight: 600 !important;
    border-left: 3px solid #DDB74E !important;
    transition: all 0.2s !important;
}

#sidebar .module h3:hover {
    background: rgba(255, 255, 255, 0.2) !important;
    padding-left: 1.25rem !important;
}

#sidebar .module ul {
    list-style: none !important;
    padding: 0 !important;
    margin: 0 !important;
    background: rgba(0, 0, 0, 0.2) !important;
}

#sidebar .module ul li {
    margin: 0 !important;
    padding: 0 !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
}

#sidebar .module ul li a {
    display: block !important;
    padding: 0.65rem 1rem 0.65rem 1.5rem !important;
    color: rgba(255, 255, 255, 0.85) !important;
    text-decoration: none !important;
    transition: all 0.2s !important;
    font-size: 0.9rem !important;
    border-left: 2px solid transparent !important;
}

#sidebar .module ul li a:hover {
    background: rgba(255, 255, 255, 0.1) !important;
    color: #DDB74E !important;
    border-left-color: #DDB74E !important;
    padding-left: 1.75rem !important;
}

#sidebar .module ul li a.selected {
    background: #DDB74E !important;
    color: #0a4a37 !important;
    font-weight: 600 !important;
    border-left-color: #0a4a37 !important;
}


/* ============================================================
   OVERRIDE ALL BLUE COLORS TO MALACHITE
============================================================ */

/* Все модули (CASES, CONTACTS, TOURISM и т.д.) */
.module h2,
.module caption,
.inline-group h2,
#changelist-filter h2 {
    background: #0f6b52 !important;
    color: white !important;
}

/* Все кнопки и ссылки в sidebar */
#sidebar a,
.module a {
    color: #0f6b52 !important;
}

#sidebar a:hover,
.module a:hover {
    color: #DDB74E !important;
}

/* Все синие элементы -> зелёные */
.button,
input[type=submit],
input[type=button],
a.button {
    background: #0f6b52 !important;
    color: white !important;
}

.button:hover,
input[type=submit]:hover,
a.button:hover {
    background: #0a4a37 !important;
}

/* Search-фильтры */
#changelist-filter h3 {
    color: #0f6b52 !important;
    border-bottom-color: #DDB74E !important;
}

#changelist-filter a {
    color: #0f6b52 !important;
}

#changelist-filter a:hover {
    color: #DDB74E !important;
}

#changelist-filter li.selected a {
    color: #DDB74E !important;
    font-weight: 600 !important;
}

/* Таблицы */
#result_list thead th {
    background: #0f6b52 !important;
    color: white !important;
}

/* Breadcrumbs */
.breadcrumbs a {
    color: #0f6b52 !important;
}

.breadcrumbs a:hover {
    color: #DDB74E !important;
}

/* ============================================================
   FIX: BUTTONS OVERFLOW & PADDING
============================================================ */

/* Кнопка "Найти" и все кнопки поиска */
.searchbar button,
input[type=submit].default,
.submit-row input,
a.button,
button {
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
    display: inline-block !important;
    min-width: 60px !important;
    padding: 0.6rem 1.2rem !important;
    font-size: 0.95rem !important;
    line-height: 1.2 !important;
    height: auto !important;
    vertical-align: middle !important;
}

/* Конкретно кнопка Search */
.searchbar input[type=submit],
form .submit-row input[type=submit] {
    padding: 0.65rem 1.5rem !important;
    background: #0f6b52 !important;
    color: white !important;
    border: none !important;
    border-radius: 4px !important;
    font-weight: 600 !important;
}

.searchbar input[type=submit]:hover,
form .submit-row input[type=submit]:hover {
    background: #0a4a37 !important;
}

/* Header градиент - если нужно убрать */
#header {
    background: #0f6b52 !important;
    /* Или если нужен градиент, то: */
    /* background: linear-gradient(135deg, #0a4a37 0%, #0f6b52 100%) !important; */
}
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

/* Золотой градиент для текста */
  .text-gold-gradient {
      background: linear-gradient(135deg, #c8952a 0%, #DDB74E 40%, #f0d080 65%, #DDB74E 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      display: inline-block; /* ВАЖНО! */
      font-weight: 700;
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
    <div class="relative max-w-8xl mx-auto px-10 py-24 ml-2 md:py-32 text-center">
        <div class="max-w-4xl mx-auto">
            <span class="inline-block px-10 py-1 mb-4 rounded-full bg-brass/20 text-brass text-sm font-semibold tracking-wide">
                 <i class="fa-solid fa-mountain-sun mr-2"></i>Туризм и MICE
            </span>
            <h1 class="text-4xl md:text-6xl font-bold mb-6 leading-tight">
                Откройте<br>Туркменистан
            </h1>
            <p class="text-lg md:text-xl text-cream/90 mb-6">
                 Пустыня Каракумы, горы Копетдаг, Каспийское море </br>и древний Шёлковый путь — в одном путешествии.
            </p>
            
            <a href="{% url 'contacts:index' %}"
               class="inline-block px-8 py-4 rounded-full bg-brass text-malachite font-bold text-lg shadow-xl hover:scale-105 transition-transform duration-200">
                Подобрать тур
            </a>
        </div>
    </div>
</section>

<!-- ===== MICE УСЛУГИ ===== -->
<section class="py-10 bg-cream border-b border-malachite/10">
    <div class="max-w-6xl mx-auto px-4">
        <div class="flex items-center gap-3 mb-6">
            <span class="inline-block px-3 py-1 rounded-full bg-malachite/10 text-malachite text-sm font-semibold">
                <i class="fa-solid fa-briefcase mr-1"></i>MICE услуги
            </span>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-4">

            <a href="{% url 'contacts:index' %}?service=visa"
               class="group flex flex-col items-center gap-3 bg-white rounded-2xl p-5 shadow-sm hover:shadow-md hover:border-malachite border border-transparent transition-all text-center">
                <div class="w-12 h-12 flex items-center justify-center rounded-xl bg-malachite/10 text-malachite text-2xl group-hover:bg-malachite group-hover:text-brass transition-colors">
                    <i class="fa-solid fa-passport"></i>
                </div>
                <span class="font-semibold text-malachite">Виза</span>
            </a>

            <a href="{% url 'contacts:index' %}?service=tickets"
               class="group flex flex-col items-center gap-3 bg-white rounded-2xl p-5 shadow-sm hover:shadow-md hover:border-malachite border border-transparent transition-all text-center">
                <div class="w-12 h-12 flex items-center justify-center rounded-xl bg-malachite/10 text-malachite text-2xl group-hover:bg-malachite group-hover:text-brass transition-colors">
                    <i class="fa-solid fa-plane-departure"></i>
                </div>
                <span class="font-semibold text-malachite">Билеты</span>
            </a>

            <a href="{% url 'contacts:index' %}?service=tours"
               class="group flex flex-col items-center gap-3 bg-white rounded-2xl p-5 shadow-sm hover:shadow-md hover:border-malachite border border-transparent transition-all text-center">
                <div class="w-12 h-12 flex items-center justify-center rounded-xl bg-malachite/10 text-malachite text-2xl group-hover:bg-malachite group-hover:text-brass transition-colors">
                    <i class="fa-solid fa-map-location-dot"></i>
                </div>
                <span class="font-semibold text-malachite">Туры</span>
            </a>

            <a href="{% url 'contacts:index' %}?service=transport"
               class="group flex flex-col items-center gap-3 bg-white rounded-2xl p-5 shadow-sm hover:shadow-md hover:border-malachite border border-transparent transition-all text-center">
                <div class="w-12 h-12 flex items-center justify-center rounded-xl bg-malachite/10 text-malachite text-2xl group-hover:bg-malachite group-hover:text-brass transition-colors">
                    <i class="fa-solid fa-van-shuttle"></i>
                </div>
                <span class="font-semibold text-malachite">Транспорт</span>
            </a>

            <a href="{% url 'contacts:index' %}?service=hotel"
               class="group flex flex-col items-center gap-3 bg-white rounded-2xl p-5 shadow-sm hover:shadow-md hover:border-malachite border border-transparent transition-all text-center">
                <div class="w-12 h-12 flex items-center justify-center rounded-xl bg-malachite/10 text-malachite text-2xl group-hover:bg-malachite group-hover:text-brass transition-colors">
                    <i class="fa-solid fa-hotel"></i>
                </div>
                <span class="font-semibold text-malachite">Гостиница</span>
            </a>

        </div>
    </div>
</section>

<!-- ===== ЗАГОЛОВОК КАТАЛОГА ===== -->
<section class="py-12 bg-white border-t border-malachite/10">
    <div class="max-w-6xl mx-auto px-4">
        <div class="flex items-center gap-3">
            <div class="w-1 h-10 bg-malachite rounded-full"></div>
            <h2 class="text-3xl md:text-4xl font-extrabold text-malachite">
                Каталог туров
            </h2>
        </div>
        <p class="text-ink/60 mt-2">Выбирайте готовые маршруты или составьте свой</p>
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
                    <li>📞 <a href="tel:+99363878057" class="hover:text-[#D4AF37] transition">+993 63 87 80 57</a></li>
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
      <span class="text-xl md:text-2xl font-extrabold text-gold-gradient  uppercase tracking-widest
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
      
        <a href="{% url 'tourism:index' %}" class="font-semibold text-gold-gradient hover:opacity-80 transition">Туризм и MICE</a>
      <a href="{% url 'consulting:index' %}" class="font-semibold text-gold-gradient hover:opacity-80 transition">Бизнес-консалтинг</a>
      <a href="{% url 'linguistics:index' %}" class="font-semibold text-gold-gradient hover:opacity-80 transition">Лингвистика и оборудование</a>
      <a href="{% url 'about:index' %}" class="font-semibold text-gold-gradient hover:opacity-80 transition">О компании</a>
      <a href="{% url 'contacts:index' %}" class="font-semibold text-gold-gradient hover:opacity-80 transition">Контакты</a>

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
