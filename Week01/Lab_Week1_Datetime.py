from datetime import date, datetime
now  = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Excuted time: ", dt_string)
name = "Panachat Aiamnam"
std_id = "64107899"
lab = "LP01-1"
print(lab +" Name : "+name+" Student ID: "+std_id)
print("-"*52)

number1 = 50
number2 = 35
summation = 0
print("Hello world")
print("This is my first program")
summation = number1 +  number2
txtprint = "{} + {} = {}"
print(txtprint.format(number1,number2,summation))