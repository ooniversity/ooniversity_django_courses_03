from django.contrib import admin
from coaches.models import Coach
from django.contrib.auth.models import User


class CoachAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'gender', 'skype', 'description']
	#list_display = ['gender', 'skype', 'description']
	list_filter = (['user__is_staff', admin.BooleanFieldListFilter],)
	search_fields = ['first_name', 'last_name', 'gender', 'skype', 'description']
	#search_fields = ['gender', 'skype', 'description']

class UserAdmin(admin.ModelAdmin):
	fields = ['username', 'password', 'first_name', 'last_name', 'email', 'is_staff']
	

admin.site.register(Coach, CoachAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)





