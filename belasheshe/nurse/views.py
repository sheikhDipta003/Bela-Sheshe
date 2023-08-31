# from django.shortcuts import render
#
# # Create your views here.
# def nurse_dashboard(request):
#     return render(request, 'nurse/dashboard.html')

from django.shortcuts import render
from django.views import View
from .models import Member,Medicine, MedicineChart,Dosage,CheckupSchedule,CheckupItem

class DashboardView(View):
    template_name = 'nurse/dashboard.html'  # Update with your actual template name

    def getMedicineSchedule(nurse_id):
        members = Member.objects.filter(Nurse_id=nurse_id)
        rows=[]
        for member in members:
            medicine_chart=MedicineChart.objects.filter(Member_id=member.Mem_id)
            dosage=Dosage.objects.filter(Chart_id=medicine_chart.Chart_id)
            medicine_name=Medicine.objects.filter(Medicine_id=dosage.Medicine_id).Name
            data = {
                'name': medicine_name,
                'time': dosage.Time,
                'quantity': dosage.Quantity
            }
            rows.append(data)

        sorted_rows = sorted(rows, key=lambda row: row['time'])
        return sorted_rows

    def getCheckupSchedule(nurse_id,date):
        checkups = CheckupSchedule.objects.filter(Nurse_id=nurse_id,Date=date).order_by('Time')
        rows=[]
        for checkup in checkups:
            checkup_item = CheckupItem.objects.filter(Checkup_id=checkup.Checkup_id)
            data = {
                'item': checkup_item,
                'time': checkup.Time,
            }
            rows.append(data)
        return rows

    def get(self, request, nurse_id,date, *args, **kwargs):
        schedules= self.getMedicineSchedule(nurse_id)
        schedules.append(self.getCheckupSchedule(nurse_id, date))
        sorted_rows = sorted(schedules, key=lambda row: row['time'])
        return render(request, self.template_name, {'schedules': schedules})

class CheckupDataEntryView(View):
    template_name = 'nurse/addCheckupData.html'  # Update with your actual template name
    def get(self, request,*args, **kwargs):
        return render(request, self.template_name)

    def addData(self,request,*args, **kwargs):
        if request.method == 'POST':
            # Get data from the POST request
            bp = request.POST.get('Blood_pressure')
            sugar = request.POST.get('Sugar')
            hr = request.POST.get('Heartrate')

            # Create a new instance of MyModel and set values
            new_instance = CheckupItem(Blood_pressure=bp, Sugar=sugar, Heartrate=hr)

            # Save the instance to the database
            new_instance.save()
            return redirect('success_page')

class ResidentConditionView(View):
    template_name = 'nurse/residentCondition.html'  # Update with your actual template name

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def retrieveData(self, request, *args, **kwargs):
        checkups = CheckupSchedule.objects.filter(Nurse_id=nurse_id, Completed="true")
        rows = []
        for checkup in checkups:
            checkup_item = CheckupItem.objects.filter(Checkup_id=checkup.Checkup_id)
            bp = checkup_item.Blood_pressure
            sugar = checkup_item.Sugar
            hr = checkup_item.Heartrate

            bpRiskRate=self.getRiskRate(bp)
            sugarRiskRate=self.getSugarRiskRate(sugar)
            riskrate=max(bpRiskRate,sugarRiskRate)
            data = {
                'memid':checkup.Member_id,
                'checkupid':checkup.Checkup_id,
                'bp': bp,
                'sugar':sugar,
                'riskrate': riskrate
            }
            rows.append(data)
        sorted_rows = sorted(rows, key=lambda row: row['riskrate'])
        return sorted_rows

    def getSugarRiskrate(self, sugar):
        riskrate = 0
        if (sugar >= 5 and sugar <= 6.5):
            riskrate = 0
        elif (sugar >= 6.5 and sugar <= 6.9):
            riskrate = 1
        elif (sugar >= 7 and sugar <= 12):
            riskrate = 2
        elif (sugar >= 12):
            riskrate = 3
        return riskrate

    def getBpRiskrate(self, bp):
        riskrate = 0
        if (bp >= 115 and bp <= 125):
            riskrate = 0
        elif (bp >= 125 and bp <= 135):
            riskrate = 1
        elif (bp >= 135 and bp <= 160):
            riskrate = 2
        elif (bp >= 160):
            riskrate = 3
        return riskrate
    def reportDoctor(self, request, member_id,*args, **kwargs):

    

# class PrescriptionListView(View):
#     template_name = 'prescription_list.html'  # Update with your actual template name

#     def get(self, request, member_id, *args, **kwargs):
#         member = Member.objects.get(Member_ID=member_id)
#         prescriptions = Prescription.objects.filter(Member_ID=member_id)
#         return render(request, self.template_name, {'member': member, 'prescriptions': prescriptions})
