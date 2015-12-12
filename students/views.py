from django.contrib import messages
from django.shortcuts import render, redirect
from students.models import Student
from django.http import HttpResponse
from django.template import RequestContext, loader
from courses.models import Course
from students.forms import StudentModelForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


class StudentListView(ListView):
    model = Student
    template_name = "students/list.html"
    context_object_name = 'students_list'

    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        try:
            course = Course.objects.get(pk = self.request.GET['course_id'])
            students_list = qs.filter(courses = course)
        except (KeyError, Course.DoesNotExist) as e:
            students_list = Student.objects.all()
        return students_list


class StudentDetailView(DetailView):
    model = Student
    template_name = "students/detail.html"
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['student'] = context['object']
        return context


class StudentCreateView(CreateView):
    form_class = StudentModelForm
    template_name = "students/add.html"
    success_url = "students:list_view"

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Student successfully added.')
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    form_class = StudentModelForm
    template_name = "students/edit.html"
    success_url = "students:list_view"

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Student successfully edited.')
        return super(StudentCreateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
    form_class = StudentModelForm
    template_name = "students/remove.html"
    success_url = "students:list_view"

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Student successfully removed.')
        return super(StudentCreateView, self).form_valid(form)



# Students list
# def list_view(request):
#     try:
#         course = Course.objects.get(pk = request.GET['course_id'])
#         students_list = Student.objects.all().filter(courses = course)
#     except KeyError:
#         students_list = Student.objects.all()
#
#     template = loader.get_template('students/list.html')
#     context = RequestContext(request, {
#         'students_list': students_list
#     })
#     return HttpResponse(template.render(context))


# Create
# def create(request):
#     form = StudentModelForm()
#     if request.method == 'POST':
#         form = StudentModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Student successfully added.')
#             return redirect('students:list_view')
#
#     template = loader.get_template('students/add.html')
#     context = RequestContext(request, {
#         'form': form
#     })
#     return HttpResponse(template.render(context))


# Delete
# def remove(request, pk):
#     student = Student.objects.get(id=pk)
#
#     if request.method == 'POST':
#         student.delete()
#         messages.success(request, 'Student successfully removed.')
#         return redirect('students:list_view')
#
#     template = loader.get_template('students/remove.html')
#     context = RequestContext(request, {
#         'student': student
#     })
#     return HttpResponse(template.render(context))


# Edit
# def edit(request, pk):
#     student = Student.objects.get(id=pk)
#     if request.method == 'POST':
#         form = StudentModelForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Student successfully edited.')
#             return redirect('students:list_view')
#     else:
#         form = StudentModelForm(instance=student)
#
#     template = loader.get_template('students/edit.html')
#     context = RequestContext(request, {
#         'form': form
#     })
#     return HttpResponse(template.render(context))


