from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from courses.models import Course


def index(request):
    courses = Course.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {'courses': courses})
    return HttpResponse(template.render(context))


def contact(request):
    return render(request, 'contact.html')

class MixinTitle(object):
    def get_context_data(self, **kwargs):
        context = super(MixinTitle, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context
