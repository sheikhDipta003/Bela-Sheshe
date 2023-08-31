from django.db import models
from viewflow.fields import CompositeKey
# Create your models here.
class Nurse(models.Model):
    Nurse_Id = models.AutoField(primary_key=True)
    Qualifications = models.CharField(max_length=50)
    Shift = models.CharField(max_length=20)

    def __str__(self):
        return f"Checkup {self.Nurse_Id}"

    #python manage.py makemigrations
#    python manage.py migrate