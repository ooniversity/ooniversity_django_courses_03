from django import forms
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from courses.models import Course, Lesson
from students.forms import StudentModelForm
from students.models import Student
class StudentListView(ListView):
    model = Student
    paginate_by = 2
    def get_queryset(self):
        queryset = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            queryset = queryset.filter(courses__id = course_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        context['c_id'] = self.request.GET.get('course_id', None)
        return context

'''
def list_view(request):
    params = {}
    if request.GET.get('course_id'):
        params['students'] = Student.objects.filter(courses = request.GET.get('course_id'))
	params['course_id'] = request.GET.get('course_id')
    else:
        params['students'] = Student.objects.all()
    return render(request, 'students/list.html', params)
'''
class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Student registration"
        return context

    def form_valid(self, form):
        message = super(StudentCreateView, self).form_valid(form)
        text = u'Student {0} {1} has been successfully added.' .format(self.object.name, self.object.surname)
        messages.success(self.request, text)
        return message

'''
def create(request):
    params = {}
    if request.POST:
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            cleaned = form.cleaned_data
            messages.success(request, 'Student {0} {1} has been successfully added.'.format(cleaned['name'], cleaned['surname']))
        return redirect('students:list_view')
    else:
        form = StudentModelForm()
    params['form'] = form
    return render(request, 'students/add.html', params)
'''
class StudentUpdateView(UpdateView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = u"Student info update"
        return context

    def get_success_url(self):
        return reverse_lazy('students:edit', kwargs={'pk': self.object.pk})
    def form_valid(self, form):
        message = super(StudentUpdateView, self).form_valid(form)
        messages.success(self.request, u'Info on the student has been sucessfully changed.')
        return message
'''
def edit(request, s_id):
    student = Student.objects.get(id = s_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance = student)
        if form.is_valid():
            student = form.save()
            messages.success(request, u'Info on the student has been sucessfully changed.')
    else:
        form = StudentModelForm(instance = student)
    return render(request, 'students/edit.html', {'form': form})
'''
class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = u"Student info suppression"
        return context

    def delete(self, request, *args, **kwargs):
        message = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        text = u'Info on {0} {1} has been sucessfully deleted.' .format(self.object.name, self.object.surname)
        messages.success(self.request, text)
        return message
'''
def remove(request, s_id):
    params = {}
    student = Student.objects.get(id = s_id)
    if request.method == "POST":
        student.delete()
        messages.success(request, u"Info on {0} {1} has been sucessfully deleted.".format(student.name, student.surname))
        return redirect('students:list_view')
    params['student'] = student
    return render(request, 'students/remove.html', params)
'''

class StudentDetailView(DetailView):
	model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        logger.debug('Students detail view has been debugged')
        logger.info('Logger of students detail view informs you!')
        logger.warning('Logger of students detail view warns you!')
        logger.error('Students detail view went wrong!')
        return context
'''
def detail (request, pk):
    params = {}
    params['student']=  Student.objects.get(id = pk)
    return render(request, 'students/detail.html', params)
'''
