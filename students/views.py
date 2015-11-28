# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404

from .models import Student


def list_view(request):
    try:
        course_id = request.GET['course_id']
        all_students = Student.objects.filter(courses__exact=course_id)
    except:
        all_students = Student.objects.all().order_by('id')

    context = {
        'all_students': all_students
    }
    return render_to_response('students/list.html', context)


def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {
        'student': student,
    }
    return render_to_response('students/detail.html', context)
