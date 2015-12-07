from students.forms import StudentModelForm
from django.shortcuts import render, redirect
from students.models import Student
import models


def list_view(request):
    context = {}
    try:
        course_id = request.GET['course_id']
        students = models.Student.objects.filter(courses__id=course_id).order_by('id')
    except:
        students = models.Student.objects.all()
    context = {'students': students}
    return render(request, 'students/list.html', context)



def detail(request, num):
    student = models.Student.objects.get(id = num)
    #print student
    return render(request, 'students/detail.html', {'student': student})






def create(request):
    context = {}
    if request.POST: 
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    context = {'form': form}
    return render(request, 'students/add.html', context)

# EDIT !!!!
def edit(request, stdnt_id):
    context = {}
    #print stdnt_id
    stdnt = Student.objects.get(id=stdnt_id)
    if request.POST:
        #print "works befor request method!!!!!!"
        form = StudentModelForm(request.POST, instance=stdnt)
        if form.is_valid():
            form.save()
            return redirect('students:list_view')

    else:
        #  print first else branch !!!!
        form = StudentModelForm(instance=stdnt)
    
    context = {'form': form}
    return render(request, 'students/edit.html', context)


def remove(request, stdnt_id):
    context = {}
    #print stdnt_id
    #print request.method
    stdnt = Student.objects.get(id=stdnt_id)
    form = StudentModelForm(instance=stdnt)
    if request.POST:
      stdnt.delete()
      return redirect('students:list_view')

    context = {'form': form}
    return render(request, 'students/remove.html', context)