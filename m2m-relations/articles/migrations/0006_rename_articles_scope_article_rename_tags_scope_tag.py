# Generated by Django 4.1.3 on 2022-12-05 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_rename_scopes_scope'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='articles',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='scope',
            old_name='tags',
            new_name='tag',
        ),
    ]
