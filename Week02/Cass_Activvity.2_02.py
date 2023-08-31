print("School of Informatics")

# method1
IphonePrice = 30000
GPAX = 4.00
MyOrder = "IphonePrice : {:,} \nGPAX : {:.2f}"
print(MyOrder.format(IphonePrice,GPAX))
print("------------------------------------------------")

# method2
student_name = "Panachat Aiamnam"
student_id = "64107899"
TxT = "Name : {} \tID : {}"
print(TxT.format(student_name,student_id))
print("------------------------------------------------")

# method3
university_name = input("university : ")
faculty_name = input("faculty : ")
Name = "{0} \t\tfaculty : {1}"
print(Name.format(university_name,faculty_name))
print("------------------------------------------------")