
#? ข้อ 2
def temperature (): #TODO สร้าง function
    number = float(input("Enter : ")) #TODO รับค่าอุณหภูมิเข้ามา
    if number > 37.5: #TODO เปรียบเทียบ
        result = True
    else:
        result = False
    return result #TODO return กลับไปแสดงที่บรรทัดที่ 9
print(temperature())