# Generated by Django 3.2.6 on 2021-08-16 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='task_manager.Tag'),
        ),
    ]
