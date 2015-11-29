from django.shortcuts import render
import models


def detail(request, num):
    science = models.Course.objects.get(id=num)
    lst_of_science = models.Lesson.objects.filter(course=models.Course.objects.filter(id=num))
    return render(request, 'courses/detail.html', {'science': science, 'lst_of_science': lst_of_science})


