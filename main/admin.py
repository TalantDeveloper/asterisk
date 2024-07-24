from django.contrib import admin
from .models import Server, Costumer


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ip', 'port', 'username')
    list_display_links = ('id', 'name', 'ip', 'port', 'username')
    list_filter = ('name', 'ip', 'port', 'username')
    search_fields = ('name', 'ip', 'port', 'username')
    empty_value_display = ';('


@admin.register(Costumer)
class CostumerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'server')
    list_display_links = ('id', 'user', 'server')
    list_filter = ('user', 'server')
    search_fields = ('user', 'server')
    empty_value_display = '---'

