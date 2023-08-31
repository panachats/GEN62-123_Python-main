import sys
sys.path.append("E:\Start Python\GEN64")
from Week01.HeadDate import Heading
Heading("LP03-1-1")

#? ข้อที่ 1
flight_landing_list = ["SL789","FD3187"] #TODO กำหนดค่าใน list
print(flight_landing_list)

#? ข้อที่ 2
flight_landing_list.append(input("Enter flight no : ")) #TODO input
print(flight_landing_list)

#? ข้อที่ 3
flight_landing_list.pop(0) #TODO ลบสมาชิกใน index 0
print(flight_landing_list)

#? ข้อที่ 4
print(flight_landing_list[1]) #TODO print index 1

#? ข้อที่ 5
print(flight_landing_list[0]) #TODO print index 0

#? ข้อที่ 6
flight_landing_list[0] = "FD3188" #TODO ทำการแก้ไขข้อมูลใน index 0
print(flight_landing_list)

#? ข้อที่ 7
flight_landing_list.append(input("Enter flight no : ")) #TODO input and append
flight_landing_list.append(input("Enter flight no : ")) #TODO input and append
print(flight_landing_list)

#? ข้อที่ 8
flight_landing_list.remove(input("Enter flight No. to remove :")) #TODO remove member in list
print(flight_landing_list)

#? ข้อที่ 9
flight_landing_list.clear() #TODO ทำการล้างข้อมูลสมาชิกภายใน list
print(flight_landing_list)