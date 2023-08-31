import numpy as np
from datetime import date, datetime
now  = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Excuted time: ", dt_string)
name = "Panachat Aiamnam"
std_id = "64107899"
lab = "Quiz4"
print(lab +" Name : "+name+" Student ID: "+std_id)
print("-"*52)

day1 = np.array ([70,75,80,88,72,92])
day2 = np.array ([99,101,80,85,79,82])
day3 = np.array ([100,89,95,120,122,99])

def da (day,d):
    total = 0
    print("Day {} ".format(d))
    for i in range(len(day)):
        print("time#{} : {} ".format(i+1,day[i]))
        total += day[i]
    print("Average : {:.1f} ".format(total / len(day)))
    print('-'*25)

da(day1,1)
da(day2,2)
da(day3,3)