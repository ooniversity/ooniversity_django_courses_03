from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course
from django.views.generic.detail import DetailView


class CoachContextMixin(object):

	def get_context_data(self, **kwargs):
		context = super(CoachContextMixin, self).get_context_data(**kwargs)
		context['course'] = Course.objects.filter(coach=self.kwargs.get(self.pk_url_kwarg, None))
		context['assist'] =  Course.objects.filter(assistant=self.kwargs.get(self.pk_url_kwarg, None))
		return context


class CoachDetailView(CoachContextMixin, DetailView):
	model = Coach
	context_object_name = 'coach'
	template_name = 'coaches/detail.html'

