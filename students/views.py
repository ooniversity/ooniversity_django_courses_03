from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages

from students.models import Student, CourseApplication
from courses.models import Course


# class StudentApplyForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField(label='Mail', help_text='personal email')
#     package = forms.ChoiceField(choices=(
#         ('standart', 'standart'),
#         ('gold', 'Gold'),
#         ('vip', 'VIP')),
#         widget=forms.RadioSelect, initial='standart')
#     news_subscribe = forms.BooleanField(required=False)


# class CourseApplicationForm(forms.ModelForm):

#     class Meta:
#         model = CourseApplication
#         exclude = ['comment', 'is_active']
#         widgets = {'package': forms.RadioSelect}
#         labels = {'email': 'Mail'}
#         help_texts = {'email': 'personal email'}


def list_view(request):
    reguest_course = request.GET
    if 'course_id' in reguest_course:
        list_students = Student.objects.filter(
            courses=reguest_course['course_id'])
    else:
        list_students = Student.objects.all()
    return render(request, 'students/list.html', {'list_students': list_students})


def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student': student})


# def apply_to_course(request):
#     if request.method == 'POST':
#         form = CourseApplicationForm(request.POST)
#         if form.is_valid():
#             application = form.save()
#             messages.success(request, 'Form saved!')
#             return redirect('students:course-application')
#     else:
#         form = CourseApplicationForm(
#             initial={'news_subscribe': True})

#     return render(request, 'students/apply.html',
#                   {'form': form})


# def edit_application(request, pk):
#     application = CourseApplication.objects.get(id=pk)
#     if request.method == 'POST':
#         form = CourseApplicationForm(request.POST, instance=application)
#         if form.is_valid():
#             application = form.save()
#             messages.success(request, 'Form saved!')
#             return redirect('students:course-application')
#     else:
#         form = CourseApplicationForm(instance=application)
#     return render(request, 'students/edit_application.html',
#                   {'form': form})


# def delete_application(request, pk):
#     application = CourseApplication.objects.get(id=pk)
#     if request.method == 'POST':
#         application.delete()
#         messages.success(request, 'Object delete saved!')
#         return redirect('students:course-application')
#     return render(request, 'students/delete_application.html',
#         {'application':application})
