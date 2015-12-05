from django.shortcuts import render
from coaches.models import Coach

def detail(request, id):
    coach = Coach.objects.get(id=id)
    return render(request, "coaches/detail.html", {"coach": coach})
