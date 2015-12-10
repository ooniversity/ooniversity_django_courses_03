from django.shortcuts import render
from courses.models import Course


def index(request):
    return render(request, 'index.html', { 'courses': Course.objects.all()})

def contact(request):
	return render(request, 'contact.html')


class MixinTitle(object):

    def get_context_data(self, **kwargs):
        data = super(MixinTitle, self).get_context_data(**kwargs)
        data['title'] = self.title
        return data

class MixinMessage(object):

    def form_valid(self, form):
		mess = self.success_message['message'].format(form.save().__getattribute__(self.success_message['attr']))
		messages.success(self.request, mess)
		return super(MixinMessage, self).form_valid(form)