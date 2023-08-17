# Generated by Django 4.2.4 on 2023-08-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_todo_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(blank=True, choices=[('High Priority', 'High Priority'), ('Mid Priority', 'Mid Priority'), ('Low Priority', 'Low Priority')], max_length=30),
        ),
    ]
