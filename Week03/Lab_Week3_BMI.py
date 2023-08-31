# ใส่พาธของโฟลเดอร์ GEN64 เพื่อที่จะสามารถเรียกใช้ไฟล์จากในโฟลเดอร์นั้นได้
# โฟลเดอร์ GEN64 ก็บไฟล์ที่จะใช้เป็นมอดูลได้
import sys
sys.path.append("E:\Start Python\GEN64")
# ImportFile HeadDate
# เรียกใช้ฟังก์ชั่น Heading จากโฟลเดรอ์ Week01 
from Week01.HeadDate import Heading
# Return ค่ากับไปที่ฟังก์ชั่น Heading ที่ตัวแปร Lab ที่ไฟล์ HeadDate 
Heading("LP02-2")

# โปรแกรม Body Mass Index
print("Body Mass Index (BMI) Calculator")
# input an int value to a W and H variable.
W = float(input("Enter your weight(kg) : ")) 
H = float(input("Enter your height:(M) : "))
# Process W and H variables and store BMI variables.
BMI = W / (H ** 2 )
print("-"*28)
# if elif else and print BMI and result variable.
if BMI >= 30.0 :
    result = "You are Obese."
elif BMI >= 25.0 :
    result = "You are Overweight."
elif BMI >= 18.5 :
    result = "You are Healthy."
else :
    result = "You are Underweight."
print("BMI = {:.2f}.".format(BMI),result)
print("-"*28)
