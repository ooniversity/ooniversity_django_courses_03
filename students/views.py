# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages

def list_view(request):
  course_id = request.GET.get('course_id')
  if course_id != None and course_id != '':
    course = Course.objects.get(id=course_id)
    stud = Student.objects.all()
    students = []
    for man in stud:
      if course in man.courses.all():
        students.append(man)
    return render(request, 'students/list.html', {'students':students})
  else:
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students':students})

def detail(request, student_id):
  student = Student.objects.get(id=student_id)
  return render(request, 'students/detail.html', {'student':student})

def create(request):
    form = StudentModelForm()
    if request.method == 'POST':
      form = StudentModelForm(request.POST)
      if form.is_valid():
        add_stud = form.save()
        messages.success(request, u'Student %s %s has been successfully added.' % (add_stud.name, add_stud.surname))
        return redirect('students:list_view')
    return render(request,'students/add.html',{'form':form})

def remove(request,pk):
    student = Student.objects.get(id=pk)
    message = u"%s %s" %(student.name, student.surname)
    if request.method == 'POST':
      student.delete()
      messages.success(request, u"Info on %s %s has been sucessfully deleted." % (student.name, student.surname))
      return redirect('students:list_view')
    return render(request, 'students/remove.html', {'message': message})

def edit(request,pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
      form = StudentModelForm(request.POST, instance=student)
      if form.is_valid():
        form.save()
        messages.success(request, u'Info on the student has been sucessfully changed.')
        return redirect('students:list_view')
    else:
      form = StudentModelForm(instance=student)
    return render(request,'students/edit.html',{'form':form})