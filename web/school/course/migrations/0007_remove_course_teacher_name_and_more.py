# Generated by Django 4.2.14 on 2024-08-18 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_alter_course_teacher_in_charge_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='teacher_name',
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher_in_charge',
            field=models.CharField(max_length=10),
        ),
    ]
