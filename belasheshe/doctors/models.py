from django.db import models
from viewflow.fields import CompositeKey


# from healthcare.models import ResidentRoomAsgn, Doctor, Nurse, MedCond
# from .member import Member

class Doctor(models.Model):
    Doctor_ID = models.IntegerField(primary_key=True, max_length=10)
    Doctor_name=models.CharField(max_length=50)
    Address=models.TextField()
    Email=models.CharField(max_length=50)
    Qualification = models.TextField()
    Shift = models.CharField(max_length=15)
    Phone = models.CharField(max_length=15)
    Account_no = models.CharField(max_length=20)
    Salary=models.IntegerField(max_length=5)

    def __str__(self):
        return self.Doctor_name


