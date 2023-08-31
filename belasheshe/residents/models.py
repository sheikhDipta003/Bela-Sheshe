from django.db import models
from viewflow.fields import CompositeKey
from doctors.models import Doctor
# from healthcare.models import ResidentRoomAsgn, Doctor, Nurse, MedCond
# from .member import Member

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
        return f"Name {self.Name}, ID {self.Member_ID}"


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
    Doctor_ID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # Nurse_ID = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    Date = models.DateField()
    Time = models.TimeField()

    def __str__(self):
        return f"Appointment {self.App_ID} for {self.Member_ID}"

class Medicine(models.Model):
    Medicine_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Generic_name=models.CharField(max_length=50)
    Company = models.CharField(max_length=50)
    Price=models.IntegerField()
    Miligram=models.IntegerField()
    Available_quantity=models.IntegerField()

    def __str__(self):
        return f"Medicine {self.Name}, available quantity {self.Available_quantity}"

class Medicine_chart(models.Model):
    Chart_ID = models.AutoField(primary_key=True)
    Member_ID = models.ForeignKey(Member, on_delete=models.CASCADE)
    Advice=models.CharField(max_length=500)
    Date=models.DateField()

    def __str__(self):
        return f"Medicine_chart for {self.Member_ID}, Date {self.Date}"