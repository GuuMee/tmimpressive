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
