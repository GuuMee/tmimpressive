# 📁 cases/templatetags/case_tags.py

from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    """{{ dict|get_item:key }} — получить значение из словаря по ключу."""
    if isinstance(dictionary, dict):
        return dictionary.get(key, '')
    return ''