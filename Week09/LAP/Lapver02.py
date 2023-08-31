import numpy as np

Adult = np.array([16, 16, 19, 21, 23, 26, 28, 30, 33, 35, 37, 40, 42,42,42,42,42,42,42])
Elder_child = np.array([8, 8, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21,21,21,21,21,21,21])
Student = np.array([14, 14, 17, 19, 21, 23, 25, 27, 30, 32, 33, 36, 38,38,38,38,38,38])

print('MRT blue line ticket machibe')
print("Press 1 for Adult ticket\nPress 2 for Elder/child ticket\nPress 3 for Student ticket")

def type ():
    type_ticket = int(input('Enter your number : '))
    if type_ticket == 1:
        station = int(input("Please select station (0 - 18) : "))
        if station >=0 and station <= 18 :
            print("Fare = {} THB".format(Adult[station]))
            sum = Adult[station]
            return fare(sum)
    
    elif type_ticket == 2:
        station = int(input("Please select station (0 - 18) : "))
        if station >=0 and station <= 18 :
            print("Fare = {} THB".format(Elder_child[station]))
            sum = Elder_child[station]
            return fare(sum)
    
    elif type_ticket == 3:
        station = int(input("Please select station (0 - 18) : "))
        if station >=0 and station <= 18 :
            print("Fare = {} THB".format(Student[station]))
            sum = Student[station]
            return fare(sum)
        else:
            print("Fail try again")
            return type()

def fare (sum):
    coin = int(input("Please inset banknote/coin : "))
    if coin < sum:
        print("Require more cash....")
        return fare(sum)
    else:
        total = coin - sum
        print("Change {} THB".format(total))
        print("Get your ticket, Thanks you")

type()


