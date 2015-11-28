from django.shortcuts import render
from django.views import generic

from students.models import Student


class DetailView(generic.DetailView):
    model = Student
    template_name = 'students/detail.html'

class ListView(generic.ListView):
    template_name = 'students/list.html'
    context_object_name = 'students_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Student.objects.all()
