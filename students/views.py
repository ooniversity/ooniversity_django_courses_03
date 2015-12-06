# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import Course
from students.models import Student
from students.forms import StudentModelForm


def list_view(request):
    try:
        st_list = Student.objects.filter(courses = int(request.GET['course_id']))
    except:
        st_list = Student.objects.all()
    return render(request, "students/list.html", {'st_list': st_list})

def detail(request, stud_id):
    student = Student.objects.get(id=stud_id)
    return render(request, "students/detail.html", {'student': student})

def create(request):
    if request.method == 'POST':
        student_form = StudentModelForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            student_form = student_form.cleaned_data            
            my_message = "Student {} {} has been successfully added.".format(student_form['name'], student_form['surname'])
            messages.success(request, my_message)
            return redirect ('students:list_view')
    else:
        student_form = StudentModelForm()        
    return render(request, "students/add.html", {'student_form': student_form})


def edit(request, stud_id):
    student = Student.objects.get(id=stud_id)
    if request.method == 'POST':
        student_form = StudentModelForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
            messages.success(request, 'Info on the student has been successfully changed.')
    else:
        student_form = StudentModelForm(instance=student)
    return render(request, "students/edit.html", {'student_form':student_form})


def remove(request, stud_id):
    student = Student.objects.get(id=stud_id)
    name = student.name
    surname = student.surname
    if request.method == 'POST':
            student.delete()
            my_message = "Info on {} {} has been sucessfully deleted.".format(name, surname)
            messages.success(request, my_message)
            return redirect ('students:list_view')
    return render(request, "students/remove.html", {'name':name, 'surname':surname})
