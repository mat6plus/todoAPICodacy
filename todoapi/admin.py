from django.contrib import admin
from todoapi.models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'user','completed')


admin.site.register(Todo, TodoAdmin)