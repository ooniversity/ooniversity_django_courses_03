from forms import CourceModelForm
from models import Course
from django.shortcuts import render, redirect
import models


def detail(request, num):
    science = models.Course.objects.get(id=num)
    lst_of_science = models.Lesson.objects.filter(course=models.Course.objects.filter(id=num))
    return render(request, 'courses/detail.html', {'science': science, 'lst_of_science': lst_of_science})





def create(request):
    context = {}
    if request.POST: 
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:list_view')
    else:
        form = StudentModelForm()
    context = {'form': form}
    return render(request, 'courses/add.html', context)


def edit(request, cours_id):
    context = {}
    cors = Student.objects.get(id=cours_id)
    if request.POST:
        form = StudentModelForm(request.POST, instance=cors)
        if form.is_valid():
            form.save()
            return redirect('courses:list_view')

    else:
        form = StudentModelForm(instance=cors)
    
    context = {'form': form}
    return render(request, 'courses/edit.html', context)


def remove(request, cours_id):
    context = {}
    cors = Student.objects.get(id=cours_id)
    form = StudentModelForm(instance=cors)
    if request.POST:
      cors.delete()
      return redirect('courses:list_view')

    context = {'form': form}
    return render(request, 'courses/remove.html', context)