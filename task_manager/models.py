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
    created = models.DateField('Created', default=datetime.now)
    updated = models.DateField('Updated', default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Task(models.Model):
    """Task model"""

    title = models.CharField('Title', max_length=256)
    description = models.CharField('Description', max_length=512, blank=True, null=True)
    created = models.DateField('Created', default=datetime.now)
    priority = models.CharField(max_length=1, choices=PRIORITY, default='M')
    status = models.CharField(max_length=2, choices=STATUS, default='BG')
    updated = models.DateField('Updated', default=datetime.now)
    tags = models.ManyToManyField(Tag, related_name='task')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
