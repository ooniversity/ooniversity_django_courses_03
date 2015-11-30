from django.contrib import admin
from .models import Coach
import models

class CoachAdmin(admin.ModelAdmin):
    #list_display = ['user.name', 'user.last_name', 'gender', 'skype', 'description']
    list_filter = ['user__is_staff']
    pass

admin.site.register(Coach, CoachAdmin)
