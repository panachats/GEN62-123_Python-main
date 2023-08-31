import sys
sys.path.append("E:\Start Python\GEN64")
from Week01.HeadDate import Heading
Heading("LP03-1-2")

#TODO สร้างตัวแปรที่มี list ว่าง
GPAX = []
for x in range(10) : #TODO วน loop 10 ครั้ง
    GPAX.append(float(input("Enter GPAX of Student No.{} : ".format(x+1))))
print(GPAX)
print("-"*44)

#TODO นำ index 1, 2, 3 มาหาผลรวม แล้วนำมาหาร 3
print("Average of GPAX :{:.2f}".format((GPAX[1]+GPAX[2]+GPAX[4]) / 3))
print("-"*44)

#TODO สร้างตัวแปร max and min
max = 0
min = 4
for i in GPAX : #TODO i วนรอบตามจำจวนสมาชิกใน list
    if (i > max) : #TODO หาค่ามากสุดใน list
        max = i
print("Max GPAX :",max)
print("-"*44)

for y in GPAX : #TODO y วนรอบตามจำจวนสมาชิกใน list
    if (y < min) : #TODO หาค่าน้อยสุดใน list
        min = y
print("Max GPAX :",min)
print("-"*44)