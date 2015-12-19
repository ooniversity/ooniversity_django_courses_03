from django.test import TestCase
from students.models import Student
from courses.models import Course, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User
from django.test import Client

def load_test_data():
    new_user_1 = User.objects.create(
                            username='user_1')

    new_user_2 = User.objects.create(
                            username='user_2')



    coach_A = Coach.objects.create(
                            user=new_user_1,
	                        date_of_birth='1999-01-01',
	                        gender='M',
	                        phone='1234',
	                        address='addr1',
	                        skype='user_1',
	                        description='coach')

    assistant_A = Coach.objects.create(
                            user=new_user_2,
	                        date_of_birth='1999-01-01',
	                        gender='M',
	                        phone='1235',
	                        address='addr2',
	                        skype='user_1',
	                        description='assistant')

    course_A = Course.objects.create(
                            name='A',
                            short_description='short_d_a',
                            description='description_A',
                            coach=coach_A,
                            assistant=assistant_A)
    course_B = Course.objects.create(
                            name='B',
                            short_description='short_d_B',
                            description='description_B',
                            coach=coach_A,
                            assistant=assistant_A)



class CoursesListTest(TestCase):
    def setUp(self):
        self.client = Client()
        load_test_data()

    def test_courses_count(self):
        self.assertEqual(Course.objects.all().count(), 2)

    def test_courses_no_crash(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_courses_is_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_courses_links_exists(self):
        response = self.client.get('/')
        self.assertContains(response, '/courses/add/')
        for i in [1, 2]:
            self.assertContains(response, '/courses/edit/{}/'.format(i))
            self.assertContains(response, '/courses/remove/{}/'.format(i))

    def test_couses_title(self):
        response = self.client.get('/')
        self.assertContains(response, '<title>ItBursa main</title>' )

class CoursesDetailTest(TestCase):

    def test_courses_no_crash(self):
        for i in [1, 2]:
            response = self.client.get('/courses/{}/'.format(i))
        self.assertEqual(response.status_code, 200)

    def test_courses_not_found(self):
        response = self.client.get('/courses/999/')
        self.assertEqual(response.status_code, 404)

    def test_courses_is_correct_template(self):
        response = self.client.get('/courses/1/')
        self.assertTemplateUsed(response, 'courses/detail.html')

    def test_courses_description(self):
        response = self.client.get('/courses/1/')
        self.assertContains(response, 'description_A')

    def test_courses_sh_descr(self):
        response = self.client.get('/courses/1/')
        self.assertContains(response, 'short_d_a')
