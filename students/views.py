from django.shortcuts import redirect, render
#from django.views import generic
from students.models import Student
#from courses.models import Course
from students import forms
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
# Create your views here.


class StudentDetailView(DetailView):
    model = Student
    #template_name = 'students/detail.html'


class StudentListView(ListView):
    model = Student
    paginate_by = 2
    ##queryset = Student.objects.all()
    ##template_name = 'students/list.html'
    ##context_object_name = 'student_list'

    def get_queryset(self):
        queryset = super(StudentListView, self).get_queryset()
        students_course = self.request.GET
        if 'course_id' in students_course:
            queryset = queryset.filter(courses=students_course['course_id'])
        return queryset
        #return Student.objects.all()
    #queryset = Student.objects.prefetch_related('courses')

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        student_list = Student.objects.all()
        paginator = Paginator(student_list, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            student_list = paginator.page(page)
        except PageNotAnInteger:
            student_list = paginator.page(1)
        except EmptyPage:
            student_list = paginator.page(paginator.num_pages)

        context['student_list'] = student_list
        return context


class StudentCreateView(CreateView):
    model = Student
    #template_name = 'students/add.html'
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

    def form_valid(self, form):
        student = form.cleaned_data
        messages.success(self.request, 'Student %s %s has been successfully added.' % (student['name'], student['surname']))
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    #template_name = 'students/add.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('students:edit', args=(self.object.pk,))

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

    def form_valid(self, form):
        student = self.get_object()
        messages.success(self.request, 'Info on the student %s %s has been sucessfully changed.' % (student.name, student.surname))
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

    def delete(self, request, **kwargs):
        student = self.get_object()
        message = super(StudentDeleteView, self).delete(request, **kwargs)
        messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
        return message


"""
def create(request):
    if request.method == 'POST':
        form = forms.StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Student %s %s has been successfully added.' % (student.name, student.surname))
            return redirect('students:list')
    else:
        form = forms.StudentModelForm()
    return render(request, 'students/add.html', {'form': form})
"""
"""
def edit(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Info on the student has been sucessfully changed.')
            return redirect('students:edit', pk)
    else:
        form = forms.StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})
"""
"""
def remove(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
        return redirect('students:list')
    return render(request, 'students/remove.html', {'student': student})

"""