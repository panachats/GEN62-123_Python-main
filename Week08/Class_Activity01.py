def averageNumber () : #TODO สร้าง Function
    number1 = int(input("Enter Namber1 : "))
    number2 = int(input("Enter Namber2 : "))
    number3 = int(input("Enter Namber3 : "))
    average = (number1 + number2 + number3) / 3 #TODO หาผลรวม และค่าเฉลี่ย
    sum = number1 + number2 #TODO หาผลรวม
    #TODO if else ถ้า else ให้กลับมาเรียกใช้ Function 
    print("The end") if average > sum else averageNumber()
#TODO เรียกใช้ function
averageNumber()


