from django.shortcuts import render
#from django.http import HttpResponse
from django.views import generic
from courses.models import Course, Lesson


# Create your views here.
#def index_courses(request):
    #courses_list = Course.objects.all()
    #context = {'courses_list': courses_list}
    #return render(request, 'index.html', context)
    #return render(request, 'index.html', {'courses_list': Course.objects.all()})

class DetailView(generic.DetailView):
    model = Course
    template_name = 'courses/detail.html'

    #def get_queryset(self):
        #return Lesson.objects.filter(subject='Lesson1')

    #def detail(request):
    #return HttpResponse("Hello, it is index.")
    #return render(request, 'index.html')
        #return render(request, 'courses/detail.html', {'lessons_list': Lesson.objects.all()})


#class LessonsView(generic.ListView):
    #template_name = 'courses/detail.html'
    #context_object_name = 'lessons_list'

    #def get_queryset(self):
        #print Lessons.objects.filter(course_id=2)
        #return Lessons.objects.filter(courses_id)


#def lessons(request):
    #return render(request, 'courses/detail.html', {'lessons_list': Lesson.objects.all()})