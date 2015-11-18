from django.shortcuts import render

def hello(request):
	return render(request, 'index.html')

def contact(request):
	return render(request, 'contact.html')

def student(request):
	return render(request, 'student_list.html')

def best(request):
	return render(request, 'student_detail.html')
