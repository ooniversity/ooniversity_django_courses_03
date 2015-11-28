from django.shortcuts import render
from students.models import Student
from courses.models import Course


def list_view(request):

    get_course_id = request.GET.get('course_id', None)

    courses_list = Course.objects.all()

    if get_course_id:

        students_list = Student.objects.filter(courses = Course.objects.get(id = get_course_id))

    else:

        students_list = Student.objects.all()

    return render(request,'students/list.html', {'students_list':students_list, 'courses_list':courses_list})


def detail(request, student_id):

    student_details = Student.objects.get(id=student_id)

    return render(request,'students/detail.html', {'student_details':student_details} )