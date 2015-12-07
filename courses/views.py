from forms import CourceModelForm
from django.shortcuts import render, redirect
from models import Course
import models


def detail(request, cours_id):
    science = models.Course.objects.get(id=cours_id)
    lst_of_science = models.Lesson.objects.filter(course=models.Course.objects.filter(id=cours_id))
    return render(request, 'courses/detail.html', {'science': science, 'lst_of_science': lst_of_science})





def add(request):
    context = {}
    if request.POST: 
        form = CourceModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CourceModelForm()
    context = {'form': form}
    return render(request, 'courses/add.html', context)


def edit(request, cours_id):
    context = {}
    return render(request, 'courses/edit.html', context)


def remove(request, cours_id):
    context = {}
    return render(request, 'courses/remove.html', context)