# Generated by Django 4.1.3 on 2022-12-02 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_remove_student_teachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='school.teacher'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='StudentTeacher',
        ),
    ]
