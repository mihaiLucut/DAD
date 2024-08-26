# models.py
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255)
    time_estimate = models.IntegerField(
        choices=[(5, '5 min'), (10, '10 min'), (15, '15 min'), (20, '20 min'), (25, '25 min')])
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
