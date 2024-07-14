from django.db import models

class Course(models.Model):
    title=models.CharField(max_length=20)
    course_code=models.PositiveSmallIntegerField()
    number_of_topics=models.PositiveSmallIntegerField()
    teacher_in_charge=models.CharField(max_length=10)
    duration=models.TimeField()
    student_enrolled=models.PositiveSmallIntegerField()
    department=models.TimeField()
    start_date=models.CharField(max_length=10)
    end_date=models.CharField(max_length=10)
    assessment_method=models.TextChoices=(
    "Laptop","Paper","Group Work",)
