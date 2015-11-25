from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student
from django.views.generic import ListView, DetailView

class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        r = self.request.GET
        if 'course_id' not in r:
            context['st_list'] = Student.objects.all()
        else:
            c_id = r['course_id']
            context['st_list'] = Student.objects.filter(courses__id=c_id)
        return context


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'
