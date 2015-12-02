from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from courses.models import Course, Lesson
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import generic

#def detail (request, pk):
    #courses = Course.objects.get(id=pk)
    #lessons = Lesson.objects.all()
    #context = {'lessons': lessons, 'courses': pk}
    #return render(request, '/home/vitalii/DJ101/ooniversity/ooniversity_django_courses_03/courses/templates/courses/detail.html', context)

class IndexView(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.all()


class DetailView(generic.DetailView):
    model = Course
    template_name = 'courses/courses/detail.html'

class LessonsView(generic.ListView): 
    template_name = 'courses/courses/detail.html' 
    context_object_name = 'lessons' 
    
    def get_queryset(self): 
        return Lesson.objects.all()







#def detail(request, a):
    #lessons = Lesson.objects.all()
    #context = {'lessons': lessons}
    #p = get_object_or_404(Course, pk=a)
    #return render_to_response('/home/vitalii/DJ101/ooniversity/ooniversity_django_courses_03/courses/templates/courses/detail.html', {'course': p}) 
    #return render(request, '/home/vitalii/DJ101/ooniversity/ooniversity_django_courses_03/courses/templates/courses/detail.html', context)



