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
