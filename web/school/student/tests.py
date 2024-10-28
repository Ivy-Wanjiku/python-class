import datetime
from django.db import IntegrityError
from django.forms import ValidationError
from django.test import TestCase

from .forms import StudentRegistrationForm

from .models import Student

class StudentTestCase(TestCase):
    def setUp(self):
        self.student=Student(
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
  
    def test_full_name_contain_first_name(self):
        self.assertIn(self.student.first_name,self.student.full_name())
    
    def test_full_name_contain_last_name(self):
        self.assertIn(self.student.last_name,self.student.full_name())
    
    def test_invalid_email(self):
        self.student.email = "not-an-email" 
        with self.assertRaises(ValidationError):
            self.student.full_clean() 
    
    def test_get_email(self):
        self.assertEqual(self.student.get_email(), "wanjikuwanjiruivy@gmail.com")
    
class StudentFormTest(TestCase):
    def test_student_form_valid(self):
        form_data={
          "first_name":"Ivy",
            "last_name":"Wanjiku",
            "image":"",
            "email":"wanjikuwanjiruivy@gmail.com",
            "Nationality":"Kenyan",
            "date_of_birth":datetime.date(2000,9,17),
            "address":"kORONGO 616",
            "gender":"female",
            "bio":"Cliff Court is the Chief Technology Officer at GoMetro, a company focused on ",
            "cv":"Cliff Court is the Chief Technology Officer at GoMetro, a company focused on enhancing fleet management operations and transitioning to electrification for large commercial vehicles. They aim to digitize transport operations and offer a comprehensive platform that improves efficiency, reduces costs, and supports sustainable transportation solutions.If you need any further details or assistance with your cover letter or anything else, feel free to ask!"  
        }
        form=StudentRegistrationForm(data=form_data)


    def test_student_form_invalid(self):
        form_data={
            "first_name":"Ivy",
            "last_name":"Wanjiku",
            "image":"",
            # "email":"wanjikuwanjiruivy@gmail.com",

        }
        form=StudentRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("email",form.errors)
