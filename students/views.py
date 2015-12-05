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
    if request.POST:
        student_form = StudentModelForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            student_form = student_form.cleaned_data            
            my_message = "Студент {} {} успешно добавлен".format(student_form['name'], student_form['surname'])
            messages.success(request, my_message)
            return redirect ('students:list_view')
    else:
        student_form = StudentModelForm()        
    return render(request, "students/add.html", {'student_form': student_form})
