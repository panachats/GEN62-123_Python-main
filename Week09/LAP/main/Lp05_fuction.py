import numpy as np

Adult = np.array([16, 16, 19, 21, 23, 26, 28, 30, 33, 35, 37, 40, 42])
Elder_child = np.array([8, 8, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21])
Student = np.array([14, 14, 17, 19, 21, 23, 25, 27, 30, 32, 33, 36, 38])

type_ticket = int(input(": ")) #TODO รับค่าประเภท

def get_station ():
    station = int(input("Please select station (0 - 18) : "))
    if station >=12 and station <= 18 : 
        return selection(12) #TODO ให้รีกลับไปที่ฟังก์ชั่น selection
    elif station >= 0 and station <= 18:
        return selection(station) #TODO ให้รีกลับไปที่ฟังก์ชั่น selection
    else:
        print("Fail try again")
        get_station() #TODO ให้กลับไปทำget_station อีกครั้ง

def selection (station): #TODO รับ agument มาจากฟังก์ชั่น get_station มาใส่ใน parameter
    if type_ticket == 1:
        fare = Adult[station] #TODO เข้าถึง index ของตัวแปร array ตามค่าที่ส่งมา
    elif type_ticket == 2:
        fare = Elder_child[station] #TODO เข้าถึง index ของตัวแปร array ตามค่าที่ส่งมา
    elif type_ticket == 3:
        fare = Student[station] #TODO เข้าถึง index ของตัวแปร array ตามค่าที่ส่งมา
    print("Fare = {} THB".format(fare))
    return get_fare(fare) #TODO ส่งค่า fare ไปใช่ใน function get_fare

def get_fare (fare): #TODO รับ agument มาจากฟังก์ชั่น selection มาใส่ใน parameter
    coin = int(input("Please inset banknote/coin : "))
    if coin < fare:
        print("Require more cash....")
        return get_fare(fare) #TODO ให้กลับไปทำget_fare อีกครั้ง
    else:
        total = coin - fare
        print("Change {} THB".format(total))
        print("Get your ticket, Thanks you")




