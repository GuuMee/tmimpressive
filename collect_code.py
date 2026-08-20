"""
================================================================
 collect_code.py — Сборщик кода проекта в один файл
 Проект: TM IMPRESSIVE
================================================================

 Что делает скрипт:
 1. Проходит по всем папкам проекта
 2. Находит файлы с кодом (.py, .html, .css, .js и др.)
 3. Пропускает мусорные папки (venv, node_modules, __pycache__)
 4. Собирает всё в один файл PROJECT_CODE.md
    с красивыми заголовками и деревом проекта

 Как использовать:
 1. Положи этот файл в КОРЕНЬ проекта (рядом с manage.py)
 2. Запусти:  python collect_code.py
 3. Получишь файл PROJECT_CODE.md — отправь его в чат!
================================================================
"""

# --- Импорты стандартной библиотеки ---
import os          # работа с файловой системой
from pathlib import Path   # удобная работа с путями
from datetime import datetime  # дата создания отчёта

# ================================================================
# НАСТРОЙКИ
# ================================================================

# Папка проекта = папка где лежит этот скрипт
PROJECT_DIR = Path(__file__).resolve().parent

# Имя итогового файла
OUTPUT_FILE = PROJECT_DIR / "PROJECT_CODE.md"

# Какие расширения файлов собираем
INCLUDE_EXTENSIONS = {
    ".py",      # Python код
    ".html",    # шаблоны Django
    ".css",     # стили
    ".js",      # JavaScript
    ".json",    # конфиги (package.json и т.д.)
    ".yml",     # docker-compose и др.
    ".yaml",
    ".toml",    # конфиги (tailwind, pyproject)
    ".txt",     # requirements.txt
    ".md",      # документация
    ".cfg",     # setup.cfg и др.
    ".ini",     # конфиги
    ".env",     # ⚠️ структура .env (секреты замаскируем!)
}

# Файлы без расширения которые тоже нужны
# ⚠️ Файлы-точки (.env, .gitignore) Python не считает "расширением",
#    поэтому их указываем здесь по имени!
INCLUDE_FILENAMES = {
    "Dockerfile",
    ".gitignore",
    ".dockerignore",
    "Procfile",
    ".env",
    ".env.example",
}

# Папки которые ПОЛНОСТЬЮ пропускаем
EXCLUDE_DIRS = {
    "venv", ".venv", "env",          # виртуальные окружения
    "node_modules",                   # npm пакеты
    "__pycache__",                    # кэш Python
    ".git",                           # git репозиторий
    ".idea", ".vscode",               # настройки редакторов
    "staticfiles",                    # собранная статика
    "media",                          # загруженные файлы
    "dist", "build",                  # сборки
    ".pytest_cache", ".mypy_cache",   # кэши инструментов
    "migrations",                     # ⚠️ миграции Django (обычно не нужны)
}

# Конкретные файлы которые пропускаем
EXCLUDE_FILES = {
    "PROJECT_CODE.md",     # сам итоговый файл (чтобы не собрать себя)
    "collect_code.py",     # сам скрипт
    "db.sqlite3",          # база данных
    "package-lock.json",   # огромный lock-файл
    "poetry.lock",
}

# Максимальный размер одного файла (в байтах) — защита от огромных файлов
MAX_FILE_SIZE = 200_000  # ~200 КБ

# Ключевые слова для маскировки секретов в .env
SECRET_KEYWORDS = ("KEY", "SECRET", "PASSWORD", "TOKEN", "PASS")


# ================================================================
# ФУНКЦИИ
# ================================================================

def should_include(file_path: Path) -> bool:
    """Проверяем — нужно ли включать этот файл в отчёт."""
    # Пропускаем файлы из чёрного списка
    if file_path.name in EXCLUDE_FILES:
        return False
    # Берём файлы из белого списка имён (Dockerfile и т.п.)
    if file_path.name in INCLUDE_FILENAMES:
        return True
    # Берём файлы с нужным расширением
    return file_path.suffix.lower() in INCLUDE_EXTENSIONS


def mask_env_secrets(content: str) -> str:
    """Маскируем секретные значения в .env файле.

    Было:  SECRET_KEY=django-insecure-abc123
    Стало: SECRET_KEY=***СКРЫТО***
    """
    masked_lines = []
    for line in content.splitlines():
        # Ищем строки вида KEY=value с секретными словами
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


def collect_files() -> list[Path]:
    """Собираем список всех подходящих файлов проекта."""
    collected = []
    for root, dirs, files in os.walk(PROJECT_DIR):
        # Удаляем мусорные папки из обхода (изменяем dirs на месте!)
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for filename in sorted(files):
            file_path = Path(root) / filename
            if should_include(file_path):
                collected.append(file_path)

    # Сортируем: сначала корень, потом по алфавиту
    return sorted(collected, key=lambda p: (len(p.relative_to(PROJECT_DIR).parts), str(p)))


def build_tree(files: list[Path]) -> str:
    """Строим текстовое дерево проекта из списка файлов."""
    lines = [f"{PROJECT_DIR.name}/"]
    for f in files:
        rel = f.relative_to(PROJECT_DIR)
        indent = "    " * (len(rel.parts) - 1)
        lines.append(f"{indent}├── {rel.name}")
    return "\n".join(lines)


def main():
    """Главная функция — собираем всё в PROJECT_CODE.md."""
    files = collect_files()

    if not files:
        print("⚠️ Файлы не найдены! Проверь что скрипт лежит в корне проекта.")
        return

    parts = []

    # --- Шапка отчёта ---
    parts.append("# 📦 Код проекта TM IMPRESSIVE")
    parts.append(f"\n> Собрано: {datetime.now().strftime('%d.%m.%Y %H:%M')}")
    parts.append(f"> Всего файлов: {len(files)}\n")

    # --- Дерево проекта ---
    parts.append("## 🌳 Структура проекта\n")
    parts.append("```")
    parts.append(build_tree(files))
    parts.append("```\n")

    # --- Содержимое каждого файла ---
    parts.append("## 📄 Содержимое файлов\n")

    total_size = 0
    for file_path in files:
        rel_path = file_path.relative_to(PROJECT_DIR)

        try:
            size = file_path.stat().st_size
            # Пропускаем слишком большие файлы
            if size > MAX_FILE_SIZE:
                parts.append(f"### ⚠️ `{rel_path}` — пропущен (слишком большой: {size // 1024} КБ)\n")
                continue

            # Читаем файл (utf-8 с заменой битых символов)
            content = file_path.read_text(encoding="utf-8", errors="replace")

            # Маскируем секреты в .env файлах
            if file_path.name.startswith(".env"):
                content = mask_env_secrets(content)

            total_size += size
            lang = get_language(file_path)

            parts.append(f"### 📄 `{rel_path}`\n")
            parts.append(f"```{lang}")
            parts.append(content.rstrip())
            parts.append("```\n")

            print(f"  ✅ {rel_path}")

        except Exception as e:
            parts.append(f"### ❌ `{rel_path}` — ошибка чтения: {e}\n")
            print(f"  ❌ {rel_path}: {e}")

    # --- Записываем итоговый файл ---
    OUTPUT_FILE.write_text("\n".join(parts), encoding="utf-8")

    print("\n" + "=" * 50)
    print(f"🎉 Готово! Файл создан: {OUTPUT_FILE.name}")
    print(f"📊 Файлов собрано: {len(files)}")
    print(f"📦 Общий размер кода: {total_size // 1024} КБ")
    print("=" * 50)
    print("\n📤 Теперь отправь PROJECT_CODE.md в чат!")


# --- Точка входа ---
if __name__ == "__main__":
    main()
