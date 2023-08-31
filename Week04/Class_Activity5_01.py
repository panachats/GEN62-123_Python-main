# ข้อ 1
i = 0
lotto_list = [] # ประกาศ list
while i < 10:
    # รับค่าตัวเลข
    num = int(input("Enter Three Number Lotto {} :".format(i+1))) 
    lotto_list.append(num) # เพิ่มค่าลงไปใน list
    i += 1 
print(lotto_list)
