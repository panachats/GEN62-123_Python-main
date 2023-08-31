
#? ข้อ 1
def avg (item): #TODO รับค่าจาก number
    total = 0
    for x in range(len(item)):
        total += item[x] #TODO บวกสะสม
    return total / len(item) #TODO หาค่าเฉลี่ยแล้วส่งค่ากลับไปแสดงที่บรรทัดที่ 9
number = [1,10,55,232,101] #TODO สร้าง list จำนวนเต็ม
print(avg(number))