# Generated by Django 4.2.14 on 2024-08-18 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_alter_teacher_options_remove_teacher_teacher_id_and_more'),
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='teacher_in_charge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher.teacher'),
        ),
    ]