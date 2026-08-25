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