from django.shortcuts import render, redirect
from courses.models import Course
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages

def list_view(request):
    course_id = request.GET.get('course_id')
    if course_id:
        course = Course.objects.get(id = course_id)
        students_list = Student.objects.all()
        students_list_course = []
        for person in students_list:
            if course in person.courses.all():
                students_list_course.append(person)
        return render(request, 'students/list.html', {'students_list_course': students_list_course})
    else:
        students_list_course = Student.objects.all()
        return render(request, 'students/list.html', {'students_list_course': students_list_course})

def detail(request, student_id):
    student = Student.objects.get(id = student_id)
    return render(request, 'students/detail.html', {'student': student})
