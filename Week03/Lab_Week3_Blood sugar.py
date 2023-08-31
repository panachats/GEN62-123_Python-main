# ใส่พาธของโฟลเดอร์ GEN64 เพื่อที่จะสามารถเรียกใช้ไฟล์จากในโฟลเดอร์นั้นได้
# โฟลเดอร์ GEN64 เก็บไฟล์ที่จะใช้เป็นมอดูลได้
import sys
sys.path.append("E:\Start Python\GEN64")
# ImportFile HeadDate
# เรียกใช้ฟังก์ชั่น Heading จากโฟลเดรอ์ Week01 
from Week01.HeadDate import Heading
# Return ค่ากับไปที่ฟังก์ชั่น Heading ที่ตัวแปร Lab ที่ไฟล์ HeadDate 
Heading("LP02-1")

# โปรแกรมประเมินความเสี่ยงของการเป็นโรคเบาหวาน
print("Diabetes measurement program")
# Input an int value to a BLS variable.
BLS = int(input("Enter blood sugar : "))
print("-"*40)
# Store the format string value in a rick and normal variable.
rick = "Blood sugar = {} mg/dL. You are rick."
normal = "Blood sugar = {} mg/dL. You are normal."
# if else and print rick and normal variable.
print(rick.format(BLS)) if BLS > 126 else print(normal.format(BLS))
print("-"*40)
