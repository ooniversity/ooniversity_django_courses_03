from django.shortcuts import render
import models
from coaches.models import Coach

def detail(request, num):
    coaches = Coach.objects.all()
    return render(request, 'coaches/detail.html', {
        "coaches": coaches,
        })


