# Generated by Django 3.2.6 on 2021-08-16 10:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_created=True)),
                ('name', models.CharField(max_length=128, verbose_name='Tag')),
                ('created', models.DateField(default=datetime.datetime.now, verbose_name='Created')),
                ('updated', models.DateField(default=datetime.datetime.now, verbose_name='Updated')),
                ('last_modified', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_created=True)),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=512, null=True, verbose_name='Description')),
                ('created', models.DateField(default=datetime.datetime.now, verbose_name='Created')),
                ('priority', models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], default='M', max_length=1)),
                ('status', models.CharField(choices=[('BG', 'Backlog'), ('IP', 'In Progress'), ('DN', 'Done')], default='BG', max_length=2)),
                ('updated', models.DateField(default=datetime.datetime.now, verbose_name='Updated')),
                ('last_modified', models.DateField(auto_now=True)),
                ('tags', models.ManyToManyField(blank=True, related_name='tags', to='task_manager.Tag')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]
