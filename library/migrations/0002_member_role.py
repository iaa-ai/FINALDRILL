# Generated by Django 5.0 on 2023-12-27 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='role',
            field=models.CharField(blank=True, choices=[('Student', 'Student'), ('Teacher', 'Teacher'), ('Staff', 'Staff'), ('Other', 'Other')], max_length=10, null=True),
        ),
    ]
