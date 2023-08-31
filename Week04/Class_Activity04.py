# ข้อที่ 1 สร้ําง List
List = ["Jessy", "Ammy", "Luzy", "Jenny", "John"]
print(List)
# ข้อที่ 2 เรียกใช้ข้อมูล Ammy
print(List[1])

# ข้อที่ 3 ลบข้อมูล Jenny ออกจําก list
List.pop(3)
print(List)

# เข้อที่ 4 พิ่มข้อมูล BigBoss ต่อท้ําย list
List.append("BigBoss")
print(List)

# ข้อที่ 5 แสดงสมาชิกเฉพาะ Luzy, Jenny และ John
List.clear()
List = ["Jessy", "Ammy", "Luzy", "Jenny", "John"]
print(List[2:5])

# ข้อที่ 6 แสดงสมาชิก Jessy และ Ammy
print(List[:-3]) # นับจากตัวด้านหลัง

