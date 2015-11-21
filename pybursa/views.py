from django.shortcuts import render

def index(request):

    return render(request, 'index.html', {"foo": "bar"},
        content_type="text/html")


def contact(request):

    return render(request, 'contact.html', {"foo": "bar"},
        content_type="text/html")


def student_list(request):

    return render(request, 'student_list.html', {"foo": "bar"},
        content_type="text/html")


def student_detail(request):

    return render(request, 'student_detail.html', {"foo": "bar"},
        content_type="text/html")
