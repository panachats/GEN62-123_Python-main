from datetime import date, datetime

def get_info_dict(persondict):
    now = datetime.now()
    persondict.update({'datetime': now.strftime("%d/%m/%Y %H:%M:%S")})
    persondict.update({'fname':input("Enter first name: ")})
    persondict.update({'lname':input("Enter last name: ")})
    persondict.update({'age':int(input("Enter age: "))})
    persondict.update({'body_temp':float(input("Enter body temperture: "))})
    provice = open("provice.txt")
    print(provice.read())
    provice.close()
    persondict.update({'location':int(input("Enter : Enter location number: "))})

def evaluation (persondict):
    if persondict.get("location") > 0 and persondict.get("location") <= 28:
        persondict.update({"risk":True})
        if persondict.get("body_temp") > 37.5:
            persondict.update({"covid":True})
        else:
            persondict.update({"covid":False})
    else:
        persondict.update({"risk":False})
        persondict.update({"covid":False})



