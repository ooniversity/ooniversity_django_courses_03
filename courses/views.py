from django.shortcuts import render
from courses.models import Course, Lesson
from django.views.generic import ListView, DetailView

class CourseListView(ListView):
    model = Course
    template_name = '../templates/index.html'



class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons_list'] = Lesson.objects.filter(course=self.object)
        return context