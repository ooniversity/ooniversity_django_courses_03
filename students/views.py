# -*- coding:UTF-8 -*-

from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages


def list_view(request):
    get_course_id = request.GET.get('course_id', None)
    courses_list = Course.objects.all()
    if get_course_id:
        students_list = Student.objects.filter(courses=Course.objects.get(id=get_course_id))
    else:
        students_list = Student.objects.all()

    return render(request, 'students/list.html', {'students_list': students_list, 'courses_list': courses_list})


def detail(request, student_id):
    student_details = Student.objects.get(id=student_id)

    return render(request, 'students/detail.html', {'student_details': student_details})


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form_content = form.cleaned_data
            form.save()
            notification = "Student %s %s has been successfully added." % (form_content['name'].encode('utf-8'), form_content['surname'].encode('utf-8'))
            messages.success(request, notification)
            return redirect('students:list_view')
    else:
        form = StudentModelForm()

    return render(request, 'students/add.html', {'form': form})


def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Info on the student has been sucessfully changed.")
            return render(request, 'students/edit.html', {'form': form})
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})


def remove(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        student.delete()
        messages.success(request, u"Info on %s %s has been sucessfully deleted." % (student.name, student.surname))
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'student': student})
