from django.db import models

from course.models import Course
from teacher.models import Teacher

class ClassPeriod(models.Model):
    classteacher=models.ManyToManyField(Teacher)
    classcourse=models.ManyToManyField(Course)
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.CharField(max_length=20)
    classroom = models.CharField(max_length=20)
    day_of_the_week = models.CharField(max_length=20)
    def __str__(self):
        return self.classroom
