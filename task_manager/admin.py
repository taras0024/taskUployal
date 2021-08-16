from django.contrib import admin

from task_manager.models import Tag, Task


@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated',)


@admin.register(Task)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'updated', 'priority', 'status',)
