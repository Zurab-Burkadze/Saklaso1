from django.db import models


class Task(models.Model):
    """
    name: String
    status: string choicefield ['draft', 'in progress', 'completed']
    description: string
    """
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    description = models.CharField(max_length=100)