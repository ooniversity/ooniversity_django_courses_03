from django.shortcuts import render
from django.shortcuts import get_object_or_404
from courses.models import Coach

def detail(request, pk):
	coach_object =  get_object_or_404(Coach, pk=pk) 
	return render(request, 'coaches/detail.html', {'coach_object': coach_object})
