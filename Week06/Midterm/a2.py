from datetime import date, datetime
now  = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Excuted time: ", dt_string)
name = "Panachat Aiamnam"
std_id = "64107899"
lab = "Quiz-2"
print(lab +" Name : "+name+" Student ID: "+std_id)
print("-"*52)

#----------------------------------------------------------------
print('Elevator controller programe...')
total = 0
x = 0
print('-'*25)
for x in range(15) :
    person_weight = int(input("Enter person {} weight ".format(x+1)))
    total += person_weight
    if person_weight == 0 :
        print('-'*25)
        break
    if total > 1200 :
        print('-'*25)
        print("Warning :\nperson {} is over weight, please leave....".format(x+1))
        print("Door closed, {} person(s), total weight {} KG".format(x,total-person_weight))
        break
if total < 1200 :
    print("Door closed, {} person(s), total weight {} KG".format(x+1,total))