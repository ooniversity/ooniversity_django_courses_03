from django.contrib import admin
from django.contrib.admin import BooleanFieldListFilter
from coaches.models import Coach
from django.contrib.auth.models import User

class CoachAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'gender', 'email', 'skype', 'description']
    list_filter = (('user__is_staff',BooleanFieldListFilter),)

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'first_name', 'last_name', 'email', 'is_staff']
    list_filter = (('is_staff',BooleanFieldListFilter),)
    fields = ['username', 'password', 'first_name', 'last_name', 'email', 'is_staff']


admin.site.register(Coach, CoachAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
