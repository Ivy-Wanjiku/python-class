from django.db import models
from course.models import Course

class Student(models.Model):
    coursename=models.ManyToManyField(Course)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    image=models.ImageField()
    email=models.EmailField()
    Nationality=models.CharField(max_length=20)
    date_of_birth=models.DateField()
    address=models.CharField(max_length=16)
    gender=models.CharField(max_length=10)
    bio=models.TextField()
    cv=models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
