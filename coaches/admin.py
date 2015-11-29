from django.contrib import admin
from django.contrib.auth.models import User
from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ['name','surname', 'gender', 'skype','description']
    list_filter = ['user__is_staff']


admin.site.register(Coach, CoachAdmin)
