patientsdict = {
    "first_name" : " ",
    "last_name" : " ",
    "age" : 0,
    "weight" : 0,
}
print("welcome to Walailak Hospital")
fname = input('Enter first name : ')
patientsdict.update({'first_name':fname})
lname = input('Enter last name : ')
patientsdict.update({'last_name':lname})
age = int(input('Enter age : '))
patientsdict.update({'age':age})
weight = float(input('Enter weight : '))
patientsdict.update({'weight':weight})
print("Name {} {} Age : {} Weight : {:.2f}".format(fname,lname,age,weight))

