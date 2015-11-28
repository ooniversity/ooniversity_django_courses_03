from django.shortcuts import render
from students.models import Student
import os


# Create your views here.
def list_view(request):
    replay = request.GET
    if 'course_id' in replay:
        result = Student.objects.filter(courses=replay['course_id'])
    else:
        result = Student.objects.all()
    return render(
        request,
        os.path.join('students', 'list.html'),
        {'students': result}
    )


def detail(request, student_id):
    result = {'student': Student.objects.get(id=student_id)}
    return render(
        request,
        os.path.join('students', 'detail.html'),
        result
    )
