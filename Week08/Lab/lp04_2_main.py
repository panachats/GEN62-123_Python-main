
#TODO ใส่พาธของโฟลเดอร์ GEN64 เพื่อที่จะสามารถเรียกใช้ไฟล์จากในโฟลเดอร์นั้นได้
import sys
sys.path.append("E:\Start Python\GEN64")

#TODO import ไฟล์ HeadDate ที่อยู่ในโฟลเดอร์ Week01 
from Week01.HeadDate import *

#TODO import ไฟล์ lp04_2_utilityfunc
from lp04_2_utilityfunc import *

#TODO เรียกใช้ Function Heading ที่อยู่ในอีกไฟล์
#* และส่งค่ากลับไป
Heading("LP04-2")

print("ข้อที่ 1 ")
#TODO เรียกใช้ function
print(validate_person_id(input('Enter your id : ')))
print('-'*43)

print("ข้อที่ 2 ")
#TODO เรียกใช้ function
print(get_email())