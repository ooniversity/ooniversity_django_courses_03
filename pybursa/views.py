from django.shortcuts import render


# Create your views here.
def main_page(request):
    # return HttpResponse('Hello, world!')
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def student_list(request):
    return render(request, 'student_list.html')


def student_detail(request):
    return render(request, 'student_detail.html')
