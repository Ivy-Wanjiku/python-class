from django.db import models

from course.models import Course
from student.models import Student
from teacher.models import Teacher

class Classroom(models.Model):
    students = models.ManyToManyField(Student, related_name='classrooms', blank=True)
    class_name = models.CharField(max_length=20)
    class_num = models.PositiveSmallIntegerField()
    teacher = models.ManyToManyField(Teacher)
    coursename = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher_in_charge = models.CharField(max_length=10) 
    number_of_students = models.PositiveSmallIntegerField()
    number_of_books = models.PositiveSmallIntegerField()
    number_of_boards = models.PositiveSmallIntegerField()
    class_color = models.CharField(max_length=10)
    number_of_windows = models.PositiveSmallIntegerField()
    common_tribe = models.CharField(max_length=12)
    number_of_arts = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.class_name

