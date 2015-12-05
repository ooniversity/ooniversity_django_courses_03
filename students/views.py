from django.shortcuts import render, get_object_or_404
from students.models import Student
from courses.models import  Course, Lesson
from django.core.urlresolvers import reverse


def list_view(request):
    try:
        course_id = request.GET['course.id']
    except:
        course_id = None
    context ={}
    print "ID=",course_id
    if course_id == None:
        context['students'] = Student.objects.all()
    else:
        p = get_object_or_404(Course, pk = course_id)
        context['students'] = Student.objects.filter(courses = course_id)
    return render(request, 'students/list.html', context)
# Create your views here.

def detail(request, student_id):
    p = get_object_or_404(Student, pk = student_id)
    context = {}
    context['student'] = Student.objects.get(id = student_id)
    context['course'] = Student.objects.get(id = student_id)
    return render(request, 'students/detail.html', context)