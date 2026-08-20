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
