from django.contrib import admin
from courses.models import Coach

class CoachAdmin(admin.ModelAdmin):
	list_display = ['get_username', 'gender', 'skype', 'description', ]

	def get_username(self, obj):
		return obj.user

	get_username.short_description = 'name'

admin.site.register(Coach, CoachAdmin)

