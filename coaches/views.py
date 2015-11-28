from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def detail(request, num):
    coach = Coach.objects.get(id=num)



    return render(request,'coaches\detail.html', {'coach':coach})
