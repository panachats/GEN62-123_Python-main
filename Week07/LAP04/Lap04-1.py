
#TODO ใส่พาธของโฟลเดอร์ GEN64 เพื่อที่จะสามารถเรียกใช้ไฟล์จากในโฟลเดอร์นั้นได้
import sys
sys.path.append("E:\Start Python\GEN64")

#TODO import ไฟล์ HeadDate ที่อยู่ในโฟลเดอร์ Week01 และตั้งชื่อให้กับไฟล์ที่มีฟังก์ชั่นอยู่สำหรับไว้เรียกใช้งาน
import Week01.HeadDate as Hd

#TODO import ไฟล์ function_def และตั้งชื่อให้กับไฟล์ที่มีฟังก์ชั่นอยู่สำหรับไว้เรียกใช้งาน
import function_def as fn

#TODO เรียกใช้ Function Heading ที่อยู่ในอีกไฟล์
#* และส่งค่ากลับไป
Hd.Heading("LP04-1")

#TODO เรียกใช้ function calculate_circle_area 
#* ส่งค่า Agument ไปที่ Parameter ที่อยู่ใน Function calculate_circle_area 
fn.calculate_circle_area(5)
fn.calculate_circle_area(8)

#TODO เรียกใช้ func function calculate_circle_circumference
#* ส่งค่า Agument ไปที่ Parameter ที่อยู่ใน Function calculate_circle_circumference
fn.calculate_circle_circumference(9)
fn.calculate_circle_circumference(4)

#TODO เรียกใช้ function calculate_retangle_area
#* ส่งค่า Agument ไปที่ Parameter ที่อยู่ใน Function calculate_retangle_area
fn.calculate_retangle_area(3,5)
fn.calculate_retangle_area(3,9)

#TODO เรียกใช้ function calculate_triangle_area
#* ส่งค่า Agument ไปที่ Parameter ที่อยู่ใน Function calculate_triangle_area
fn.calculate_triangle_area(2,5)
fn.calculate_triangle_area(5,9)