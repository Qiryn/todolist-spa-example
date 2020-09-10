from django.contrib import admin

from . import models

# Register your models here.
@admin.register(models.TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    pass