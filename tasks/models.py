from django.db import models
from datetime import date


class Task(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.title