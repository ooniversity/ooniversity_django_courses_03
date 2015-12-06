# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from .models import Student
from students.forms import StudentModelForm
from django.contrib import messages
from django.template import RequestContext
from django.core.context_processors import csrf


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


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Student %s %s has been successfully added.' % (student.name, student.surname))
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    context = {'form': form}
    context.update(csrf(request))
    return render_to_response('students/add.html', context, context_instance=RequestContext(request))


def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Information about the student has successfully changed')
    else:
        form = StudentModelForm(instance=student)
    context = {'form': form}
    context.update(csrf(request))
    return render_to_response('students/edit.html', context, context_instance=RequestContext(request))


def remove(request, student_id):
    student = Student.objects.get(id=student_id)
    remove_message = "Warning, the student %s %s will be removed " % (student.name, student.surname)
    if request.method == 'POST':
        student.delete()
        messages.success(request,
                         "Attention, you're going to remove the student %s %s. Confirm the action " % (
                         student.name, student.surname))
        return redirect('students:list_view')
    context = {'remove_message': remove_message}
    context.update(csrf(request))
    return render_to_response('students/remove.html', context, context_instance=RequestContext(request))
