from django.shortcuts import render
import models


def detail(request, num):
    item = models.Course.objects.get(id=num)
    lesson = models.Lesson.objects.filter(course=models.Course.objects.filter(id=num))
    return render(request, 'courses\detail.html', {'item': item, 'lesson': lesson})


