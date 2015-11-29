from django.contrib import admin
from .models import Coach

class CoachAdmin(admin.ModelAdmin):
    list_display = ['user.name', 'user.last_name', 'gender', 'skype', 'description']
    list_filter = ['user.name']

admin.site.register(Coach, CoachAdmin)
