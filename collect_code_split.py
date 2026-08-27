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
