from django.contrib import admin
from .models import Country

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('cca2', 'name_common', 'region', 'population')
    list_filter = ('region', 'subregion')
    search_fields = ('name_common', 'name_official', 'cca2')
    ordering = ('name_common',)