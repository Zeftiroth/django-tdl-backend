from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default='undone')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name