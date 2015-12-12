from django.shortcuts import redirect, render
from django.views import generic
from students.models import Student
#from courses.models import Course
from students import forms
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
# Create your views here.


class StudentDetailView(generic.DetailView):
    model = Student
    #template_name = 'students/detail.html'


class StudentListView(generic.ListView):
    #model = Student
    queryset = Student.objects.all()
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


class StudentCreateView(generic.CreateView):
    model = Student
    #template_name = 'students/add.html'
    success_url = reverse_lazy('students:list')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context


class StudentUpdateView(generic.UpdateView):
    model = Student
    #template_name = 'students/add.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('students:edit', args=(self.object.pk,))

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

    #def form_valid(self, form):


class StudentDeleteView(generic.DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

def create(request):
    #print request.POST
    #form = StudentModelForm()
    if request.method == 'POST':
        form = forms.StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            #data = form.cleaned_data
            #student = Student()
            #student.name = data['name']
            #student.surname = data['surname']
            #student.date_of_birth = data['date_of_birth']
            #student.email = data['email']
            #student.phone = data['phone']
            #student.address = data['address']
            #student.skype = data['skype']
            #student.courses = data['courses']
            #student.save()
            messages.success(request, 'Student %s %s has been successfully added.' % (student.name, student.surname))
            return redirect('students:list')
    else:
        form = forms.StudentModelForm()
    return render(request, 'students/add.html', {'form': form})


def edit(request, pk):
    student = Student.objects.get(id=pk)
    #form = forms.StudentModelForm(instance=student)
    if request.method == 'POST':
        form = forms.StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Info on the student has been sucessfully changed.')
            return redirect('students:edit', pk)
    else:
        form = forms.StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})


def remove(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
        return redirect('students:list')
    return render(request, 'students/remove.html', {'student': student})