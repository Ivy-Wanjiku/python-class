from django.db import models

from teacher.models import Teacher

class Course(models.Model):
    title=models.CharField(max_length=20)
    course_code=models.PositiveSmallIntegerField()
    number_of_topics=models.PositiveSmallIntegerField()
    duration=models.TimeField()
    student_enrolled=models.PositiveSmallIntegerField()
    department=models.TimeField()
    start_date=models.CharField(max_length=10)
    teachers = models.ManyToManyField(Teacher, related_name='courses', blank=True)
    end_date=models.CharField(max_length=10)
    assessment_method=models.TextChoices=(
    "Laptop","Paper","Group Work",)