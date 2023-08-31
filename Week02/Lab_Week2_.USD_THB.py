# input path folder GEN64 for module
# ใส่พาธของโฟลเดอร์ GEN64 เพื่อที่จะสามารถเรียกใช้ไฟล์จากในโฟลเดอร์นั้นได้
# โฟลเดอร์ GEN64 ก็จะสามารถเก็บไฟล์ที่จะใช้เป็นมอดูลได้แล้ว
# ในกรณีที่ไฟล์ที่เราจะเรียกใช้อยู่คนละโฟลเดรอ์
import sys
sys.path.append("E:\Start Python\GEN64")

# ImportFile HeadDate
# เรียกใช้ฟังก์ชั่น Heading จากโฟลเดรอ์ Week01 
from Week01.HeadDate import Heading

# Returnค่ากับไปที่ฟังก์ชั่น Heading ที่ตัวแปร Lab ที่ไฟล์ HeadDate 
Heading("LP01-2")

# Input
print("Welcome to Exchange kiosk")
exchang_rate = float(input("Today THB-USD exchange rate : "))
USD = int(input("Enter $USD amount : "))
print("-------------------------------------------")

# Process USD >> THB , Fee, Net
THB = int(USD * exchang_rate)
Fee = THB * 0.02
Net = int(THB - Fee)
text ="{0} USD = {1} THB, Fee = {2:.2f} THB \nNet {3} THB"
print(text.format(USD, THB, Fee, Net))
print("-------------------------------------------")

# Process and Output money
print("Bank note and coin :")
money_list = (1000, 500, 100, 50, 20, 10, 5, 2, 1)
for index in money_list :
    if index >= 20 :
        print("Banknote {} : {}".format(index, int(Net / index)))
    else :
        print("Coin {} : {}".format(index, int(Net / index)))
    Net %= index
print("-------------------------------------------")