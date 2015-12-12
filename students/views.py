from django.contrib import messages
from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView



def students_list(request):
    course_id = request.GET.get('course_id', None)
    if course_id:
        students = Student.objects.filter(course=course_id)
        courses_list = 'NO'

    else:
        courses_list = 'NO'
        students = Student.objects.all()
        test = Student.objects.filter(name='Ivan')
        print test

    return render(request, 'students/student_list.html', {'students': students, 'student_courses': Course.objects.all(),
                                                 'courses_list': courses_list})

class StudentListlView(ListView):
    model = Student
    context_object_name = 'students'

    def get_queryset(self):
        qs = super(StudentListlView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(course=course_id)
        return qs

def add_student(request):


    if request.method == 'POST':
        form = StudentModelForm(request.POST)


        new_student = form.save()
        messages.success(request, 'Form saved')
        return redirect ('/student_list/add/')
    else:
        form = StudentModelForm()

    return render(request, 'add.html', {'model_form': form})

class StudentDetailView(DetailView):

    model = Student
    context_object_name = "student_details"


