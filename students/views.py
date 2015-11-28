from django.shortcuts import render

from courses.models import Course
from students.models import Student
from django.http import HttpResponse

def detail (request, pk):
    params = {}
    params['student']=  Student.objects.get(id = pk)
    return render(request, 'students/detail.html', params)

def list_view(request):
    params = {}
    if request.GET.get('course_id'):
        params['students'] = Student.objects.filter(courses = request.GET.get('course_id'))
	params['course_id'] = request.GET.get('course_id')
    else:
        params['students'] = Student.objects.all()
    return render(request, 'students/list.html', params)
