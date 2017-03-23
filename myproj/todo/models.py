from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    priority = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=200)
