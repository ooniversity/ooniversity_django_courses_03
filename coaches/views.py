from django.shortcuts import render
from courses.models import Course
from coaches.models import Coach
from django.views.generic.detail import DetailView
from pybursa.utils import MixinCoachContext


class CoachDetailView(MixinCoachContext, DetailView):
    model = Coach
    template_name = 'coaches/detail.html'
    


'''
def detail(request, pk):
	coaches = Coach.objects.get(id=pk)
	courses = Course.objects.filter(coach=pk)
	assistants = Course.objects.filter(assistant=pk)
	return render(request, 'coaches/detail.html', {'coaches': coaches, 'courses': courses, 'assistants': assistants})
'''
