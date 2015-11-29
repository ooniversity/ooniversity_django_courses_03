from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from coaches.models import Coach

def detail(request, coach_id):
    coach = get_object_or_404(Coach, pk=coach_id)
    template = loader.get_template('coaches/detail.html')
    context = RequestContext(request, {
        'coach': coach,
    })
    return HttpResponse(template.render(context))
