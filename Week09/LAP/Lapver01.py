import numpy as np

adult = np.array([16, 16, 19, 21, 23, 26, 28, 30, 33, 35, 37, 40, 42])
elderchild = np.array([8, 8, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21])
student = np.array([14, 14, 17, 19, 21, 23, 25, 27, 30, 32, 33, 36, 38])

print('MRT blue line ticket machibe')
print("Press 1 for Adult ticket\nPress 2 for Elder/child ticket\nPress 3 for Student ticket")

def select_type():
    press_type = int(input())
    return press_type

def station ():
    press_station = int(input("Please select station (0-18) : "))
    if press_station >= 12 and press_station <= 18:
        return 12
    elif press_station >= 0 :
        return press_station
    else:
        print("Fail try again")
        return station()

def type_ticket (press_type,press_station):
    if press_type == 1:
        sum = adult[press_station]
    elif press_type == 2:
        sum = elderchild[press_station]
    elif press_type ==3:
        sum = student[press_station]
    print("Fare = {} THB".format(sum))
    return fare(sum)

def fare(sum):
    coin = int(input("Plaease inset banknote/coin : "))
    if coin < sum :
        print("Require more cash......")
        return fare(sum)
    else:
        total = coin - sum
        print("Change {} THB".format(total))
        print("Get your ticket, Thanks you")

p_ty = select_type()
p_sta = station()
se = type_ticket(p_ty,p_sta)



            
