from django.db import models
    
    
class Attendance(models.Model):
    status = models.CharField(max_length=30)
    date = models.DateTimeField()

class Employee(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    joining_date = models.DateTimeField()
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    