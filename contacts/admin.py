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
