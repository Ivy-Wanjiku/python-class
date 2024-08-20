# Generated by Django 4.2.14 on 2024-08-15 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
        ('student', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='department',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.RemoveField(
            model_name='course',
            name='student_enrolled',
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher_in_charge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='teacher.teacher'),
        ),
        migrations.AddField(
            model_name='course',
            name='student_enrolled',
            field=models.ManyToManyField(related_name='course', to='student.student'),
        ),
    ]
