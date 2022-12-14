# Generated by Django 4.1.3 on 2022-12-02 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_remove_student_teacher_student_teachers'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='school.student')),
                ('teachers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='school.teacher')),
            ],
        ),
    ]
