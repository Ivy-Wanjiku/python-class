# Generated by Django 4.2.14 on 2024-10-21 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_remove_student_student_id_student_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='coursename',
        ),
    ]
