# Generated by Django 4.2.14 on 2024-08-20 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_remove_course_teacher_in_charge_course_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='name',
        ),
    ]
