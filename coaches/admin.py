from django.contrib import admin
from .models import Coach
import models

class CoachAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'get_name', 'gender', 'skype', 'description']
    list_filter = ['user__is_staff']

admin.site.register(Coach, CoachAdmin)
