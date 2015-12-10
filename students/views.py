from django.shortcuts import render, redirect
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class StudentDetailView(DetailView):
    model = Student    
    

class StudentListView(ListView):
    model = Student
    def get_queryset(self):
        if 'course_id' in self.request.GET:
            student_list = Student.objects.filter(courses=self.request.GET['course_id'])
        else:
            student_list = Student.objects.all()
        return student_list
    
class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Student %s %s has been successfully added.' % (
                form.instance.name, form.instance.surname))
        return super(StudentCreateView, self).form_valid(form)        
                
class StudentUpdateView(UpdateView):
    model = Student
    def get_success_url(self, **kwargs):
		return reverse_lazy('students:edit', args=(self.object.pk,))
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context
    def form_valid(self, form):
        
        messages.success(self.request, 'Info on the student has been successfully changed.')
        return super(StudentUpdateView, self).form_valid(form)
                  
class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context
    def delete(self, request, *args, **kwargs):
        stud = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (
                self.object.name, self.object.surname))
        return stud
        

        
