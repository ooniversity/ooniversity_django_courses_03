from django.contrib import admin
from django.contrib.auth.models import User
from coaches.models import *

class CoachAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'skype', 'description']
    list_filter = ['gender', 'user__is_staff']

admin.site.register(Coach, CoachAdmin)