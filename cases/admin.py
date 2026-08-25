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