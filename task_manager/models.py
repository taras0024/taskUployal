from datetime import datetime

from django.db import models

PRIORITY = [
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
]

STATUS = [
    ('BG', 'Backlog'),
    ('IP', 'In Progress'),
    ('DN', 'Done'),
]


class Tag(models.Model):
    """Tag model"""

    name = models.CharField('Tag', max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Task(models.Model):
    """Task model"""

    title = models.CharField('Title', max_length=256)
    description = models.CharField('Description', max_length=512, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=1, choices=PRIORITY, default='M')
    status = models.CharField(max_length=2, choices=STATUS, default='BG')
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='task')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
