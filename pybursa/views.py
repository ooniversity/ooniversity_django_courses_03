from django.shortcuts import render

def hello(request):
	return render(request, 'index.html')

def hello_python(request):
	return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')