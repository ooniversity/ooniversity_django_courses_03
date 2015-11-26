from django.shortcuts import render
from students.models import Student
from courses.models import Course


def list_view(request):
    course_id = request.GET.get('course_id')
    # print(course_id)
    if course_id != None and course_id != '':
        # course = Course.objects.get(id=course_id)
        # student = Student.objects.all()
        list_students = []
        # for people in student:
        #     if course in people.courses.all():
        #         list_students.append(people)
        return render(request, 'students/list.html', {'list_students': list_students})
    else:
        list_students = Student.objects.all()
    return render(request, 'students/list.html', {'list_students': list_students})


def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student': student})
