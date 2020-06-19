from django.db import models
from datetime import datetime


class task(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    date = models.DateField(datetime.today)