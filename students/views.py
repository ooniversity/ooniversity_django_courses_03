# -*- coding: utf-8 -*
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from students.models import Student


class StudentDetailView(DetailView):
    model = Student


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        student = form.save()
        messages.success(self.request, 'Student %s %s has been successfully added.' % (
            student.name, student.surname))
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    # template_name = 'students/add.html'

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        messages.success(
            self.request, 'Info on the student has been sucessfully changed.')
        return super(StudentUpdateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('students:edit', args=(self.object.pk,))


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        data = super(StudentDeleteView, self).get_context_data(**kwargs)
        data['title'] = 'Student info suppression'
        return data

    def delete(self, request, *args, **kwargs):
        message = super(StudentDeleteView, self).delete(
            request, *args, **kwargs)
        messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (
            self.object.name, self.object.surname))
        return message


# def list_view(request):
#     reguest_course = request.GET
#     if 'course_id' in reguest_course:
#         list_students = Student.objects.filter(
#             courses=reguest_course['course_id'])
#     else:
#         list_students = Student.objects.all()
# return render(request, 'students/list.html', {'list_students':
# list_students})

#
# def detail(request, pk):
#     student = Student.objects.get(id=pk)
#     return render(request, 'students/detail.html', {'student': student})


# def create(request):
#     context = {}
#     if request.method == "POST":
#         context['form'] = form = StudentModelForm(request.POST)
#         if form.is_valid():
#             student = form.save()
#             data = form.cleaned_data
#             messages.success(request, 'Student %s %s has been successfully added.' % (
#                 student.name, student.surname))
#             return redirect('students:list_view')

#     else:
#         context['form'] = StudentModelForm()
#     return render(request, 'students/add.html', context)


# def edit(request, pk):
#     student = Student.objects.get(id=pk)
#     if request.method == "POST":
#         form = StudentModelForm(request.POST, instance=student)
#         if form.is_valid():
#             student = form.save()
#             messages.success(
#                 request, 'Info on the student has been sucessfully changed.')
#             # return redirect('students:list_view')
#     else:
#         form = StudentModelForm(instance=student)
#     return render(request, 'students/edit.html', {'form': form})


# def remove(request, pk):
#     student = Student.objects.get(id=pk)
#     if request.method == "POST":
#         student.delete()
#         messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (
#             student.name, student.surname))
#         return redirect('students:list_view')
#     return render(request, 'students/remove.html', {'student': student})
