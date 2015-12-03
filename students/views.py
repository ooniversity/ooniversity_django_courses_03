from django.shortcuts import render, redirect
from students.models import Student
from django.contrib import messages
from students.forms import *

def list_view(request):
    r = request.GET
    if 'course_id' in r:
        students=Student.objects.filter(courses=r['course_id'])
    else:
        students=Student.objects.all()
    return render(request, 'students/list_view.html', {'students': students})


def create(request):
    print request.POST
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            mess = "Student {} {} has been successfully added.".format(request.POST['name'], request.POST['surname'])
            messages.success(request, mess)
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})


def detail(request, pk):
    return render(request, 'students/detail.html', { 'student' : Student.objects.get(id=pk)})

"""
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
"""