# Generated by Django 4.2.14 on 2024-08-18 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]