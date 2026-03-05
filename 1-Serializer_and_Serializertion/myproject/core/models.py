from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField()
    roll = models.IntegerField()
    city = models.CharField()

