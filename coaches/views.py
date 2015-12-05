from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course
from django.core.exceptions import ObjectDoesNotExist


def detail(request, detail_id):
	return render(request, 'coaches/detail.html', {'coach': Coach.objects.get(id = detail_id), 'course': Course.objects.filter(coach=detail_id), 'assist': Course.objects.filter(assistant=detail_id)})
