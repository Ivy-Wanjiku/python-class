# Generated by Django 4.2.14 on 2024-08-18 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_remove_course_teacher_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='department',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.CharField(max_length=10),
        ),
    ]