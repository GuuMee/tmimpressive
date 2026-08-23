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
