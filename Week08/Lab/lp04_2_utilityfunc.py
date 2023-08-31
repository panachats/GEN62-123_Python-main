
#?ข้อที่ 2
def validate_person_id (id): #TODO ประกาศ func
    sum_digit = 0 
    count = 13 #TODO กำหนดค่านับเป็น 13
    for x in range(len(id)): 
        if count == 1: #TODO ถ้าค่า count เท่ากับ 1
            last_digit = int(id[x]) #TODO ให้เก็บค่าที่วนจนค่า count ที่เป็น 1 ก็คือหลักสุดท้าย
            break #TODO ทำการหยุด
        sum_digit += int(id[x])*count  #TODO ทำการคูณและบวกสะสมค่า คูนตามจำนวนนับ
        count -= 1 #TODO และลบจำนวน count ไปเรื่อย ๆ
    mod = sum_digit % 11 #TODO นำผลลัพธ์มา mod 11
    check_digit = (11 - mod)%10 #TODO นำผลลัพธ์มาลบ 11 ถ้าค่ามากกว่า 9 ให้ % 10
    if check_digit == last_digit : #TODO ถ้าผลลัพธ์เท่าหลักสุดท้ายของ id 
        return True
    else:
        return False

#?ข้อที่ 2
def get_email (): #TODO ประกาศ func
    email = input("Enter your email : ") #TODO รับค่า
    at =0
    dot = 0
    character = {'$','#','!'} #TODO สร้างตัวแปร set เก็บค่า
    if email[0] == "@": #TODO เช็คว่า index ที่ 0 เท่ากับ @ ไหม
        print("Error")
        return get_email() #TODO ให้ return กลับไปทำ func ใหม่
    for x in email:
        if x in character:
            print("No Character",character)
            return get_email() #TODO ให้ return กลับไปทำ func ใหม่
        if x == '@': #TODO ตรวจสอบว่ามี @ อยู่ไหมถ้ามีให้เพิ่มค่าตามจำนวนที่มี
            at += 1 
        if x == '.': #TODO ตรวจสอบว่ามี . อยู่ไหมถ้ามีให้เพิ่มค่าตามจำนวนที่มี
            dot += 1
    if at == 1 and dot >=1 : #TODO เช็คว่า @ มีค่าเท่ากับ 1 ตัวไหม และ dot มีค่ามากกว่าหรือเท่ากับ 1 ไหม
        print("Success")
        return email #TODO return ค่ากลับไปแสดงมรส่วนของการเรียก func
    else:
        print("Error")
        return get_email() #TODO ให้ return กลับไปทำ func ใหม่



