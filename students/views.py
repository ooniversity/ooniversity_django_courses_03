# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from courses.models import Course, Lesson
from students.models import Student
from students.forms import StudentModelForm

def list_view(request):
    try:
        qs= request.GET
        course = get_object_or_404(Course, pk=qs['course_id'])
        students = Student.objects.filter(courses__id = qs['course_id'])
        return render (request, 'students/list_view.html',{'course':course, 'students': students,})
    except:
        student_courses={}
        course = Course.objects.all()
        students = Student.objects.all()
        return render (request, 'students/list_view.html',{'course':course, 'students': students,})

def detail(request,student_id):
    student = get_object_or_404(Student, pk=student_id)
    courses = Course.objects.filter(student__id= student_id)
    return render (request, 'students/detail.html',{'courses':courses,'student': student})

def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            stud = form.save()
            mes = u'Студент %s %s успешно добавлен.' %(stud.name, stud.surname)
            messages.success(request, mes)
            return redirect("students:list_view")
    else:
        form = StudentModelForm()
    return render(request, "students/add.html", {'form':form})

def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            stud = form.save()
            mes = u'Данные изменены.'
            messages.success(request, mes)
    else:
        form = StudentModelForm(instance=student)
    return render(request, "students/edit.html", {'form':form})

def remove(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        student.delete()
        mes = u'Студент %s %s был удалён.' %(student.name, student.surname)
        messages.success(request, mes)
        return redirect("students:list_view")

    return render(request, "students/remove.html", {'name':student.name, 'surname':student.surname})
