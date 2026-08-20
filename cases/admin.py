from django.contrib import admin
from .models import Case


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'direction', 'client', 'is_featured', 'is_active', 'order')
    list_editable = ('is_featured', 'is_active', 'order')
    list_filter = ('direction', 'is_featured', 'is_active')
    search_fields = ('title', 'client')
    prepopulated_fields = {'slug': ('title',)}
