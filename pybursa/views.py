from django.shortcuts import render

def index(request):
    return render(request, "{% url 'index' %}")
    
def contact(request):
    return render(request, "{% url 'contact' %}")
    
def student_list(request):
    return render(request, "{% url 'student_list' %}")
    
def student_detail(request):
    return render(request, "{% url 'student_detail' %}")

