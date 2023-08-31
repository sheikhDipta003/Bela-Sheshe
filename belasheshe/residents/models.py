from django.db import models
from viewflow.fields import CompositeKey
from nurse.models import Nurse
#from doctors.models import Doctor
# from healthcare.models import ResidentRoomAsgn, Doctor, Nurse, MedCond
# from .member import Member
#from residents.models import CheckupItem
class Member(models.Model):
    Member_ID = models.IntegerField(primary_key=True, max_length=10)
    # Room_no = models.ForeignKey(ResidentRoomAsgn, on_delete=models.CASCADE)
    Room_no = models.IntegerField()
    Name = models.CharField(max_length=100)
    Address = models.TextField()
    Email = models.EmailField()
    Phone = models.CharField(max_length=15)
    DOB = models.DateField()
    Religion = models.CharField(max_length=50)
    Account_no = models.CharField(max_length=20)

    def __str__(self):
        return self.Name


# Create a model named ResidentMedCond
class ResidentMedCond(models.Model):
    id = CompositeKey(columns=['Member_ID', 'Cond_ID'])
    Member_ID = models.ForeignKey(Member, on_delete=models.CASCADE)
    # Cond_ID = models.ForeignKey(MedCond, on_delete=models.CASCADE)
    Cond_ID = models.IntegerField()

    def __str__(self):
        return f"Medical Condition for {self.Member_ID}"
    
# Create a model named MemberAppoint
class MemberAppoint(models.Model):
    App_ID = models.AutoField(primary_key=True)
    Member_ID = models.ForeignKey(Member, on_delete=models.CASCADE)
    # Doctor_ID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # Nurse_ID = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    Doctor_ID = models.IntegerField()
    Nurse_ID = models.IntegerField()
    Date = models.DateField()
    Time = models.TimeField()

    def __str__(self):
        return f"Appointment {self.App_ID} for {self.Member_ID}"

class CheckupItem(models.Model):
    Checkup_Id = models.AutoField(primary_key=True)
    Blood_Pressure = models.CharField(max_length=20)
    Sugar = models.DecimalField(max_digits=5, decimal_places=2)
    Heartrate = models.IntegerField()

    def __str__(self):
        return f"Checkup {self.Checkup_Id}"


# class SpecialCheckupSchedule(models.Model):
#     specialcheckupid = models.OneToOneField(CheckupItem, primary_key=True, on_delete=models.CASCADE)
#     memberid = models.ForeignKey(Member, on_delete=models.CASCADE)
#     nurseid = models.ForeignKey(Nurse, on_delete=models.CASCADE)
#     doctorid = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     date = models.DateField()
#     frequency = models.PositiveIntegerField()
#     completed = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f"Special Checkup Schedule for {self.memberid}"