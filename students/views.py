from django.shortcuts import render,  get_object_or_404
from django.db import models
import models
from courses.models import Course

def list_view(request):
    try:
        course_id = request.GET['course_id']
        students = models.Student.objects.filter(courses__id=course_id).order_by('id')
        selection = True
    except:
        students = models.Student.objects.all()
        selection = False

    return render(request, 'students/list.html', {'students': students,
        'selection': selection})


def detail(request, student_id):
    student = models.Student.objects.get(id = student_id)
    return render(request, 'students/detail.html', {'student': student})
