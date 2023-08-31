from residents.models import CheckupItem

checkup_item1 = CheckupItem(bloodpressure='120/80', sugar=5.5, heartrate=75)
checkup_item2 = CheckupItem(bloodpressure='130/85', sugar=6.2, heartrate=80)

checkup_item1.save()
checkup_item2.save()
CheckupItem.objects.all()
exit()

from nurse.models import Nurse
item1 = Nurse(qualifications='BSN', shift='day')
item2 = Nurse(qualifications='BSN', shift='night')
item3 = Nurse(qualifications='BSN', shift='night')
item4 = Nurse(qualifications='BSN', shift='night')

item1.save()
item2.save()
item3.save()
item4.save()
Nurse.objects.all()
exit()
