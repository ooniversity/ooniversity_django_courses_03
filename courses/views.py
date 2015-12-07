from forms import CourceModelForm
from django.shortcuts import render, redirect
from models import Course
import models


def detail(request, num):
    science = models.Course.objects.get(id=num)
    lst_of_science = models.Lesson.objects.filter(course=models.Course.objects.filter(id=num))
    return render(request, 'courses/detail.html', {'science': science, 'lst_of_science': lst_of_science})





def create(request):
    context = {}
    if request.POST: 
        form = CourceModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourceModelForm()
    context = {'form': form}
    return render(request, 'courses/add.html', context)


def edit(request, cours_id):
    context = {}
    cors = Cource.objects.get(id=cours_id)
    if request.POST:
        form = CourceModelForm(request.POST, instance=cors)
        if form.is_valid():
            form.save()
            return redirect('courses')

    else:
        form = CourceModelForm(instance=cors)
    
    context = {'form': form}
    return render(request, 'courses/edit.html', context)


def remove(request, cours_id):
    context = {}
    cors = Cource.objects.get(id=cours_id)
    form = CourceModelForm(instance=cors)
    if request.POST:
      cors.delete()
      return redirect('courses')

    context = {'form': form}
    return render(request, 'courses/remove.html', context)