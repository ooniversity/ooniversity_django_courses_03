from django.shortcuts import render, get_object_or_404

from students.models import Student
from courses.models import Course, Lesson

def list_view(request):
    if request.GET.get('course_id'):
        students = Student.objects.filter(courses = request.GET.get('course_id'))
    else:
        students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

def detail(request,student_id):
    students = get_object_or_404(Student, pk=student_id)
    courses = Course.objects.filter(student__id= student_id)
    return render (request, 'students/detail.html', {'courses':courses,'students': students})
