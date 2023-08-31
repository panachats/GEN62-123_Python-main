from datetime import date, datetime


def Heading (Lab) :
    now  = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Excuted time: ", dt_string)
    name = "Panachat Aiamnam"
    std_id = "64107899"
    print(Lab +" Name : "+name+" Student ID: "+std_id)
    print("-------------------------------------------")
    return