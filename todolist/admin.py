from django.contrib import admin
from todolist.models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ['description', 'is_completed', 'user']
admin.site.register(Todo, TodoAdmin)