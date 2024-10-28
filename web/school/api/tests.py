import datetime
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from student.models import Student
from .serializers import StudentSerializer


class StudentListAPIViewTest(APITestCase):
    def setUp(self):
        self.student=Student.objects.create(
          first_name="Ivy",
            last_name="Wanjiku",
            image="",
            email="wanjikuwanjiruivy@gmail.com",
            Nationality="Kenyan",
            date_of_birth=datetime.date(2000,9,17),
            address="kORONGO 616",
            gender="female",
            bio="Cliff Court is the Chief Technology Officer at GoMetro, a company focused on ",
            cv="Cliff Court is the Chief Technology Officer at GoMetro, a company focused on enhancing fleet management operations and transitioning to electrification for large commercial vehicles. They aim to digitize transport operations and offer a comprehensive platform that improves efficiency, reduces costs, and supports sustainable transportation solutions.If you need any further details or assistance with your cover letter or anything else, feel free to ask!"

            )
    def test_get_student_list(self):
        url=reverse("student_list_view")
        response=self.client.get(url)
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        # self.assertEqual(response.data,serializer.data)

