from django.shortcuts import render
from students.models import Student
from django.http import HttpResponse
from django.template import RequestContext, loader
from courses.models import Course


def student_detail(request, student_id):
    student = Student.objects.get(pk = student_id)
    template = loader.get_template('students/detail.html')
    context = RequestContext(request, {
        'student': student,
    })
    return HttpResponse(template.render(context))


def list_view(request):
    try:
        course = Course.objects.get(pk = request.GET['course_id'])
        students_list = Student.objects.all().filter(courses = course)
    except KeyError:
        students_list = Student.objects.all()

    template = loader.get_template('students/list.html')
    context = RequestContext(request, {
        'students_list': students_list
    })
    return HttpResponse(template.render(context))
