from django.shortcuts import render
from coaches.models import Coach
# from coaches.models import course


def detail(request, pk):
    coach = Coach.objects.get(id=pk)
    return render(request, 'coaches/detail.html', {'coach': coach})
