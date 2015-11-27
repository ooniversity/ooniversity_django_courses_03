from django.shortcuts import render
from coaches.models import Coach
# from coaches.models import course


def detail(request, pk):
    coach = Coach.objects.get(id=pk)
    coach.get_full_name = coach.user.get_full_name()
    # coach.email = coach.user.email
    # coach.courses_coach = Course.objects.filter(coach=coach)
    # coach.courses_assistant = Course.objects.filter(assistant=coach)
    return render(request, 'coaches/detail.html', {'coach': coach})
