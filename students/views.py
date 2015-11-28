from django.shortcuts import render
from courses.models import Course
from students.models import Student

def detail(request, course_id):
    course = Course.objects.get(id = course_id)
    students_list = Student.objects.all()
    students_list_course = []
    for person in students_list:
        if course in person.courses.all():
            students_list_course.append(person)
    return render(request, 'students/detail.html', {'course': course, 'students_list_course': students_list_course})
