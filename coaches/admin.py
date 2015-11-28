from django.contrib import admin
from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'gender', 'skype', 'description']
    list_filter = ['gender', 'user__is_staff']


admin.site.register(Coach, CoachAdmin)
