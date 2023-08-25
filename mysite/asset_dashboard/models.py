from datetime import datetime

from django.db import models

class Employee(models.Model):
    employeename = models.CharField(max_length=100, blank=False, null=False)
    employeeid = models.CharField(max_length=20, blank=False, null=False)
    assetid = models.CharField(max_length=50, blank=False, null=False)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Others')])
    start_date = models.DateField()
    end_date = models.DateField()
    #filename = models.FileField(upload_to='uploads/') # This will save the uploaded file to the 'uploads/' directory.

    def __str__(self):
        return str(self.employeename)