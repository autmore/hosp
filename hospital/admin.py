from django.contrib import admin

from django.contrib import admin
from .models import Diagnosis, Heal

# Регистрируем модель Diagnosis в административной панели
@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('name', 'doctor', 'date_added')
    search_fields = ('name', 'doctor__username')
    list_filter = ('doctor', 'date_added')
    ordering = ('-date_added',)

@admin.register(Heal)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('treatment', 'date_added')
    search_fields = ('treatment', 'doctor__username')
    list_filter = ('treatment', 'date_added')
    ordering = ('-date_added',)
