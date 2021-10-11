from django.contrib import admin
from .models import Memory
# Register your models here.


class MemoryAdmin(admin.ModelAdmin):
    list_display = ('location', 'comment', 'created_at', 'user')


admin.site.register(Memory, MemoryAdmin)