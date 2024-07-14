from django.db import models

class Classroom(models.Model):
    class_name=models.CharField(max_length=20)
    class_num=models.PositiveSmallIntegerField()
    teacher_in_charge=models.CharField(max_length=15)
    number_of_students=models.PositiveSmallIntegerField()
    number_of_books=models.PositiveSmallIntegerField()
    number_of_boards=models.PositiveSmallIntegerField()
    class_color=models.CharField(max_length=10)
    number_of_windows=models.PositiveSmallIntegerField()
    common_tribe = models.CharField(max_length=12)
    number_of_arts=models.PositiveSmallIntegerField()
    def __str__(self):
        return f"{self.class_name}"
