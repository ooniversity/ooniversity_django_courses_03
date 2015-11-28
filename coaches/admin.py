# -*- coding: utf-8 -*-
from django.contrib import admin
from coaches.models import Coach

class CoachAdmin(admin.ModelAdmin):

    list_display  = ('first_name', 'last_name', 'gender', 'skype', 'description')
    list_filter = ('user__is_staff', )

    def first_name(self, obj):
        return obj.first_name()

    def last_name(self, obj):
        return obj.last_name()

    def is_staff(self, obj):
        return obj.is_staff()

admin.site.register(Coach, CoachAdmin)
