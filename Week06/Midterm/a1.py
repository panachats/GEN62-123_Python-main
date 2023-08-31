from datetime import date, datetime
now  = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Excuted time: ", dt_string)
name = "Panachat Aiamnam"
std_id = "64107899"
lab = "Quiz-1"
print(lab +" Name : "+name+" Student ID: "+std_id)
print("-"*52)

#----------------------------------------------------------------
print('Water billing program...')
print('-'*25)
tap_water = int(input("Enter water unit(s) : "))
service_month = 30
print('-'*25)

if tap_water > 30  :
    total = (tap_water * 20) + service_month
elif tap_water > 15 and tap_water <= 30 :
    total = (tap_water * 15) + service_month
else:
    total = (tap_water * 10) + service_month

print('Total cost =',total)