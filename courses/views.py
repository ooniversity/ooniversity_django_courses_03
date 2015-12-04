from django.shortcuts import render
from courses.models import Course, Lesson
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm

# Create your views here.
def detail(request, course_id):
	course = Course.objects.get(id = course_id)
	lessons = Lesson.objects.filter(course = course_id)
	coach = course.coach.full_name()
	coach_descr = course.coach.description
	c = course.coach.id
	assistant = course.assistant.full_name()
	as_descr = course.assistant.description
	a = course.assistant.id
	return render(request, 'courses/detail.html', 
		{'course':course, 'lessons':lessons, 'coach':coach, 'assistant':assistant, 'c':c, 'coach_descr':coach_descr, 'as_descr':as_descr, 'a':a})

def create(request):
	if request.POST:
		form = CourseModelForm(request.POST)
		if form.is_valid():
			student = form.save()
			messages.success(request, 'Student has been successfully added.')
			return redirect('students:list_view')
	else:
		form = CourseModelForm()
	return render(request, 'students/add.html', {'form':form})


def edit(request, student_id):
	student = Course.objects.get(id = student_id)
	if request.POST:
		form = CourseModelForm(request.POST, instance = student)
		if form.is_valid():
			student = form.save()
			messages.success(request, 'Info on the student has been sucessfully changed.')
			return redirect('students:edit', student.id)
	else:
		form = CourseModelForm(instance = student)
	return render(request, 'students/edit.html', {'form':form})


def remove(request, student_id):
	student = Course.objects.get(id = student_id)
	if request.method == 'POST':
		messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
		student.delete()
		return redirect('students:list_view')
	return render(request, 'students/remove.html', {'student':student})
