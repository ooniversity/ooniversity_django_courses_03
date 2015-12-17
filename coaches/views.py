from django.shortcuts import render
from django.views import generic
from courses.models import Course, Lesson
from coaches.models import Coach


# Create your views here.


class CoachDetailView(generic.DetailView):
    model = Coach
    template_name = 'coaches/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CoachDetailView, self).get_context_data(**kwargs)
        context['coach_for_courses'] = Course.objects.filter(coach=self.kwargs.get(self.pk_url_kwarg, None))
        context['assistant_for_courses'] = Course.objects.filter(assistant=self.kwargs.get(self.pk_url_kwarg, None))
        return context

