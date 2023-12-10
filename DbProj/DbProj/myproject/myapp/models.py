from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=255)
    age = models.IntegerField()
    contact_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)

class Position(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    position = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
