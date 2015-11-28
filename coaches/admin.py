from django.contrib import admin
from coaches.models import Coach

# Register your models here.
class CoachAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'gender', 'skype', 'desciption']

admin.site.register(Coach, CoachAdmin)