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

