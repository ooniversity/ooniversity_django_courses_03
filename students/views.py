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
                  
def edit(request, pk):
    form = StudentModelForm()
    student = Student.objects.get(id=pk)
    res={}   
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            messages.success(request, 'Info on the student has been successfully changed.')
            
    else:
        form = StudentModelForm(instance = student) 
    res['form'] = form
    return render(request, 'students/edit.html', res)

def remove(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (
            student.name, student.surname))
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'student': student})
        
