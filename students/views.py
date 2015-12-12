# -*- coding:UTF-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from students.models import Student
from courses.models import Course
import students.forms
from django.contrib import messages
from django.views.generic.detail import DetailView


class StudentDetailView(DetailView):
    model = Student
    # template_name = ""
    context_object_name = "student_details"


# ------ old ----

def list_view(request):
    get_course_id = request.GET.get('course_id', None)
    courses_list = Course.objects.all()
    if get_course_id:
        students_list = Student.objects.filter(courses=Course.objects.get(id=get_course_id))
    else:
        students_list = Student.objects.all()

    return render(request, 'students/list.html', {'students_list': students_list, 'courses_list': courses_list})

# replaced with class
# def detail(request, pk):
#    student_details = Student.objects.get(id=pk)

    return render(request, 'students/detail.html', {'student_details': student_details})


def create(request):
    if request.method == 'POST':
        form = students.forms.StudentModelForm(request.POST)
        if form.is_valid():
            form_content = form.cleaned_data
            form.save()
            notification = "Student %s %s has been successfully added." % (form_content['name'], form_content['surname'])
            messages.success(request, notification)
        return redirect('students:list_view')
    else:
        form = students.forms.StudentModelForm()

    return render(request, 'students/add.html', {'form': form})


def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = students.forms.StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Info on the student has been successfully changed.")
            return render(request, 'students/edit.html', {'form': form})

    form = students.forms.StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})


def remove(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        student.delete()
        messages.success(request, u"Info on %s %s has been successfully deleted." % (student.name, student.surname))
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'student': student})
