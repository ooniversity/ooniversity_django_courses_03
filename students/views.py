from django.shortcuts import render, get_object_or_404
from courses.models import Course, Lesson
from students.models import Student

def list_view(request):
    try:
        qs= request.GET
        course = get_object_or_404(Course, pk=qs['course_id'])
        students = Student.objects.filter(courses__id = qs['course_id'])
        return render (request, 'students/list_view.html',{'course':course, 'students': students,})
    except:
        student_courses={}
        course = Course.objects.all()
        students = Student.objects.all()
        return render (request, 'students/list_view.html',{'course':course, 'students': students,})

def detail(request,student_id):
    student = get_object_or_404(Student, pk=student_id)
    courses = Course.objects.filter(student__id= student_id)
    return render (request, 'students/detail.html',{'courses':courses,'student': student})

