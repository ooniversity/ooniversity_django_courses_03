from django.contrib import admin
from coaches.models import Coach
from django.contrib.auth.models import User


class UsersInline(admin.StackedInline):
    model = User
    extra = 0
    list_display = (('subject', 'description', 'order'), )

class CoachAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'skype', 'description']
    list_filter = ['gender', 'user__is_staff']


    def first_name(self, obj): return obj.user.first_name
    def last_name(self, obj): return obj.user.last_name


admin.site.register(Coach, CoachAdmin)
# Register your models here.
