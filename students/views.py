# -*- coding: utf-8 -*-
#from django.core.context_processors import csrf
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
#from courses.models import Course, Lesson
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages
 


def list_view(request):

    args = {}

    if request.GET.get('course_id'):
        course = request.GET.get('course_id')
        st = Student.objects.filter(courses__id=course)
        args['students'] = st
    else:

        st = Student.objects.all()
        args['students'] = st

    return render(request, 'students/list.html', args)


def detail(request, stud_id):

    args = {}
    args['stud_id'] = stud_id
    st = Student.objects.get(id=stud_id)
    args['student'] = st

    return render(request, 'students/detail.html', args)

def create(request):
    args = {}
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            surname = data['surname']            
            student = form.save()
            #print form.cleaned_data
            messages.success(request, 'Student %s %s has been successfully added.' % (name, surname))
            return redirect('students:list_view')
    else:    
        form = StudentModelForm()
    #args.update(csrf(request))
        args['form'] = form
        return render(request, 'students/add.html', args)

def edit(request, stud_id):
    args = {}
    student = Student.objects.get(id=stud_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            edit_student = form.save()
            messages.success(request, 'Info on the student has been sucessfully changed.')
            return redirect('students:edit', stud_id=stud_id)     
    else:            

        form = StudentModelForm(instance=student)
        args['form'] = form
        return render(request, 'students/edit.html', args)

def remove(request, stud_id):
    args = {}
    student = Student.objects.get(id=stud_id)
    if request.method == 'POST':
        #data = form.cleaned_data
        
        name = student.name
        surname = student.surname
        student.delete()
        messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (name, surname))
        return redirect('students:list_view')
    else:
        args['student'] = student
        return render (request, 'students/remove.html', args)    