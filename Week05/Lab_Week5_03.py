import sys
sys.path.append("E:\Start Python\GEN64")
from Week01.HeadDate import Heading
Heading("LP03-2")

i = 0
height =[]
weight =[]

print('Childrtens record list...')
children = int(input("How many children(s) : " ))
print('-'*20)
while i < children :
    print("Children #{}".format(i+1))
    weight.append(float(input("Enter weight(kg) : ")))
    height.append(float(input("Enter height(M) : "))) 
    print('-'*20)
    i += 1

#TODO สร้าง Function และรับตัวแปร list height and weight มาเก็บที่ agrs
def Average (agrs) :
    total = 0
    for x in range(len(agrs)):
        total +=  agrs[x]
    avg = total / len(agrs)
    return avg #TODO retun ค่า avg กลับไปที่ agrs และ agrs จะส่งค่ากลับไปที่ตัว list
#TODO format weight and height ที่อยู่ใน Function Average
print("Average of weight = {:.2f} kg".format(Average(weight)))
print("Average of height = {:.2f} M".format(Average(height)))





