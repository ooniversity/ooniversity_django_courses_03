from django.contrib import admin
from feedbacks.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
	list_display = ['from_email', 'time_seconds']

	def time_seconds(self, obj):
	    return obj.create_date.strftime(" %H:%M:%S")

	time_seconds.short_description = "Sent at"


admin.site.register(Feedback, FeedbackAdmin)