from django.contrib import admin
from coaches.models import Coach
from django.contrib.auth.models import User

# Register your models here.
class CoachAdmin(admin.ModelAdmin):
	list_display = ['full_name', 'gender', 'skype', 'desciption']
	list_filter = ['user__is_staff']

admin.site.register(Coach, CoachAdmin)