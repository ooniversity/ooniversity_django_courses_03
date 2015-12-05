from django.contrib import admin
from coaches.models import Coach
from django.contrib.auth.models import User


class CoachAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'skype', 'description']
    list_filter = ['gender', 'user__is_staff']
    search_fields = ['user', 'user__first_name', 'user__last_name', 'user_email', 'gender', 'skype', ]


    def first_name(self, obj):
    	return obj.user.first_name
    def last_name(self, obj):
    	return obj.user.last_name
    name = property(first_name)
    surname = property(last_name)


admin.site.register(Coach, CoachAdmin)

