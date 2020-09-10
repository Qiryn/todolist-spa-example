from django.db import models


# Create your models here.

class TodoItem(models.Model):
    name = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
