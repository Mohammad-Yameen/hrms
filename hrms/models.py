from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    joining_date = models.DateTimeField()