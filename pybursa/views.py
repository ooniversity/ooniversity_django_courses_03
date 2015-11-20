from django.shortcuts import get_object_or_404, render_to_response

def index(request):
    return render_to_response('index.html')


def student_list(request):
    return render_to_response('student_list.html')


def student_detail(request):
    return render_to_response('student_detail.html')


def contact(request):
    return render_to_response('contact.html')