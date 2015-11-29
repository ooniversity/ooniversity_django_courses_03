from django.contrib import admin
from coaches.models import Coach
# Register your models here.

class CoachAdmin(admin.ModelAdmin):

	list_display = ['name', 'surname', 'gender', 'skype', 'description']
	list_display_links = ['name', 'surname']
	list_filter = ['user__is_staff', 'skype']

admin.site.register(Coach, CoachAdmin)

from django.db import models
from django.contrib.auth.models import User

#pass to users: useruser