from datetime import datetime #Import in this order: built-ins, django, third party

from django.db import models
from django.urls import reverse


class TaskGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=True)
    taskgroup = models.ForeignKey(
        'TaskGroup', 
        on_delete=models.CASCADE, 
        related_name='tasks'
    )

    def __str__(self):
        return '{}: due on {} unit(s)'.format(self.name, self.due_date)
    
    def get_absolute_url(self):
        return reverse('tasks:task-detail', args=[self.pk])
    
    @property
    def is_due(self):
        return datetime.now() >= self.due_date
    
    class Meta:
        ordering = ['due_date'] # order by due date ascending order
        unique_together = ['name', 'due_date'] # Don't create a duplicate task
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'