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
    return render(request, 'students/list.html', {'students': students})


def detail(request, pk):
    return render(request, 'students/detail.html', { 'student' : Student.objects.get(id=pk)})


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            mess = "Student {} {} has been successfully added.".format(application.name, application.surname)
            messages.success(request, mess)
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})


def edit(request, pk):
    application = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=application)
        if form.is_valid():
            application = form.save()
            messages.success(request, 'Info on the student has been sucessfully changed.')
    else:
        form = StudentModelForm(instance=application)
    return render(request, 'students/edit.html', {'form': form})


def remove(request, pk):
    student = Student.objects.get(id=pk)
    fname = '{} {}'.format(student.name, student.surname)
    if request.method == 'POST':
        student.delete()
        mess = 'Info on {} has been sucessfully deleted.'.format(fname)
        messages.success(request, mess)
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'full_name': fname}) 


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