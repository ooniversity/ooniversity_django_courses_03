from django.shortcuts import render_to_response
from courses.models import Course
from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = 'contact.html'


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context


def page_404(request):
    response = render_to_response('404.html')
    response.status_code = 404
    return response


def page_500(request):
    response = render_to_response('500.html')
    response.status_code = 500
    return response

# def contact(request):
#     return render(request, 'contact.html')


# def student_list(request):
#    return render(request, 'student_list.html')


# def student_detail(request):
#     return render(request, 'student_detail.html')
