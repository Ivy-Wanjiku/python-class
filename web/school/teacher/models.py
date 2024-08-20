from django.db import models

class Teacher(models.Model):
    name=models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True) 
    picture = models.ImageField(upload_to='teachers/')  
    cv = models.TextField()
    payment_methods = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    total_amount_paid = models.PositiveSmallIntegerField()
    experience = models.PositiveSmallIntegerField()
    age = models.PositiveSmallIntegerField()
    level_of_education = models.CharField(max_length=15)
    unit_taught = models.CharField(max_length=10)
    payment_accounts = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


