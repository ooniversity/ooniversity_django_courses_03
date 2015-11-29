from django.contrib import admin
from courses.models import Coach
from django.contrib.auth.admin import UserAdmin as UA
from django.contrib.auth.models import User


class CoachAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'gender', 'skype', 'description',)
    list_filter = ('user__is_staff',)


    def name(self, object):
        return object.user.first_name


    def last_name(self, object):
        return object.user.last_name

# class UserAdmin(UA):
#     fields = ('username', 'password', 'first_name', 'second_name' )


admin.site.register(Coach, CoachAdmin)
