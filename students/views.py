from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Choice, Question
from students.models import Student

def list_view(request):
    try:
        course_id = request.GET['course_id']
        course_students = Student.objects.filter(courses = course_id)
    except:
        course_students = Student.objects.all()

    return render(request, 'students/list.html', {'course_students': course_students})

def detail(request, student_id):
    student = Student.objects.get(id = student_id)
    return render(request, 'students/detail.html', {'student': student})

